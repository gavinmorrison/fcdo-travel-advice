#!/bin/bash
# Test script to simulate the GitHub Actions workflow locally
# This helps verify that the workflow will work before pushing changes

set -e  # Exit on any error

echo "🧪 Testing FCDO Travel Advice workflow locally..."
echo "================================================"

# Check if Python is available
if ! command -v python &> /dev/null; then
    echo "❌ Python is not installed or not in PATH"
    exit 1
fi

echo "✅ Python found: $(python --version)"

# Check if requirements.txt exists
if [ ! -f "requirements.txt" ]; then
    echo "❌ requirements.txt not found"
    exit 1
fi

echo "✅ requirements.txt found"

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Run the script in test mode
echo "🚀 Running script in test mode..."
python get_status.py --test 2> test_stderr.log || true

# Check if TEST.md was created
if [ -f "TEST.md" ]; then
    echo "✅ TEST.md created successfully"
    echo "📄 First few lines of TEST.md:"
    head -n 5 TEST.md
else
    echo "❌ TEST.md was not created"
    if [ -s test_stderr.log ]; then
        echo "📋 Error log:"
        cat test_stderr.log
    fi
    exit 1
fi

# Check if there were any errors
if [ -s test_stderr.log ]; then
    echo "⚠️  Script produced some output to stderr:"
    cat test_stderr.log
fi

# Clean up
rm -f TEST.md test_stderr.log

echo "🎉 Local workflow test completed successfully!"
echo "The GitHub Actions workflow should work correctly."
