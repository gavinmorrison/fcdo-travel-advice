# CLAUDE.md - AI Assistant Guide

This document provides comprehensive information about the FCDO Travel Advice Status Monitor codebase for AI assistants to effectively understand and contribute to the project.

## Project Overview

**Purpose**: Automatically fetch and monitor travel advice from the UK Foreign, Commonwealth & Development Office (FCDO) API, generating a comprehensive table showing the current travel advisory status for all countries worldwide.

**Primary Language**: Python 3.7+
**License**: MIT
**Version**: 1.0.0
**Author**: Gavin Morrison

## Repository Structure

```
fcdo-travel-advice/
├── .github/
│   └── workflows/
│       ├── update_readme.yml    # Daily automated README updates (2 AM UTC)
│       └── test_run.yml         # Manual test workflow (workflow_dispatch)
├── .gitignore                   # Git ignore rules
├── CHANGELOG.md                 # Version history and changes
├── CHANGES.log                  # Auto-generated log of status changes
├── CLAUDE.md                    # This file - AI assistant guide
├── LICENSE                      # MIT License
├── README.md                    # User-facing documentation (auto-updated)
├── get_status.py                # Main Python script (293 lines)
├── requirements.txt             # Python dependencies (requests>=2.31.0)
└── test_workflow.sh             # Local testing script for workflows
```

## Core Architecture

### Data Flow

1. **Fetch Country List** → API call to `https://www.gov.uk/api/content/foreign-travel-advice`
2. **Extract Slugs** → Parse country slugs from API response
3. **Fetch Country Details** → API call per country: `{BASE_URL}/{slug}`
4. **Process Alerts** → Categorize using traffic light system
5. **Generate Markdown** → Create sorted table with status indicators
6. **Update README** → Replace content between `<!-- FCDO_TABLE_START -->` and `<!-- FCDO_TABLE_END -->` markers

### Key Components

#### get_status.py

**Main Functions**:
- `fetch_json(url)` - HTTP requests with 30s timeout, error handling
- `get_all_country_slugs(base_url)` - Fetches complete country list
- `get_country_data(slug)` - Fetches individual country details
- `fetch_all_country_data(slugs)` - Batch processes all countries
- `get_traffic_light_status(alert_list)` - Applies categorization rules
- `translate_advice(alert_list, country_name)` - Human-readable text
- `generate_markdown_table(results)` - Creates formatted table
- `write_output(content, filename)` - Writes to file or stdout

**Command Line Interface**:
```bash
python get_status.py                 # Output to stdout
python get_status.py -o FILE         # Output to file
python get_status.py --test          # Test mode (6 countries → TEST.md)
python get_status.py --version       # Show version
```

## Traffic Light System

### Status Categories

| Emoji | Status | Rule | Alert Types |
|-------|--------|------|-------------|
| 🔴 Red | Avoid all travel (whole country) | Has `avoid_all_travel_to_whole_country` | Highest priority |
| ⚠️ Warning | Avoid travel to parts | Has `avoid_all_travel_to_parts` BUT NOT whole country | Second priority |
| 🟡 Yellow | Avoid all but essential travel | Has any yellow alert, no red alerts | Third priority |
| 🟢 Green | No advisories | Empty alert list `[]` | Default safe |
| ❓ Unknown | Error or unrecognized | API errors or unknown alert types | Error state |

### Alert Processing Logic (lines 96-128)

**Priority Order** (checked in sequence):
1. If `avoid_all_travel_to_whole_country` → 🔴 Red
2. Elif `avoid_all_travel_to_parts` → ⚠️ Warning
3. Elif any yellow alert → 🟡 Yellow
4. Elif empty list → 🟢 Green
5. Else → ❓ Unknown

**Yellow Alerts**:
- `avoid_all_but_essential_travel_to_whole_country`
- `avoid_all_but_essential_travel_to_parts`

**Important**: A country can have multiple alerts (e.g., Azerbaijan has both red parts + yellow parts). The highest severity alert determines the status.

## GitHub Actions Workflows

### update_readme.yml - Production Workflow

**Triggers**:
- Scheduled: Daily at 2 AM UTC (`cron: '0 2 * * *'`)
- Manual: `workflow_dispatch`

