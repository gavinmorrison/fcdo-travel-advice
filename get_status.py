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

# --- New: Human-readable templates ---
ADVICE_TEMPLATES = {
    "avoid_all_travel_to_whole_country": "FCDO advises against all travel to {country_name}.",
    "avoid_all_travel_to_parts": "FCDO advises against all travel to parts of {country_name}.",
    "avoid_all_but_essential_travel_to_whole_country": "FCDO advises against all but essential travel to {country_name}.",
    "avoid_all_but_essential_travel_to_parts": "FCDO advises against all but essential travel to parts of {country_name}."
}
# --- End New ---

# Define test slugs - Expected results based on NEW rules
TEST_SLUGS = [
    "colombia",      # Expected: 🟡 Yellow
    "north-korea",   # Expected: 🟡 Yellow
    "turkey",        # Expected: 🔴 Red
    "azerbaijan",    # Expected: 🔴* Red*
    "yemen",         # Expected: 🔴 Red
    "norway"         # Expected: 🟢 Green
]

def fetch_json(url):
    """Fetches JSON data from a URL."""
    try:
        response = requests.get(url, timeout=30) # Add timeout
        response.raise_for_status() # Raises HTTPError for bad responses (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        # Log error to stderr for visibility in Actions logs
        print(f"Error fetching {url}: {e}", file=sys.stderr)
        return None # Return None to indicate failure

# --- New: Function to translate advice slugs ---
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

    # Combine known advice with line breaks
    output = "<br />".join(readable_advice)

    # Append any unknown alerts found
    if unknown_alerts:
        unknown_str = ", ".join(unknown_alerts)
        warning_msg = f"Unrecognized alerts: {unknown_str}"
        if output: # Add to existing known advice
             output += f"<br />({warning_msg})"
        else: # Only unknown alerts were found
             output = warning_msg
        print(f"Warning: Found unrecognized alert values for {country_name}: {unknown_alerts}", file=sys.stderr)

    return output
# --- End New ---


def get_traffic_light_status(alert_list):
    """
    Determines the traffic light emoji based on FCDO rules.
    Note: Raw status string generation is now handled by translate_advice.

    Args:
        alert_list: A list of alert status strings from the API.

    Returns:
        A string: the emoji status ('🔴', '🔴*', '🟡', '🟢', '❓')
    """
    # Rule 5: Handle unexpected input type (treat as error/unknown)
    if not isinstance(alert_list, list):
        print(f"Warning: Unexpected alert_list type: {type(alert_list)}. Assigning '❓'.", file=sys.stderr)
        return "❓" # Return only emoji

    current_alerts = set(alert_list)
    has_red = bool(current_alerts.intersection(RED_ALERTS))
    has_yellow = bool(current_alerts.intersection(YELLOW_ALERTS))

    # Apply rules in order of precedence
    if has_red:
        # Rule 2: Red with Asterisk*
        if has_yellow:
            emoji = "🔴*"
        # Rule 1: Red
        else:
            emoji = "🔴"
    elif has_yellow:
        # Rule 3: Yellow (only if no Red)
        emoji = "🟡"
    # Rule 4: Green (only if no Red or Yellow and list is empty)
    elif not alert_list:
         emoji = "🟢"
    # Rule 5: Question Mark (if list has content but none match Red/Yellow - covers unexpected API values)
    else:
        # Check if *any* alert exists that isn't known
        if any(alert not in ADVICE_TEMPLATES for alert in alert_list):
             emoji = "❓"
        else:
             # This case should ideally not happen if ADVICE_TEMPLATES is complete
             # but indicates valid list content didn't match Red/Yellow/Green rules.
             print(f"Warning: Alert list {alert_list} didn't match Red/Yellow/Green rules, but contains known values. Assigning '❓'.", file=sys.stderr)
             emoji = "❓"


    return emoji # Return only emoji

