# Changelog

All notable changes to the FCDO Travel Advice Status Monitor will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-06-14

### Added
- 📄 **MIT License** - Added proper open source licensing
- 📋 **requirements.txt** - Proper dependency management for Python packages
- 📖 **Comprehensive README.md** - Detailed documentation with usage instructions, automation details, and project structure
- 🔧 **Version information** - Added `--version` command line argument
- 🧪 **Local testing script** - `test_workflow.sh` for testing GitHub Actions workflow locally
- 📝 **Enhanced documentation** - Added detailed docstrings and code comments
- 📊 **Changelog** - This file to track project changes

### Improved
- 🚀 **GitHub Actions workflows** - Updated to use requirements.txt for dependency management
- 🧹 **Code quality** - Removed unused variables and imports, improved error handling
- 📁 **Project structure** - Better organization with proper gitignore rules
- 🔍 **Error handling** - More robust error reporting and logging

### Removed
- 🗑️ **sample_results.csv** - Removed unnecessary test data file
- 🧹 **Temporary files** - Cleaned up test output files

### Fixed
- ✅ **GitHub Actions compatibility** - Workflows now properly install dependencies
- 🔧 **Code linting issues** - Resolved unused variable warnings
- 📦 **Dependency management** - Proper specification of required packages

### Technical Details
- **Script version**: 1.0.0
- **Python compatibility**: 3.7+
- **Dependencies**: requests>=2.31.0
- **License**: MIT
- **Automation**: Daily updates via GitHub Actions at 2 AM UTC

### Migration Notes
- No breaking changes from previous versions
- Existing functionality remains unchanged
- New features are additive and optional
