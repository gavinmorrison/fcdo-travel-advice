# FCDO Travel Advice Status

This repository automatically tracks the UK Foreign, Commonwealth & Development Office (FCDO) travel advice status for all listed countries. The table below is updated daily via a GitHub Action.

## Traffic Light System

The status column uses a traffic light system based on the following rules:

*   🔴 **Red:** FCDO advises against **all travel** to at least one part of the country (applies if `avoid_all_travel_to_parts` or `avoid_all_travel_to_whole_country` is present).
*   🔴* **Red with Asterisk:** A combination of "avoid all travel" and "avoid all but essential travel" warnings exist for the country (both Red-level and Yellow-level alerts are present).
*   🟡 **Yellow:** FCDO advises against **all but essential travel** (applies if `avoid_all_but_essential_travel_to_parts` or `avoid_all_but_essential_travel_to_whole_country` is present), **and** no Red-level warnings are present.
*   🟢 **Green:** No FCDO travel warnings apply (the API returns an empty list for `alert_status`).
*   ❓ **Question Mark:** An error occurred fetching/processing data, the `alert_status` was missing or invalid, or contained unrecognized values.

Refer to the linked FCDO advice page for full details on any warnings.

---

## Travel Advice Table

<!-- FCDO_TABLE_START -->
*(Table content will be automatically inserted here by the daily GitHub Action)*
<!-- FCDO_TABLE_END -->

---

*Last updated: Automatically updated daily.*