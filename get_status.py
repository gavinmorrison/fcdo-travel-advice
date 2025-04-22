import requests
import sys
import json # Import json for potential error details

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

def get_traffic_light_status(alert_list):
    """
    Determines the traffic light emoji and raw status string based on alert levels.

    Args:
        alert_list: A list of alert status strings from the API.

    Returns:
        A tuple: (emoji_string, raw_status_string)
    """
    if not isinstance(alert_list, list):
        # Handle unexpected data type
        print(f"Warning: Unexpected alert_list type: {type(alert_list)}. Treating as no alerts.", file=sys.stderr)
        alert_list = []

    current_alerts = set(alert_list)
    raw_status = ", ".join(alert_list) if alert_list else "No specific alerts"

    has_red = bool(current_alerts.intersection(RED_ALERTS))
    has_yellow = bool(current_alerts.intersection(YELLOW_ALERTS))

    emoji = "🟢" # Default Green
    if has_red:
        emoji = "🔴"
    elif has_yellow:
        emoji = "🟡"

    # Add asterisk if multiple severity levels are present
    if has_red and has_yellow:
        emoji += "*"
    # Could also add check for green + yellow/red if "No alert status" was ever mixed,
    # but based on sample data, it seems exclusive.

    return emoji, raw_status

def get_country_data(slug):
    """Fetches and processes data for a single country."""
    url = f"{BASE_URL}/{slug}"
    data = fetch_json(url)

    if data is None:
        return {"slug": slug, "error": "Failed to fetch API data"}

    try:
        details = data.get("details", {})
        country_name = details.get("country", {}).get("name", slug.replace('-', ' ').title())
        alert_list = details.get("alert_status", []) # Expecting a list

        return {
            "country": country_name,
            "slug": slug,
            "alert_list": alert_list,
            "error": None
        }
    except Exception as e:
        # Catch potential errors during data extraction
        print(f"Error processing data for {slug}: {e}\nData: {json.dumps(data)}", file=sys.stderr)
        return {"slug": slug, "error": f"Error processing API response: {str(e)}"}


def main():
    """Fetches all countries, gets their status, and prints a Markdown table."""
    print("Fetching country list...", file=sys.stderr)
    root_data = fetch_json(BASE_URL)
    if root_data is None or 'links' not in root_data or 'children' not in root_data['links']:
        print("❌ Error: Could not fetch the main country list from API.", file=sys.stderr)
        sys.exit(1)

    countries = root_data['links']['children']
    total = len(countries)
    print(f"Found {total} countries. Fetching details...", file=sys.stderr)

    markdown_rows = [
        "| Status | Country | FCDO Advice |",
        "|:------:|---------|-------------|"
    ]

    processed_count = 0
    for i, country_link_data in enumerate(countries, start=1):
        # Extract slug safely
        slug = None
        try:
            # Navigate the structure carefully
            if isinstance(country_link_data, dict) and \
               'details' in country_link_data and \
               isinstance(country_link_data['details'], dict) and \
               'country' in country_link_data['details'] and \
               isinstance(country_link_data['details']['country'], dict):
                slug = country_link_data['details']['country'].get('slug')
        except Exception as e:
             print(f"Warning: Error extracting slug from entry {i}: {e}\nData: {json.dumps(country_link_data)}", file=sys.stderr)


        if not slug:
            title = country_link_data.get('title', f'Unknown Entry {i}')
            print(f"⚠️ Skipping entry {i}/{total} ('{title}') due to missing slug.", file=sys.stderr)
            markdown_rows.append(f"| ❓ | {title} | Error: Missing slug in API list |")
            continue # Skip to the next country

        print(f"Processing {i}/{total}: {slug}", file=sys.stderr)
        result = get_country_data(slug)

        if result.get("error"):
            country_name = slug.replace('-', ' ').title()
            markdown_rows.append(f"| ❓ | {country_name} | Error: {result['error']} |")
        else:
            emoji, raw_status = get_traffic_light_status(result['alert_list'])
            country_name = result['country']
            link = f"https://www.gov.uk/foreign-travel-advice/{result['slug']}"
            markdown_rows.append(f"| {emoji} | [{country_name}]({link}) | {raw_status} |")
            processed_count += 1
        # Removed time.sleep for faster execution in Actions

    print(f"\nProcessed {processed_count}/{total} countries.", file=sys.stderr)
    # Print the final table to stdout
    print("\n".join(markdown_rows))

if __name__ == "__main__":
    main()