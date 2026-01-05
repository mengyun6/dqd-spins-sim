"""Plotting utilities for visualization."""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from typing import Tuple


def plot_spin_expectations(
    time_points: np.ndarray,
    expectations: np.ndarray,
    output_path: Path,
    title: str = "Spin Expectation Values vs Time"
) -> None:
    """
    Plot the expectation values of Pauli operators as a function of time.
    
    Args:
        time_points: 1D array of time values
        expectations: Array of shape (N, 3) with columns [⟨σx⟩, ⟨σy⟩, ⟨σz⟩]
        output_path: Path where the plot should be saved
        title: Plot title
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    ax.plot(time_points, expectations[:, 0], label=r'$\langle \sigma_x \rangle$', linewidth=2)
    ax.plot(time_points, expectations[:, 1], label=r'$\langle \sigma_y \rangle$', linewidth=2)
    ax.plot(time_points, expectations[:, 2], label=r'$\langle \sigma_z \rangle$', linewidth=2)
    
    ax.set_xlabel('Time', fontsize=12)
    ax.set_ylabel('Expectation Value', fontsize=12)
    ax.set_title(title, fontsize=14)
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()

