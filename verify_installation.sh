#!/bin/bash
# Verification script to check if the environment is set up correctly

set -e

echo "Verifying installation..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Error: Virtual environment 'venv' not found."
    echo "   Please run 'bash setup.sh' first."
    exit 1
fi

# Activate virtual environment
source venv/bin/activate

# Check Python version
echo "✓ Python version: $(python --version)"

# Check if all required packages are installed
echo "Checking required packages..."
python -c "import numpy; print(f'  ✓ numpy {numpy.__version__}')" || { echo "  ❌ numpy not installed"; exit 1; }
python -c "import scipy; print(f'  ✓ scipy {scipy.__version__}')" || { echo "  ❌ scipy not installed"; exit 1; }
python -c "import matplotlib; print(f'  ✓ matplotlib {matplotlib.__version__}')" || { echo "  ❌ matplotlib not installed"; exit 1; }
python -c "import yaml; print(f'  ✓ pyyaml {yaml.__version__}')" || { echo "  ❌ pyyaml not installed"; exit 1; }
python -c "import pandas; print(f'  ✓ pandas {pandas.__version__}')" || { echo "  ❌ pandas not installed"; exit 1; }

# Check if the main module can be imported
echo "Checking module imports..."
python -c "from src.models.hamiltonians import single_spin_hamiltonian; print('  ✓ hamiltonians module')" || { echo "  ❌ Cannot import hamiltonians"; exit 1; }
python -c "from src.models.dynamics import simulate_time_evolution; print('  ✓ dynamics module')" || { echo "  ❌ Cannot import dynamics"; exit 1; }
python -c "from src.utils.io import generate_run_id; print('  ✓ io module')" || { echo "  ❌ Cannot import io"; exit 1; }
python -c "from src.utils.plotting import plot_spin_expectations; print('  ✓ plotting module')" || { echo "  ❌ Cannot import plotting"; exit 1; }

# Check if config file exists
if [ ! -f "configs/v0_single_spin_precession.yml" ]; then
    echo "  ❌ Config file not found"
    exit 1
else
    echo "  ✓ Config file exists"
fi

echo ""
echo "✅ All checks passed! Installation is complete."
echo ""
echo "You can now run the simulation:"
echo "  source venv/bin/activate"
echo "  python -m src.run --config configs/v0_single_spin_precession.yml"

