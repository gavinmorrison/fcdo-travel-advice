# FCDO Travel Advice Status Monitor

This repository contains a Python script that automatically fetches and monitors travel advice from the UK Foreign, Commonwealth & Development Office (FCDO) API. The script generates a comprehensive table showing the current travel advisory status for all countries worldwide.

## 🚦 Status Legend

The script uses a traffic light system to categorize travel advice:

- 🔴 **Red**: FCDO advises against all travel to the whole country
- ⚠️ **Warning**: FCDO advises against all travel to parts of the country  
- 🟡 **Yellow**: FCDO advises against all but essential travel
- 🟢 **Green**: No specific travel advisories currently active
- ❓ **Unknown**: Error or unrecognized alert status

## 📊 Current Travel Advice Status

The table below is automatically updated daily at 2 AM UTC via GitHub Actions:

<!-- FCDO_TABLE_START -->
<!-- FCDO_TABLE_END -->

*Last updated: Automatically via GitHub Actions*

## 🛠️ Usage

### Prerequisites

- Python 3.7 or higher
- Internet connection for API access

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/fcdo-travel-advice.git
   cd fcdo-travel-advice
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Script

#### Basic Usage
```bash
# Output to console
python get_status.py

# Output to file
python get_status.py -o travel_advice.md
```

#### Test Mode
```bash
# Run with a small subset of countries for testing
python get_status.py --test
```

#### Command Line Options
```bash
python get_status.py --help
```

- `--test`: Run in test mode with predefined countries
- `-o, --output FILE`: Specify output file path
- `--version`: Show version information

## 🤖 Automation

This repository includes GitHub Actions workflows for automation:

### Daily Updates (`update_readme.yml`)
- Runs daily at 2 AM UTC
- Fetches latest travel advice data
- Updates the table in this README automatically
- Commits changes back to the repository

### Manual Testing (`test_run.yml`)
- Can be triggered manually from the Actions tab
- Runs the script in test mode for verification
- Useful for testing changes without affecting the main table

## 📁 Project Structure

```
fcdo-travel-advice/
├── .github/workflows/     # GitHub Actions workflows
│   ├── update_readme.yml  # Daily automated updates
│   └── test_run.yml       # Manual testing workflow
├── get_status.py          # Main Python script
├── requirements.txt       # Python dependencies
├── LICENSE               # MIT License
├── README.md             # This file (auto-updated)
└── .gitignore           # Git ignore rules
```

## 🔧 Technical Details

### Data Source
The script fetches data from the official FCDO API:
- Base URL: `https://www.gov.uk/api/content/foreign-travel-advice`
- Real-time data directly from government sources
- Comprehensive coverage of all countries and territories

### Processing Logic
1. Fetches the complete list of countries from the API
2. Retrieves detailed travel advice for each country
3. Categorizes advice using the traffic light system
4. Generates a sorted Markdown table
5. Handles errors gracefully with appropriate status indicators

### Error Handling
- Network timeouts and connection errors
- Invalid or missing API data
- Unrecognized alert statuses
- Comprehensive logging to stderr

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## ⚠️ Disclaimer

This tool is for informational purposes only. Always check the official FCDO website at [gov.uk/foreign-travel-advice](https://www.gov.uk/foreign-travel-advice) for the most current and detailed travel advice before making travel decisions.