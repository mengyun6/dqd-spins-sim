# Project Overview: Numerical Simulation of Spin Dynamics in DQD

## Project Goal

This repository implements a numerical simulation framework for studying spin dynamics in double quantum dot (DQD) systems. The long-term goal is to model two-spin exchange-coupled systems with Zeeman field gradients, enabling the study of quantum gate operations and spin-based quantum information processing.

## Current Scope (v0)

**What v0 covers:**
- Single spin-1/2 particle under a static magnetic field
- Unitary time evolution (closed system, no decoherence)
- Larmor precession dynamics
- Expectation values of Pauli operators: ⟨σx⟩, ⟨σy⟩, ⟨σz⟩

**What is explicitly out of scope for v0:**
- Two-spin systems and exchange coupling
- Decoherence and open system dynamics (Lindblad master equation)
- Time-dependent control fields
- Multi-qubit gates

## Model & Equations

The v0 implementation uses the Hamiltonian:

```
H = (ω/2) * (n · σ)
```

where:
- `ω` is the Larmor frequency (angular frequency)
- `n` is a unit vector specifying the magnetic field direction
- `σ = (σx, σy, σz)` are the Pauli matrices

The state evolves according to the Schrödinger equation: `iℏ d|ψ⟩/dt = H|ψ⟩`, resulting in Larmor precession around the magnetic field axis.

## Assumptions

1. **Static magnetic field**: The magnetic field is constant in time (no time-dependent control)
2. **Closed system**: No coupling to environment, pure unitary evolution
3. **Single spin**: Only one spin-1/2 particle (no exchange coupling or multi-spin interactions)
4. **No decoherence**: No T1/T2 relaxation or dephasing processes

## Key Decisions

**Why start with single-spin precession:**
- Simplest non-trivial quantum dynamics
- Foundation for understanding two-spin systems
- Validates numerical methods before adding complexity
- Clear analytical solution for verification

**Why this output format:**
- **Plot (PNG)**: Visual verification of precession dynamics
- **Metrics (JSON)**: Machine-readable results for automated analysis
- **Config copy**: Ensures reproducibility and traceability

## Open Questions / Parking Lot

Items to revisit in future versions:

1. **Two-spin Hamiltonian**: Add exchange coupling term `J(σ₁·σ₂)` and Zeeman gradients
2. **Decoherence**: Implement Lindblad master equation with T1/T2 rates
3. **Time-dependent control**: Add pulse sequences for quantum gates (e.g., π/2 rotations)
4. **Optimization**: Parameter optimization for quantum control protocols
5. **Verification**: Compare numerical results with analytical solutions for known cases

## References

- Nielsen & Chuang, "Quantum Computation and Quantum Information" (Chapter 2: Introduction to Quantum Mechanics)
- Loss & DiVincenzo, "Quantum computation with quantum dots" (Phys. Rev. A 57, 120, 1998)
- Standard quantum mechanics textbooks on spin precession and Larmor frequency

