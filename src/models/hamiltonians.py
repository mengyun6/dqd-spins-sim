"""Hamiltonian definitions for spin systems."""

import numpy as np
from typing import List, Tuple


def pauli_matrices() -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Return the Pauli matrices σx, σy, σz.
    
    Returns:
        Tuple of (σx, σy, σz) as 2x2 numpy arrays
    """
    sigma_x = np.array([[0, 1], [1, 0]], dtype=complex)
    sigma_y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sigma_z = np.array([[1, 0], [0, -1]], dtype=complex)
    return sigma_x, sigma_y, sigma_z


def single_spin_hamiltonian(omega: float, axis: List[float]) -> np.ndarray:
    """
    Construct the Hamiltonian for a single spin-1/2 under a static magnetic field.
    
    H = (ω/2) * (n · σ)
    
    where:
        ω: Larmor frequency
        n: unit vector (axis) specifying the magnetic field direction
        σ: vector of Pauli matrices (σx, σy, σz)
    
    Args:
        omega: Larmor frequency (angular frequency)
        axis: Unit vector [nx, ny, nz] specifying the magnetic field direction
        
    Returns:
        2x2 complex numpy array representing the Hamiltonian
    """
    # Normalize the axis to ensure it's a unit vector
    axis = np.array(axis, dtype=float)
    axis = axis / np.linalg.norm(axis)
    
    sigma_x, sigma_y, sigma_z = pauli_matrices()
    
    # H = (ω/2) * (nx*σx + ny*σy + nz*σz)
    H = (omega / 2.0) * (axis[0] * sigma_x + axis[1] * sigma_y + axis[2] * sigma_z)
    
    return H


# Extension point for future: two-spin Hamiltonian
# def two_spin_hamiltonian(omega1, omega2, axis1, axis2, J, ...):
#     """Two-spin Hamiltonian with exchange coupling J."""
#     pass

