#!/bin/bash

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip to latest version
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

echo "Setup complete! Virtual environment created and dependencies installed."
echo "To activate the environment in the future, run: source venv/bin/activate"