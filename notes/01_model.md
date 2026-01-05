# Model: Single Spin-1/2 Larmor Precession

## Hamiltonian

The system is described by the Hamiltonian:

```
H = (ω/2) * (n · σ)
```

Expanding the dot product:

```
H = (ω/2) * (nx·σx + ny·σy + nz·σz)
```

where:
- `ω` (omega): Larmor frequency [rad/s] - determines the precession rate
- `n = [nx, ny, nz]`: Unit vector specifying the magnetic field direction (normalized to |n| = 1)
- `σ = [σx, σy, σz]`: Vector of Pauli matrices

## Pauli Matrices

```
σx = [0  1]    σy = [0  -i]    σz = [1   0]
     [1  0]         [i   0]         [0  -1]
```

## Time Evolution

The state evolves according to the Schrödinger equation:

```
iℏ d|ψ(t)⟩/dt = H|ψ(t)⟩
```

For a time-independent Hamiltonian, the solution is:

```
|ψ(t)⟩ = U(t)|ψ(0)⟩
```

where the unitary evolution operator is:

```
U(t) = exp(-i H t / ℏ)
```

In our implementation, we set ℏ = 1 (natural units), so:

```
U(t) = exp(-i H t)
```

## Expectation Values

The observables we compute are the expectation values of Pauli operators:

```
⟨σi⟩(t) = ⟨ψ(t)|σi|ψ(t)⟩
```

These represent the components of the Bloch vector, which precesses around the magnetic field axis.

## Parameters in Configuration

### `omega` (ω)
- **Type**: float
- **Units**: rad/s (angular frequency)
- **Meaning**: Larmor frequency, determines how fast the spin precesses
- **Example**: `omega: 1.0` means one full precession per 2π time units

### `axis` (n)
- **Type**: list of 3 floats [nx, ny, nz]
- **Units**: dimensionless (unit vector)
- **Meaning**: Direction of the static magnetic field
- **Example**: `axis: [0, 0, 1]` means field along z-axis
- **Note**: Automatically normalized in the code

### `initial_state`
- **Type**: string
- **Options**: 
  - `"up_x"`: |+x⟩ = (|0⟩ + |1⟩)/√2
  - `"down_x"`: |-x⟩ = (|0⟩ - |1⟩)/√2
  - `"up_y"`: |+y⟩ = (|0⟩ + i|1⟩)/√2
  - `"down_y"`: |-y⟩ = (|0⟩ - i|1⟩)/√2
  - `"up_z"`: |0⟩ (spin up along z)
  - `"down_z"`: |1⟩ (spin down along z)
- **Meaning**: Initial quantum state of the spin

### `total_time`
- **Type**: float
- **Units**: time (same units as 1/omega)
- **Meaning**: Total simulation time
- **Example**: `total_time: 10.0` with `omega: 1.0` means ~1.59 precession periods

### `dt`
- **Type**: float
- **Units**: time
- **Meaning**: Time step for numerical integration
- **Note**: Should be much smaller than 1/omega for accuracy
- **Example**: `dt: 0.01` with `omega: 1.0` means ~628 steps per precession period

### `seed`
- **Type**: integer
- **Meaning**: Random seed for reproducibility (currently not used in v0, but reserved for future stochastic processes)

## Physical Interpretation

When `axis: [0, 0, 1]` and `initial_state: "up_x"`:
- The magnetic field points along the z-axis
- The spin starts pointing along the x-axis
- The spin precesses in the xy-plane around the z-axis
- ⟨σz⟩ remains constant (0), while ⟨σx⟩ and ⟨σy⟩ oscillate with frequency ω

## Future Extensions

### Two-Spin Model (Planned)
```
H = (ω₁/2)(n₁·σ₁) + (ω₂/2)(n₂·σ₂) + J(σ₁·σ₂)
```
- `J`: Exchange coupling strength
- `ω₁, ω₂`: Individual Larmor frequencies
- `n₁, n₂`: Field directions for each spin

### Decoherence (Planned)
Add Lindblad operators for:
- T1 relaxation (energy dissipation)
- T2 dephasing (phase decoherence)

