#!/bin/bash
# Setup script for dqd-spin-sim project
# This script creates a virtual environment and installs all dependencies

set -e  # Exit on error

echo "Setting up dqd-spin-sim environment..."

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "Error: python3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "Found Python $PYTHON_VERSION"

# Remove existing venv if it exists
if [ -d "venv" ]; then
    echo "Removing existing virtual environment..."
    rm -rf venv
fi

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment and upgrade pip
echo "Upgrading pip..."
source venv/bin/activate
pip install --upgrade pip

# Install dependencies
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

# Verify installation
echo ""
echo "Verifying installation..."
python -c "import numpy, scipy, matplotlib, yaml, pandas; print('✓ All dependencies installed successfully!')"

echo ""
echo "Setup complete! To activate the environment, run:"
echo "  source venv/bin/activate"
echo ""
echo "Then you can run the simulation:"
echo "  python -m src.run --config configs/v0_single_spin_precession.yml"