**Permissions**: `contents: write` (required for commits)

**Steps**:
1. Checkout repository (`actions/checkout@v4`)
2. Set up Python 3.11 (`actions/setup-python@v5`)
3. Install dependencies from `requirements.txt`
4. Run script: `python get_status.py --output results.md`
5. Validate `results.md` exists and is not empty
6. Save old table for comparison (change detection)
7. Update README.md between markers using `awk`
8. Update "Last updated" line with actual date/time
9. Detect changes and generate summary (Python inline script)
10. Update CHANGES.log if status changes occurred
11. Commit with informative message and push
12. Retry push with exponential backoff (5s, 10s)

**Key Features**:
- Captures stderr to `script_stderr.log` for debugging
- Continues on script failure (`|| true`)
- Only commits if changes detected (`git diff --staged --quiet`)
- Uses bot identity for commits
- **Dynamic timestamp**: Updates "Last updated" with actual date/time (e.g., `2025-01-04 02:00 UTC`)
- **Change detection**: Compares old vs new table to identify status changes
- **Informative commits**: Messages like `Update FCDO travel advice: 2 worsened, 1 improved`
- **CHANGES.log**: Auto-generated changelog tracking status changes over time

**Change Detection Categories**:
- ⬆️ Worsened: Status became more severe (e.g., 🟡 → 🔴)
- ⬇️ Improved: Status became less severe (e.g., 🔴 → 🟡)
- ➕ Added: New country appeared in the list
- ➖ Removed: Country removed from the list

### test_run.yml - Testing Workflow

**Triggers**: Manual only (`workflow_dispatch`)

**Purpose**: Validate script functionality without committing

**Steps**:
1. Checkout and setup (same as production)
2. Run in test mode: `python get_status.py --test`
3. Validate `TEST.md` created successfully
4. Display snippet in workflow logs
5. No commits made

## Development Workflows

### Local Development

**Setup**:
```bash
git clone <repo-url>
cd fcdo-travel-advice
pip install -r requirements.txt
```

**Testing**:
```bash
# Quick test with 6 countries
python get_status.py --test

# Full run to stdout
python get_status.py

# Full run to file
python get_status.py -o output.md

# Test workflow simulation
./test_workflow.sh
```

### Making Changes

**When modifying get_status.py**:
1. Test locally first: `python get_status.py --test`
2. Verify output format and status logic
3. Check stderr output for warnings/errors
4. Run full test: `./test_workflow.sh`
5. Update version in `__version__` if releasing
6. Document changes in CHANGELOG.md

**When modifying workflows**:
1. Test locally if possible
2. Use `test_run.yml` for validation
3. Monitor Actions tab for errors
4. Check workflow logs for stderr output

## API Details

### Base Endpoint
```
https://www.gov.uk/api/content/foreign-travel-advice
```

### Country List Response
```json
{
  "links": {
    "children": [
      {
        "details": {
          "country": {
            "slug": "afghanistan"
          }
        },
        "title": "Afghanistan"
      }
    ]
  }
}
```

### Country Detail Endpoint
```
https://www.gov.uk/api/content/foreign-travel-advice/{slug}
```

### Country Detail Response
```json
{
  "details": {
    "country": {
      "name": "Afghanistan",
      "slug": "afghanistan"
    },
    "alert_status": [
      "avoid_all_travel_to_whole_country"
    ]
  }
}
```

## Code Conventions

### Error Handling
- All API calls wrapped in try-except
- Errors logged to stderr with context
- Failed countries marked with ❓ status
- Script continues on individual failures

### Logging Strategy
- **stderr**: Progress updates, errors, warnings
- **stdout**: Final markdown output (when no `-o` flag)
- **File**: Output when `-o` flag specified

### Data Processing
- All results sorted alphabetically by country name
- Sorting happens after data collection (line 266)
- Case-sensitive sorting based on API-provided names

### Test Data (TEST_SLUGS, lines 50-57)
```python
TEST_SLUGS = [
    "colombia",      # 🟡 Yellow
    "north-korea",   # 🟡 Yellow
    "turkey",        # ⚠️ Warning
    "azerbaijan",    # ⚠️ Warning (multiple alerts)
    "yemen",         # 🔴 Red
    "norway"         # 🟢 Green
]
```

