# CLAUDE.md

Monitors FCDO travel advice via the GOV.UK API and generates a status table in README.md. A GitHub Actions workflow runs daily at 2 AM UTC.

## Commands

```bash
python3 get_status.py --test          # Quick test (6 countries → TEST.md)
python3 get_status.py -o results.md   # Full run (~230 countries)
python3 get_status.py                 # Full run to stdout
./test_workflow.sh                    # Simulate the CI workflow locally
```

## Key Conventions

- **stdout vs stderr**: stdout is reserved for markdown output (or file with `-o`). All progress/errors go to stderr.
- **Results sorted alphabetically** by country name after collection.
- **Update CHANGELOG.md** for all versioned changes.

## Traffic Light Priority

Countries can have multiple alerts. Highest severity wins, checked in this order:

1. `avoid_all_travel_to_whole_country` → 🔴 Red
2. `avoid_all_travel_to_parts` → ⚠️ Warning
3. `avoid_all_but_essential_travel_to_whole_country` or `_to_parts` → 🟡 Yellow
4. Empty alert list → 🟢 Green
5. Anything else → ❓ Unknown

If FCDO adds a new alert type, update `ADVICE_TEMPLATES`, `RED_ALERTS`/`YELLOW_ALERTS` sets, and the traffic light logic in `get_traffic_light_status()`.

## Workflow Gotchas

- README.md content is replaced between `<!-- FCDO_TABLE_START -->` and `<!-- FCDO_TABLE_END -->` markers. The workflow auto-adds markers if missing.
- `CHANGES.log` tracks status changes over time. It's excluded from `*.log` in `.gitignore` via a `!CHANGES.log` negation — don't remove that.
- The workflow uses `|| true` after the script run so that partial results can still be committed.
- Push retries with exponential backoff (5s, 10s) for transient network failures.
- Change detection compares old vs new table to generate informative commit messages and CHANGES.log entries.

## API

Base: `https://www.gov.uk/api/content/foreign-travel-advice`
Per-country: `https://www.gov.uk/api/content/foreign-travel-advice/{slug}`

No auth required. Sequential requests for all ~230 countries takes 2–3 minutes.
