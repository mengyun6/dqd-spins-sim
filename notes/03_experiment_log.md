# Experiment Log

Format: `Date → Config → Result → Next Step`

---

## 2025-01-05

### Run ID: 20260105_163243

**Config:**
```yaml
seed: 0
total_time: 10.0
dt: 0.01
omega: 1.0
axis: [0, 0, 1]
initial_state: "up_x"
output_dir: "results"
```

**Result:**
- ✅ Simulation completed successfully
- Plot shows Larmor precession: ⟨σx⟩ and ⟨σy⟩ oscillate, ⟨σz⟩ ≈ 0
- Precession period ≈ 2π/ω ≈ 6.28 time units (as expected)
- Final expectations: sx = -0.839, sy = -0.544, sz ≈ 0.0 (2.3e-17)
- Total steps: 1000 (10.0 / 0.01)

**Observations:**
- Precession dynamics match analytical solution
- Numerical integration stable with dt = 0.01
- Output format (PNG + JSON) works well for reproducibility

**Next Steps:**
1. [ ] Verify against analytical solution for different initial states
2. [ ] Test with different magnetic field directions (axis)
3. [ ] Check numerical accuracy by varying dt
4. [ ] Prepare for two-spin model implementation

---

## Template for Future Entries

### YYYY-MM-DD

### Run ID: YYYYMMDD_HHMMSS

**Config:**
```yaml
# Copy config here
```

**Result:**
- What happened
- Key observations
- Any errors or issues

**Observations:**
- Detailed notes
- Comparison with expectations
- Performance metrics

**Next Steps:**
- [ ] Action items
- [ ] Questions to investigate
- [ ] Planned modifications

---

## Planned Experiments

### Single-Spin Validation
- [ ] Test all initial states (up_x, down_x, up_y, down_y, up_z, down_z)
- [ ] Test different magnetic field directions (x, y, z, arbitrary)
- [ ] Verify precession frequency matches ω
- [ ] Check conservation of |⟨σ⟩| (should be constant for pure states)

### Numerical Accuracy
- [ ] Convergence test: vary dt from 0.1 to 0.001
- [ ] Compare with analytical solution: |ψ(t)⟩ = exp(-iHt)|ψ(0)⟩
- [ ] Check unitarity preservation (trace of density matrix)

### Parameter Sweeps
- [ ] Vary omega: 0.1, 0.5, 1.0, 2.0, 5.0
- [ ] Vary total_time: 1.0, 5.0, 10.0, 20.0
- [ ] Study effect on precession period and phase

### Future: Two-Spin Model
- [ ] Implement two-spin Hamiltonian with exchange J
- [ ] Test SWAP gate dynamics
- [ ] Study entanglement generation

### Future: Decoherence
- [ ] Add T1 relaxation (longitudinal)
- [ ] Add T2 dephasing (transverse)
- [ ] Compare with experimental T1/T2 times

---

## Key Findings Summary

(To be updated as experiments progress)

- **v0 Validation**: Single-spin precession works correctly
- **Numerical Stability**: dt = 0.01 sufficient for omega = 1.0
- **Reproducibility**: Deterministic output with fixed seed

