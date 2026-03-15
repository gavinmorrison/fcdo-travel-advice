#!/usr/bin/env python3
"""
FCDO Travel Advice Status Checker

This script fetches travel advice data from the UK Foreign, Commonwealth & Development Office (FCDO)
API and generates a Markdown table showing the current travel advisory status for all countries.

The script categorizes countries using a traffic light system:
🔴 Red: FCDO advises against all travel to the whole country
⚠️  Warning: FCDO advises against all travel to parts of the country
🟡 Yellow: FCDO advises against all but essential travel
🟢 Green: No specific travel advisories active
❓ Unknown: Error or unrecognized alert status

Author: Gavin Morrison
License: MIT
Version: 1.0.0
"""

import sys
import os
import requests
import json
import argparse
from datetime import datetime

__version__ = "1.0.0"
__author__ = "FCDO Travel Advice Monitor"
__license__ = "MIT"

BASE_URL = "https://www.gov.uk/api/content/foreign-travel-advice"

# Define alert levels for easier checking
RED_ALERTS = {
    "avoid_all_travel_to_whole_country",
    "avoid_all_travel_to_parts"
}
YELLOW_ALERTS = {
    "avoid_all_but_essential_travel_to_whole_country",
    "avoid_all_but_essential_travel_to_parts"
}

# Human-readable templates
ADVICE_TEMPLATES = {
    "avoid_all_travel_to_whole_country": "FCDO advises against all travel to {country_name}.",
    "avoid_all_travel_to_parts": "FCDO advises against all travel to parts of {country_name}.",
    "avoid_all_but_essential_travel_to_whole_country": "FCDO advises against all but essential travel to {country_name}.",
    "avoid_all_but_essential_travel_to_parts": "FCDO advises against all but essential travel to parts of {country_name}."
}

# Define test slugs - Updated expected results
TEST_SLUGS = [
    "colombia",      # Expected: 🟡 Yellow
    "north-korea",   # Expected: 🟡 Yellow
    "turkey",        # Expected: ⚠️ Warning (avoid_all_travel_to_parts only)
    "azerbaijan",    # Expected: ⚠️ Warning (avoid_all_travel_to_parts AND avoid_all_but_essential_travel_to_parts)
    "yemen",         # Expected: 🔴 Red (avoid_all_travel_to_whole_country)
    "norway"         # Expected: 🟢 Green
]

def fetch_json(url):
    """Fetches JSON data from a URL."""
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}", file=sys.stderr)
        return None

def translate_advice(alert_list, country_name):
    """Translates API alert slugs into human-readable sentences."""
    if not alert_list:
        return "No specific FCDO travel advisories are currently active."

    readable_advice = []
    unknown_alerts = []
    for alert in alert_list:
        template = ADVICE_TEMPLATES.get(alert)
        if template:
            readable_advice.append(template.format(country_name=country_name))
        else:
            unknown_alerts.append(alert)

    output = "<br />".join(readable_advice)

    if unknown_alerts:
        unknown_str = ", ".join(unknown_alerts)
        warning_msg = f"Unrecognized alerts: {unknown_str}"
        if output:
             output += f"<br />({warning_msg})"
        else:
             output = warning_msg
        print(f"Warning: Found unrecognized alert values for {country_name}: {unknown_alerts}", file=sys.stderr)

    return output

def get_traffic_light_status(alert_list):
    """Determines the traffic light emoji based on FCDO rules (updated 🔴/🔴* logic)."""
    if not isinstance(alert_list, list):
        print(f"Warning: Unexpected alert_list type: {type(alert_list)}. Assigning '❓'.", file=sys.stderr)
        return "❓"

    current_alerts = set(alert_list)
    has_red_whole = "avoid_all_travel_to_whole_country" in current_alerts
    has_red_parts = "avoid_all_travel_to_parts" in current_alerts
    has_any_yellow = bool(current_alerts.intersection(YELLOW_ALERTS))

    # Apply rules in order of precedence based on confirmed logic
    if has_red_whole:
        # Rule: 🔴 if 'whole_country' red alert exists (takes precedence)
        emoji = "🔴"
    elif has_red_parts:
         # Rule: ⚠️ if 'parts' red alert exists AND 'whole_country' red alert does NOT exist
         emoji = "⚠️"
    elif has_any_yellow:
        # Rule: 🟡 if any Yellow alerts exist AND no Red alerts exist
        emoji = "🟡"
    elif not alert_list:
         # Rule: 🟢 if list is empty (no alerts)
         emoji = "🟢"
    else:
        # Rule: ❓ if list has content but none match known Red/Yellow alerts
        if any(alert not in ADVICE_TEMPLATES for alert in alert_list):
             emoji = "❓" # Contains unrecognized alerts
        else:
             # Contains known alerts, but didn't trigger Red/Yellow/Green logic (should not happen ideally)
             print(f"Warning: Alert list {alert_list} didn't match Red/Yellow/Green rules, but contains known values. Assigning '❓'.", file=sys.stderr)
             emoji = "❓"
    return emoji

