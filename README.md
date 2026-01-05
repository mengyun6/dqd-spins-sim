# Numerical Simulation of Spin Dynamics in DQD (Double Quantum Dot)

This repository provides a numerical simulation framework for studying spin dynamics in quantum dot systems. The current implementation focuses on a minimal model of single-spin Larmor precession under a static magnetic field, serving as a foundation for extending to two-spin exchange-coupled systems in double quantum dots.

## System Requirements

- Python 3.8 or higher
- pip (Python package installer)
- bash (for automated setup script on Unix-like systems)

## Quickstart

### Option 1: Automated Setup (Recommended)

Run the setup script to automatically create a virtual environment and install all dependencies:

```bash
bash setup.sh
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

**Verify installation (optional):**
```bash
bash verify_installation.sh
```

### Option 2: Manual Setup

1. **Create a virtual environment and install dependencies:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

### Run the Simulation

After setting up the environment, run the v0 demo:

```bash
python -m src.run --config configs/v0_single_spin_precession.yml
```

- `results/<run_id>/spin_expectation.png` - Plot of Pauli expectation values vs time
- `results/<run_id>/metrics.json` - Simulation metrics and final state
- `results/<run_id>/config_used.yml` - Copy of the configuration used

## Minimal Model

The v0 implementation simulates a single spin-1/2 particle under a static magnetic field. The Hamiltonian is:

```
H = (ω/2) * (n · σ)
```

where:
- `ω` is the Larmor frequency
- `n` is a unit vector specifying the magnetic field direction
- `σ = (σx, σy, σz)` are the Pauli matrices

The simulation computes the time evolution of the quantum state and outputs the expectation values `<σx>`, `<σy>`, and `<σz>` as functions of time. The state evolves according to the Schrödinger equation, resulting in Larmor precession around the magnetic field axis.

## Definition of Done (DoD)

A third party should be able to:
1. Clone this repository
2. Follow the Quickstart instructions above
3. Reproduce the plot and metrics within 30 minutes

The output is deterministic when a seed is fixed in the configuration file.

## Extension Plan (Future Work)

- **Two-spin model**: Add exchange coupling `J` and Zeeman field gradients for double quantum dot systems
- **Decoherence**: Implement Lindblad master equation for open system dynamics
- **Pulse sequences**: Add time-dependent control fields for quantum gate operations
- **Optimization**: Add parameter optimization routines for quantum control

## Project Structure

```
dqd-spin-sim/
├── README.md
├── requirements.txt           # Python dependencies
├── setup.sh                   # Automated setup script
├── verify_installation.sh     # Verification script
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── run.py              # Main CLI entry point
│   ├── models/
│   │   ├── __init__.py
│   │   ├── hamiltonians.py # Hamiltonian definitions
│   │   └── dynamics.py     # Time evolution
│   └── utils/
│       ├── __init__.py
│       ├── io.py           # I/O utilities
│       └── plotting.py     # Plotting utilities
├── configs/
│   └── v0_single_spin_precession.yml
├── results/
│   └── .gitkeep
└── notes/
    └── README.md
```

