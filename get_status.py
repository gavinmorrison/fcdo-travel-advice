import requests
import sys
import json # Import json for potential error details
import argparse # Import argparse for command-line flags

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
    "turkey",        # Expected: 🔴* Red* (avoid_all_travel_to_parts only)
    "azerbaijan",    # Expected: 🔴* Red* (avoid_all_travel_to_parts AND avoid_all_but_essential_travel_to_parts)
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
    has_any_red = has_red_whole or has_red_parts
    has_any_yellow = bool(current_alerts.intersection(YELLOW_ALERTS))

    # Apply rules in order of precedence based on confirmed logic
    if has_red_whole:
        # Rule: 🔴 if 'whole_country' red alert exists (takes precedence)
        emoji = "🔴"
    elif has_red_parts:
         # Rule: 🔴* if 'parts' red alert exists AND 'whole_country' red alert does NOT exist
         emoji = "🔴*"
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
            "error": error_msg
        }
    except Exception as e:
        print(f"Error processing data for {slug}: {e}\nData: {json.dumps(data)}", file=sys.stderr)
        return {"slug": slug, "country": slug.replace('-', ' ').title(), "alert_list": None, "error": f"Error processing API response: {str(e)}"}


def main(args):
    """Fetches countries, gets status, sorts, and prints/writes Markdown table."""

    slugs_to_process = []
    output_target = sys.stdout # Default to standard output
    output_filename = None

    # Determine output target
    if args.output:
        output_filename = args.output
        print(f"Output will be written to file: {output_filename}", file=sys.stderr)
    elif args.test:
        # Default output file for test mode if --output not specified
        output_filename = "TEST.md"
        print(f"Test mode active. Output will be written to default file: {output_filename}", file=sys.stderr)
    else:
         print(f"Output will be written to standard output.", file=sys.stderr)


    if args.test:
        print("🧪 Running in test mode with predefined slugs.", file=sys.stderr)
        slugs_to_process = TEST_SLUGS
    else:
        # Fetch full list if not in test mode
        print("Fetching full country list...", file=sys.stderr)
        root_data = fetch_json(BASE_URL)
        if root_data is None or 'links' not in root_data or 'children' not in root_data['links']:
            print("❌ Error: Could not fetch the main country list from API.", file=sys.stderr)
            sys.exit(1)
        all_countries_data = root_data['links']['children']
        print(f"Found {len(all_countries_data)} countries in API list. Extracting slugs...", file=sys.stderr)
        for i, country_link_data in enumerate(all_countries_data, start=1):
            slug = country_link_data.get('details', {}).get('country', {}).get('slug')
            if slug:
                slugs_to_process.append(slug)
            else:
                title = country_link_data.get('title', f'Unknown Entry {i}')
                print(f"⚠️ Skipping entry '{title}' due to missing slug.", file=sys.stderr)

    # Fetch data for selected slugs
    total_slugs = len(slugs_to_process)
    print(f"Fetching details for {total_slugs} countries...", file=sys.stderr)
    all_results = []
    for i, slug in enumerate(slugs_to_process, start=1):
        print(f"Fetching {i}/{total_slugs}: {slug}", file=sys.stderr)
        all_results.append(get_country_data(slug))

    # Sort results alphabetically
    all_results.sort(key=lambda x: x.get('country', ''))
    print(f"\nSorting complete.", file=sys.stderr)

    # Generate Markdown table
    markdown_rows = [
        "| Status | Country | FCDO Advice |",
        "|:------:|---------|-------------|"
    ]
    processed_count = 0
    error_count = 0
    print(f"Generating Markdown table for {len(all_results)} countries...", file=sys.stderr)
    for result in all_results:
        country_name = result.get('country', 'Unknown')
        slug = result.get('slug', '')
        link = f"https://www.gov.uk/foreign-travel-advice/{slug}" if slug else "#"

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
            emoji = get_traffic_light_status(alert_list) # Get emoji based on updated logic
            advice_text = translate_advice(alert_list, country_name)
            if emoji == '❓' and not advice_text.startswith("Unrecognized alerts") and not advice_text.startswith("Error:"):
                 advice_text = "Error: Could not determine status from alerts."
                 error_count += 1
            processed_count += 1

        markdown_rows.append(f"| {emoji} | [{country_name}]({link}) | {advice_text} |")

    print(f"\nProcessed {processed_count}/{len(all_results)} countries successfully. Encountered {error_count} errors/unknown statuses.", file=sys.stderr)

    # Write output
    final_markdown = "\n".join(markdown_rows)
    if output_filename:
        try:
            with open(output_filename, 'w', encoding='utf-8') as f:
                f.write(final_markdown)
            print(f"✅ Successfully wrote results to {output_filename}", file=sys.stderr)
        except IOError as e:
            print(f"❌ Error writing to file {output_filename}: {e}", file=sys.stderr)
            sys.exit(1) # Exit if file write fails
    else:
        # Print to standard output if no file specified
        print(final_markdown)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch FCDO travel advice and generate a Markdown table.")
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