#!/bin/bash

# ------------------------------
# Script Name: run_selenium_test.sh
# Description: Sets up the environment and runs the Selenium test script.
# Usage: ./run_selenium_test.sh
# ------------------------------

# Exit immediately if a command exits with a non-zero status
set -e

# Variables
SCRIPT_PATH="/Users/tallevi/PycharmProjects/DevOps1909/selenium_test.py"
VENV_PATH="/Users/tallevi/PycharmProjects/DevOps1909/venv"

# Function to check if a command exists
command_exists () {
    command -v "$1" >/dev/null 2>&1
}

# 1. Activate Virtual Environment (if exists)
if [ -d "$VENV_PATH" ]; then
    echo "✅ Activating virtual environment at $VENV_PATH"
    source "$VENV_PATH/bin/activate"
else
    echo "⚠️ Virtual environment not found at $VENV_PATH. Proceeding without it."
fi

# 2. Check if Selenium is installed, install if not
echo "🔍 Checking if Selenium is installed..."
if python3 -c "import selenium" >/dev/null 2>&1; then
    echo "✅ Selenium is already installed."
else
    echo "⚠️ Selenium is not installed. Installing now..."
    pip3 install selenium
    echo "✅ Selenium installation complete."
fi

# 3. Run the Selenium Test Script
echo "🚀 Running Selenium test script: $SCRIPT_PATH"
python3 "$SCRIPT_PATH"
echo "✅ Selenium test script executed successfully."

# 4. Deactivate Virtual Environment (if activated)
if [ -d "$VENV_PATH" ]; then
    echo "🔄 Deactivating virtual environment."
    deactivate
fi

exit 0