def get_country_data(slug):
    """Fetches and processes data for a single country."""
    url = f"{BASE_URL}/{slug}"
    data = fetch_json(url)

    if data is None:
        return {"slug": slug, "country": slug.replace('-', ' ').title(), "alert_list": None, "error": "Failed to fetch API data"}

    try:
        details = data.get("details", {})
        country_name = details.get("country", {}).get("name", slug.replace('-', ' ').title())
        alert_list = details.get("alert_status")
        change_history = details.get("change_history", [])
        reviewed_at = details.get("reviewed_at")
        error_msg = None

        if alert_list is None:
             error_msg = "Missing 'alert_status' in API response"
             alert_list = None
        elif not isinstance(alert_list, list):
             error_msg = f"Invalid 'alert_status' type: {type(alert_list)}"
             alert_list = None

        return {
            "country": country_name,
            "slug": slug,
            "alert_list": alert_list,
            "change_history": change_history,
            "reviewed_at": reviewed_at,
            "error": error_msg
        }
    except Exception as e:
        print(f"Error processing data for {slug}: {e}\nData: {json.dumps(data)}", file=sys.stderr)
        return {"slug": slug, "country": slug.replace('-', ' ').title(), "alert_list": None, "error": f"Error processing API response: {str(e)}"}


def get_all_country_slugs(base_url):
    """Fetches the list of all country slugs from the API."""
    print("Fetching full country list...", file=sys.stderr)
    root_data = fetch_json(base_url)
    if root_data is None or 'links' not in root_data or 'children' not in root_data['links']:
        print("❌ Error: Could not fetch the main country list from API.", file=sys.stderr)
        return None

    slugs = []
    all_countries_data = root_data['links']['children']
    print(f"Found {len(all_countries_data)} countries in API list. Extracting slugs...", file=sys.stderr)
    for i, country_link_data in enumerate(all_countries_data, start=1):
        slug = country_link_data.get('details', {}).get('country', {}).get('slug')
        if slug:
            slugs.append(slug)
        else:
            title = country_link_data.get('title', f'Unknown Entry {i}')
            print(f"⚠️ Skipping entry '{title}' due to missing slug.", file=sys.stderr)
    return slugs

def fetch_all_country_data(slugs):
    """Fetches data for a list of country slugs."""
    total_slugs = len(slugs)
    print(f"Fetching details for {total_slugs} countries...", file=sys.stderr)
    all_results = []
    for i, slug in enumerate(slugs, start=1):
        print(f"Fetching {i}/{total_slugs}: {slug}", file=sys.stderr)
        all_results.append(get_country_data(slug))
    return all_results

def generate_markdown_table(results, country_pages_dir=None):
    """Generates the Markdown table rows from processed country data."""
    markdown_rows = [
        "| Status | Country | FCDO Advice |",
        "|:------:|---------|-------------|"
    ]
    processed_count = 0
    error_count = 0
    print(f"Generating Markdown table for {len(results)} countries...", file=sys.stderr)
    for result in results:
        country_name = result.get('country', 'Unknown')
        slug = result.get('slug', '')
        if country_pages_dir and slug:
            link = f"{country_pages_dir}/{slug}.md"
        elif slug:
            link = f"https://www.gov.uk/foreign-travel-advice/{slug}"
        else:
            link = "#"

        if result.get("error"):
            emoji = "❓"
            advice_text = f"Error: {result['error']}"
            error_count += 1
        elif result.get("alert_list") is None:
             emoji = "❓"
             advice_text = "Error: Invalid or missing alert data during processing."
             error_count += 1
        else:
            alert_list = result['alert_list']
            emoji = get_traffic_light_status(alert_list)
            advice_text = translate_advice(alert_list, country_name)
            if emoji == '❓' and not advice_text.startswith("Unrecognized alerts") and not advice_text.startswith("Error:"):
                 advice_text = "Error: Could not determine status from alerts."
                 error_count += 1
            processed_count += 1

        markdown_rows.append(f"| {emoji} | [{country_name}]({link}) | {advice_text} |")

    print(f"\nProcessed {processed_count}/{len(results)} countries successfully. Encountered {error_count} errors/unknown statuses.", file=sys.stderr)
    return "\n".join(markdown_rows)

def format_date(iso_date):
    """Formats an ISO date string to GOV.UK style, e.g. '14 June 2025'."""
    try:
        dt = datetime.fromisoformat(iso_date.replace("Z", "+00:00"))
        return dt.strftime("%-d %B %Y")
    except (ValueError, AttributeError):
        return iso_date[:10] if iso_date else ""


