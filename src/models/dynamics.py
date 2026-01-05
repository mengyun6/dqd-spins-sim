"""Time evolution of quantum states."""

import numpy as np
from typing import Tuple, List
from scipy.linalg import expm


def initial_state_from_string(state_str: str) -> np.ndarray:
    """
    Create an initial state vector from a string specification.
    
    Supported states:
        - "up_x": |+x⟩ = (|0⟩ + |1⟩) / √2
        - "down_x": |-x⟩ = (|0⟩ - |1⟩) / √2
        - "up_y": |+y⟩ = (|0⟩ + i|1⟩) / √2
        - "down_y": |-y⟩ = (|0⟩ - i|1⟩) / √2
        - "up_z": |0⟩ (spin up along z)
        - "down_z": |1⟩ (spin down along z)
    
    Args:
        state_str: String specifying the initial state
        
    Returns:
        2-element complex numpy array representing the state vector
    """
    sqrt2_inv = 1.0 / np.sqrt(2.0)
    
    if state_str == "up_x":
        return np.array([sqrt2_inv, sqrt2_inv], dtype=complex)
    elif state_str == "down_x":
        return np.array([sqrt2_inv, -sqrt2_inv], dtype=complex)
    elif state_str == "up_y":
        return np.array([sqrt2_inv, 1j * sqrt2_inv], dtype=complex)
    elif state_str == "down_y":
        return np.array([sqrt2_inv, -1j * sqrt2_inv], dtype=complex)
    elif state_str == "up_z":
        return np.array([1.0, 0.0], dtype=complex)
    elif state_str == "down_z":
        return np.array([0.0, 1.0], dtype=complex)
    else:
        raise ValueError(f"Unknown initial state: {state_str}")


def evolve_state(state: np.ndarray, H: np.ndarray, dt: float) -> np.ndarray:
    """
    Evolve a quantum state forward in time by dt using the unitary evolution operator.
    
    U(t) = exp(-i * H * t)
    |ψ(t+dt)⟩ = U(dt) |ψ(t)⟩
    
    Args:
        state: Current state vector (2-element complex array)
        H: Hamiltonian (2x2 complex array)
        dt: Time step
        
    Returns:
        Evolved state vector
    """
    # Unitary evolution operator: U = exp(-i * H * dt)
    U = expm(-1j * H * dt)
    return U @ state


def compute_pauli_expectations(state: np.ndarray) -> Tuple[float, float, float]:
    """
    Compute expectation values of Pauli operators for a given state.
    
    <σi> = ⟨ψ|σi|ψ⟩
    
    Args:
        state: State vector (2-element complex array, assumed normalized)
        
    Returns:
        Tuple of (⟨σx⟩, ⟨σy⟩, ⟨σz⟩) as real floats
    """
    from .hamiltonians import pauli_matrices
    
    sigma_x, sigma_y, sigma_z = pauli_matrices()
    
    # <σi> = ⟨ψ|σi|ψ⟩ = state^dagger @ σi @ state
    state_dagger = np.conj(state)
    
    sx = np.real(state_dagger @ sigma_x @ state)
    sy = np.real(state_dagger @ sigma_y @ state)
    sz = np.real(state_dagger @ sigma_z @ state)
    
    return sx, sy, sz


def simulate_time_evolution(
    H: np.ndarray,
    initial_state: np.ndarray,
    total_time: float,
    dt: float,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Simulate the time evolution of a quantum state.
    
    Args:
        H: Hamiltonian (2x2 complex array)
        initial_state: Initial state vector (2-element complex array)
        total_time: Total simulation time
        dt: Time step
        
    Returns:
        Tuple of (time_points, expectations) where:
            time_points: 1D array of time values
            expectations: Array of shape (N, 3) with columns [⟨σx⟩, ⟨σy⟩, ⟨σz⟩]
    """
    num_steps = int(np.round(total_time / dt))
    time_points = np.linspace(0.0, total_time, num_steps + 1)
    
    expectations = np.zeros((num_steps + 1, 3))
    state = initial_state.copy()
    
    # Compute initial expectations
    sx, sy, sz = compute_pauli_expectations(state)
    expectations[0] = [sx, sy, sz]
    
    # Evolve state step by step
    for i in range(1, num_steps + 1):
        state = evolve_state(state, H, dt)
        sx, sy, sz = compute_pauli_expectations(state)
        expectations[i] = [sx, sy, sz]
    
    return time_points, expectations