def get_country_data(slug):
    """Fetches and processes data for a single country."""
    url = f"{BASE_URL}/{slug}"
    data = fetch_json(url)

    # Handle fetch error (Rule 5 implicitly)
    if data is None:
        # Return structure consistent with success case for easier processing later
        return {"slug": slug, "country": slug.replace('-', ' ').title(), "alert_list": None, "error": "Failed to fetch API data"}

    try:
        details = data.get("details", {})
        country_name = details.get("country", {}).get("name", slug.replace('-', ' ').title())
        # Ensure alert_status exists and is a list (Rule 5 check)
        alert_list = details.get("alert_status")
        error_msg = None

        if alert_list is None:
             print(f"Warning: 'alert_status' key missing for {slug}. Treating as error.", file=sys.stderr)
             error_msg = "Missing 'alert_status' in API response"
             alert_list = None # Ensure alert_list is None on error
        elif not isinstance(alert_list, list):
             print(f"Warning: 'alert_status' is not a list for {slug} (type: {type(alert_list)}). Treating as error.", file=sys.stderr)
             error_msg = f"Invalid 'alert_status' type: {type(alert_list)}"
             alert_list = None # Ensure alert_list is None on error

        return {
            "country": country_name,
            "slug": slug,
            "alert_list": alert_list, # Will be None if error occurred here
            "error": error_msg
        }
    except Exception as e:
        # Catch potential errors during data extraction (Rule 5 implicitly)
        print(f"Error processing data for {slug}: {e}\nData: {json.dumps(data)}", file=sys.stderr)
        # Return structure consistent with success case
        return {"slug": slug, "country": slug.replace('-', ' ').title(), "alert_list": None, "error": f"Error processing API response: {str(e)}"}


def main(args): # Accept parsed arguments
    """Fetches countries, gets their status, sorts alphabetically, and prints a Markdown table."""

    slugs_to_process = []

    if args.test:
        print("🧪 Running in test mode with predefined slugs.", file=sys.stderr)
        slugs_to_process = TEST_SLUGS
    else:
        print("Fetching full country list...", file=sys.stderr)
        root_data = fetch_json(BASE_URL)
        if root_data is None or 'links' not in root_data or 'children' not in root_data['links']:
            print("❌ Error: Could not fetch the main country list from API.", file=sys.stderr)
            sys.exit(1)

        all_countries_data = root_data['links']['children']
        print(f"Found {len(all_countries_data)} countries in API list. Extracting slugs...", file=sys.stderr)

        # Extract slugs from the full list
        for i, country_link_data in enumerate(all_countries_data, start=1):
            slug = None
            try:
                # Simplified extraction assuming 'slug' is directly under 'details'->'country'
                slug = country_link_data.get('details', {}).get('country', {}).get('slug')
            except Exception as e:
                 print(f"Warning: Error extracting slug from entry {i}: {e}\nData: {json.dumps(country_link_data)}", file=sys.stderr)

            if slug:
                slugs_to_process.append(slug)
            else:
                title = country_link_data.get('title', f'Unknown Entry {i}')
                print(f"⚠️ Skipping entry '{title}' due to missing slug.", file=sys.stderr)

    # --- New: Fetch all country data first ---
    total_slugs = len(slugs_to_process)
    print(f"Fetching details for {total_slugs} countries...", file=sys.stderr)
    all_results = []
    for i, slug in enumerate(slugs_to_process, start=1):
        print(f"Fetching {i}/{total_slugs}: {slug}", file=sys.stderr)
        all_results.append(get_country_data(slug))
    # --- End New ---

    # --- New: Sort results alphabetically by country name ---
    # Handle potential None values or missing 'country' keys during sort
    all_results.sort(key=lambda x: x.get('country', ''))
    print(f"\nSorting complete.", file=sys.stderr)
    # --- End New ---


    # --- New: Generate Markdown table from sorted results ---
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
        link = f"https://www.gov.uk/foreign-travel-advice/{slug}" if slug else "#" # Fallback link

        # Handle errors first (Rule 5)
        if result.get("error"):
            emoji = "❓"
            advice_text = f"Error: {result['error']}"
            error_count += 1
        # Handle cases where alert_list is None due to processing error in get_country_data
        elif result.get("alert_list") is None:
             emoji = "❓"
             advice_text = "Error: Invalid or missing alert data during processing."
             error_count += 1
        else:
            # Get emoji and translate advice
            alert_list = result['alert_list']
            emoji = get_traffic_light_status(alert_list)
            advice_text = translate_advice(alert_list, country_name)
            if emoji == '❓' and not advice_text.startswith("Unrecognized alerts"):
                 # If emoji is '?', but translate_advice didn't set an error/unknown message,
                 # it means get_traffic_light_status found an issue.
                 advice_text = "Error: Could not determine status from alerts."
                 error_count += 1 # Count these as errors too
            processed_count += 1 # Count non-error results

        markdown_rows.append(f"| {emoji} | [{country_name}]({link}) | {advice_text} |")
    # --- End New ---

    print(f"\nProcessed {processed_count}/{len(all_results)} countries successfully. Encountered {error_count} errors/unknown statuses.", file=sys.stderr)
    # Print the final table to stdout
    print("\n".join(markdown_rows))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch FCDO travel advice and generate a Markdown table.")
    parser.add_argument(
        "--test",
        action="store_true",
        help="Run in test mode using a predefined list of country slugs."
    )
    parsed_args = parser.parse_args()
    main(parsed_args) # Pass parsed arguments to main