## Common Tasks for AI Assistants

### Adding New Status Category

1. Update `get_traffic_light_status()` logic (lines 96-128)
2. Add emoji constant at module level
3. Update README.md status legend
4. Update this CLAUDE.md documentation
5. Add test case to TEST_SLUGS if possible

### Handling New Alert Types

1. Add to `ADVICE_TEMPLATES` dict (lines 42-47)
2. Add to RED_ALERTS or YELLOW_ALERTS sets if applicable
3. Update traffic light logic if needed
4. Test with affected country

### Debugging Workflow Failures

1. Check Actions tab → Failed workflow → Logs
2. Look for "Script stderr log" section
3. Check if `results.md` or `TEST.md` created
4. Verify API accessibility (rate limits, downtime)
5. Test locally: `./test_workflow.sh`

### Modifying README Update Logic

**Markers**: Content between `<!-- FCDO_TABLE_START -->` and `<!-- FCDO_TABLE_END -->`

**AWK Script** (update_readme.yml, lines 78-83):
- Reads `results.md` into memory
- Preserves content outside markers
- Replaces content between markers
- Handles missing markers gracefully

**Safety**:
- Markers auto-added if missing
- Original content preserved outside markers
- Only commits if changes detected

### Performance Optimization

**Current**: Sequential API calls for ~230 countries (~2-3 minutes)

**Potential Improvements**:
- Implement concurrent requests (asyncio/threading)
- Add caching layer with TTL
- Implement request pooling
- Add rate limiting protection

**Note**: Current approach is simple and reliable. Optimize only if performance becomes an issue.

## Troubleshooting

### Common Issues

**"results.md is empty or was not created"**
- API timeout or connection issue
- Check stderr log for network errors
- Verify API endpoint accessibility
- Check rate limiting

**"Unrecognized alerts" warning**
- New alert type added by FCDO
- Add to ADVICE_TEMPLATES
- Update traffic light logic if needed

**Git push failures in workflow**
- Transient network issue (auto-retries)
- Permission issues (check `contents: write`)
- Branch protection rules

**Missing markers in README**
- Workflow auto-adds markers
- Ensure at least one marker present initially
- Check AWK script logic

## Version History

See [CHANGELOG.md](CHANGELOG.md) for detailed version history.

**Current Version**: 1.0.0 (2025-06-14)

## Dependencies

**Runtime**:
- Python 3.7+
- requests>=2.31.0

**Development**:
- bash (for test_workflow.sh)
- git

**CI/CD**:
- GitHub Actions
- ubuntu-latest runner
- Python 3.11 in workflows

## Security Considerations

- No authentication required for FCDO API
- No sensitive data stored or processed
- Bot commits use GitHub-provided credentials
- Workflow runs in isolated runner environment
- Rate limiting handled gracefully by API

## Best Practices for AI Assistants

1. **Always test locally before suggesting workflow changes**
2. **Preserve existing error handling patterns**
3. **Log to stderr for debugging, stdout for output**
4. **Maintain alphabetical sorting of results**
5. **Keep traffic light logic simple and documented**
6. **Update CHANGELOG.md for all changes**
7. **Use `--test` mode for quick validation**
8. **Check stderr logs when debugging issues**
9. **Respect API rate limits and add delays if needed**
10. **Maintain backwards compatibility with existing data format**

## Quick Reference

**Test Locally**: `python get_status.py --test`
**Full Run**: `python get_status.py -o results.md`
**Workflow Test**: `./test_workflow.sh`
**View Logs**: GitHub Actions tab → Workflow run → Job logs
**API Docs**: https://www.gov.uk/api/content/foreign-travel-advice
**Status Legend**: See README.md "Status Legend" section

## Contact & Support

For issues or questions, create an issue in the GitHub repository with:
- Script version (`python get_status.py --version`)
- Error messages from stderr
- Steps to reproduce
- Expected vs actual behavior

---

*Last Updated: 2025-11-14*
*Document Version: 1.0.0*
*For: Claude and other AI assistants*
