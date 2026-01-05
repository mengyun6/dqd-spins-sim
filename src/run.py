"""Main CLI entry point for spin dynamics simulation."""

import argparse
import yaml
import numpy as np
from pathlib import Path
from typing import Dict, Any

from src.models.hamiltonians import single_spin_hamiltonian
from src.models.dynamics import initial_state_from_string, simulate_time_evolution
from src.utils.io import create_output_directory, save_config, save_metrics, generate_run_id
from src.utils.plotting import plot_spin_expectations


def load_config(config_path: str) -> Dict[str, Any]:
    """
    Load configuration from a YAML file.
    
    Args:
        config_path: Path to the configuration file
        
    Returns:
        Dictionary containing the configuration
    """
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    return config


def run_simulation(config: Dict[str, Any], run_id: str) -> None:
    """
    Run a single-spin precession simulation based on the provided configuration.
    
    Args:
        config: Configuration dictionary
        run_id: Unique identifier for this run
    """
    # Set random seed for reproducibility
    if 'seed' in config:
        np.random.seed(config['seed'])
    
    # Extract parameters
    omega = config['omega']
    axis = config['axis']
    total_time = config['total_time']
    dt = config['dt']
    initial_state_str = config['initial_state']
    output_dir_base = config.get('output_dir', 'results')
    
    # Create output directory
    output_dir = create_output_directory(output_dir_base, run_id)
    
    print(f"Running simulation with run_id: {run_id}")
    print(f"Output directory: {output_dir}")
    
    # Construct Hamiltonian
    H = single_spin_hamiltonian(omega, axis)
    print(f"Larmor frequency: {omega}")
    print(f"Magnetic field axis: {axis}")
    
    # Prepare initial state
    initial_state = initial_state_from_string(initial_state_str)
    print(f"Initial state: {initial_state_str}")
    
    # Run simulation
    print(f"Simulating from t=0 to t={total_time} with dt={dt}...")
    time_points, expectations = simulate_time_evolution(
        H, initial_state, total_time, dt
    )
    
    # Save plot
    plot_path = output_dir / "spin_expectation.png"
    plot_spin_expectations(time_points, expectations, plot_path)
    print(f"Saved plot to: {plot_path}")
    
    # Prepare metrics
    final_expectations = {
        'sx': float(expectations[-1, 0]),
        'sy': float(expectations[-1, 1]),
        'sz': float(expectations[-1, 2])
    }
    
    metrics = {
        'run_id': run_id,
        'config': config,
        'total_time': float(total_time),
        'dt': float(dt),
        'steps': len(time_points) - 1,
        'final_expectations': final_expectations
    }
    
    # Save metrics
    metrics_path = output_dir / "metrics.json"
    save_metrics(metrics, metrics_path)
    print(f"Saved metrics to: {metrics_path}")
    
    # Save config copy
    config_path = output_dir / "config_used.yml"
    save_config(config, config_path)
    print(f"Saved config copy to: {config_path}")
    
    print("Simulation completed successfully!")


def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description="Simulate spin dynamics in quantum dot systems"
    )
    parser.add_argument(
        '--config',
        type=str,
        required=True,
        help='Path to configuration YAML file'
    )
    parser.add_argument(
        '--run-id',
        type=str,
        default=None,
        help='Optional run identifier (default: auto-generated timestamp)'
    )
    
    args = parser.parse_args()
    
    # Load configuration
    config = load_config(args.config)
    
    # Generate or use provided run_id
    run_id = args.run_id if args.run_id else generate_run_id()
    
    # Run simulation
    run_simulation(config, run_id)


if __name__ == "__main__":
    main()