def generate_country_page(result):
    """Generates a Markdown page for a single country with current status and change history."""
    country_name = result.get('country', 'Unknown')
    slug = result.get('slug', '')
    alert_list = result.get('alert_list', [])
    change_history = result.get('change_history', [])
    reviewed_at = result.get('reviewed_at', '')
    fcdo_url = f"https://www.gov.uk/foreign-travel-advice/{slug}"

    emoji = get_traffic_light_status(alert_list) if alert_list is not None else "❓"
    advice_text = translate_advice(alert_list, country_name) if alert_list is not None else "Unable to determine status."

    lines = []
    lines.append(f"# {country_name} {emoji}")
    lines.append("")
    lines.append(advice_text.replace("<br />", "\n\n"))
    lines.append("")
    if reviewed_at:
        lines.append(f"*Last reviewed by FCDO: {format_date(reviewed_at)}*")
        lines.append("")
    lines.append(f"[View current FCDO travel advice for {country_name}]({fcdo_url})")
    lines.append("")
    lines.append("---")
    lines.append("")

    if change_history:
        lines.append("## Change History")
        lines.append("")

        # Group entries by year
        years = {}
        for entry in change_history:
            timestamp = entry.get("public_timestamp", "")
            note = entry.get("note", "No details provided.")
            year = timestamp[:4] if len(timestamp) >= 4 else "Unknown"
            years.setdefault(year, []).append((timestamp, note))

        sorted_years = sorted(years.keys(), reverse=True)

        for i, year in enumerate(sorted_years):
            entries = years[year]
            if i == 0:
                # Most recent year: open by default
                lines.append(f"### {year}")
                lines.append("")
                for timestamp, note in entries:
                    lines.append(f"**{format_date(timestamp)}**")
                    lines.append(f"<br />{note}")
                    lines.append("")
            else:
                # Older years: collapsed
                lines.append(f"<details>")
                lines.append(f"<summary><strong>{year}</strong> ({len(entries)} update{'s' if len(entries) != 1 else ''})</summary>")
                lines.append("")
                for timestamp, note in entries:
                    lines.append(f"**{format_date(timestamp)}**")
                    lines.append(f"<br />{note}")
                    lines.append("")
                lines.append(f"</details>")
                lines.append("")

    return "\n".join(lines)


def write_country_pages(results, output_dir):
    """Writes individual Markdown pages for each country."""
    os.makedirs(output_dir, exist_ok=True)
    count = 0
    for result in results:
        slug = result.get('slug', '')
        if not slug:
            continue
        page_content = generate_country_page(result)
        filepath = os.path.join(output_dir, f"{slug}.md")
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(page_content)
            count += 1
        except IOError as e:
            print(f"Error writing country page {filepath}: {e}", file=sys.stderr)
    print(f"Wrote {count} country pages to {output_dir}/", file=sys.stderr)


def write_output(content, filename):
    """Writes the given content to a file or standard output."""
    if filename:
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Successfully wrote results to {filename}", file=sys.stderr)
        except IOError as e:
            print(f"❌ Error writing to file {filename}: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print(content)


def main(args):
    """Fetches countries, gets status, sorts, and prints/writes Markdown table."""

    output_filename = None
    if args.output:
        output_filename = args.output
        print(f"Output will be written to file: {output_filename}", file=sys.stderr)
    elif args.test:
        output_filename = "TEST.md"
        print(f"Test mode active. Output will be written to default file: {output_filename}", file=sys.stderr)
    else:
         print(f"Output will be written to standard output.", file=sys.stderr)

    if args.test:
        print("🧪 Running in test mode with predefined slugs.", file=sys.stderr)
        slugs_to_process = TEST_SLUGS
    else:
        slugs_to_process = get_all_country_slugs(BASE_URL)
        if slugs_to_process is None:
            sys.exit(1)

    all_results = fetch_all_country_data(slugs_to_process)

    # Sort results alphabetically
    all_results.sort(key=lambda x: x.get('country', ''))
    print(f"\nSorting complete.", file=sys.stderr)

    # Generate country pages
    countries_dir = "countries"
    if not args.test:
        write_country_pages(all_results, countries_dir)

    final_markdown = generate_markdown_table(all_results, countries_dir if not args.test else None)

    write_output(final_markdown, output_filename)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Fetch FCDO travel advice and generate a Markdown table.",
        epilog=f"Version {__version__} - {__license__} License"
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}"
    )
    parser.add_argument(
        "--test",
        action="store_true",
        help="Run in test mode using a predefined list of country slugs (outputs to TEST.md by default)."
    )
    parser.add_argument(
        "-o", "--output",
        metavar="FILE",
        help="Specify output file path (default: stdout, or TEST.md if --test is used)."
    )
    parsed_args = parser.parse_args()
    main(parsed_args)