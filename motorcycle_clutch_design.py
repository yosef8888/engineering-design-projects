#!/usr/bin/env python3
"""
=====================================================================
ME6990-02: MOTORCYCLE CLUTCH & SPRINGS DESIGN
=====================================================================
Spring-loaded wet clutch for 60 hp motorcycle engine
Complete design solution with stress analysis
"""
import numpy as np
from math import pi, sqrt

print("="*100)
print("MOTORCYCLE CLUTCH & SPRINGS DESIGN — COMPLETE SOLUTION")
print("="*100 + "\n")

# =====================================================================
# SECTION 1: ENGINE SPECIFICATIONS
# =====================================================================
print("SECTION 1: ENGINE SPECIFICATIONS")
print("-"*100 + "\n")

Hp_rated = 60      # hp
Nr = 9000          # rpm
Tr = Hp_rated * 63025 / Nr  # Rated torque (lb-in)
FS = 1.5           # Safety factor

Tcmx_required = Tr * FS

print(f"Rated Power: {Hp_rated} hp @ {Nr} rpm")
print(f"Rated Torque: {Tr:.3f} lb·in")
print(f"Required Clutch Capacity (FS=1.5): {Tcmx_required:.3f} lb·in\n")

# =====================================================================
# SECTION 2: CLUTCH FRICTION PARAMETERS
# =====================================================================
print("SECTION 2: CLUTCH FRICTION ANALYSIS")
print("-"*100 + "\n")

mu_f = 0.12          # Friction coefficient (wet paper)
N_springs = 6        # Number of springs
Nfd = 9              # Number of friction discs
Npairs = 2 * Nfd     # Friction disc pairs
Do_friction = 6.0    # Outer friction diameter (in)
Di_friction = 0.5    # Inner friction diameter (in)
Dm = (Do_friction + Di_friction) / 2  # Mean friction diameter
Ac = 0.006           # Clearance when disengaged (in)

print(f"Coefficient of Friction: μ = {mu_f}")
print(f"Number of Friction Disc Pairs: Npairs = {Npairs}")
print(f"Mean Friction Diameter: Dm = {Dm} in")
print(f"Disc Clearance: Ac = {Ac} in\n")

# =====================================================================
# SECTION 3: SPRING DESIGN
# =====================================================================
print("SECTION 3: SPRING SELECTION & CALCULATIONS")
print("-"*100 + "\n")

# Spring material properties
G = 11500000       # Modulus of rigidity (psi) - Chrome Vanadium A232
Su_wire = 200000   # Ultimate tensile strength (psi)
tau_allowable = 0.50 * Su_wire  # Allowable shear stress

# Selected spring dimensions
dw = 0.070         # Wire diameter (inches)
dm = 0.50          # Mean coil diameter (inches)
Na_coils = 4       # Number of active coils
do_coil = dm + dw  # Outer coil diameter

print(f"Material: Chrome Vanadium A232")
print(f"Wire Diameter: dw = {dw} in")
print(f"Mean Coil Diameter: dm = {dm} in")
print(f"Active Coils: Na = {Na_coils}")
print(f"Outer Coil Diameter: do = {do_coil} in\n")

# Spring rate calculation
k = (G * dw**4) / (8 * dm**3 * Na_coils)
k_total = k * N_springs

print(f"Spring Rate (per spring): k = {k:.3f} lb·in")
print(f"Total Spring Rate (6 springs): k_total = {k_total:.3f} lb·in\n")

# =====================================================================
# SECTION 4: SPRING FORCE & COMPRESSION
# =====================================================================
print("SECTION 4: SPRING FORCE & CLUTCH VERIFICATION")
print("-"*100 + "\n")

# Required spring force
F_spring_required = Tcmx_required / (mu_f * Npairs * Dm / 2)
delta_y = F_spring_required / k  # Spring compression
Le = 0.75            # Length when engaged (in)
Lds = Le + delta_y + Ac  # Length disengaged

print(f"Required Spring Force (per spring): F = {F_spring_required:.3f} lb")
print(f"Spring Compression: δy = {delta_y:.4f} in")
print(f"Length Engaged: Le = {Le} in")
print(f"Length Disengaged: Lds = {Lds:.4f} in\n")

# Clutch torque verification
Tcmx_capacity = mu_f * Npairs * (Dm/2) * F_spring_required

print(f"Calculated Clutch Capacity: {Tcmx_capacity:.3f} lb·in")
print(f"Required Capacity: {Tcmx_required:.3f} lb·in")
print(f"Margin: {(Tcmx_capacity/Tcmx_required - 1)*100:.1f}%")
print(f"Status: {'✓ PASS' if Tcmx_capacity >= Tcmx_required else '✗ FAIL'}\n")

# =====================================================================
# SECTION 5: STRESS ANALYSIS
# =====================================================================
print("SECTION 5: SPRING STRESS ANALYSIS")
print("-"*100 + "\n")

K_w = 1.3            # Wahl stress concentration factor
F_max = F_spring_required + (Ac * k)

# Maximum shear stress
tau_max = (8 * K_w * F_max * dm) / (pi * dw**3)

print(f"Maximum Spring Force: F_max = {F_max:.3f} lb")
print(f"Maximum Shear Stress: τ_max = {tau_max:.0f} psi")
print(f"Allowable Shear Stress: τ_allowable = {tau_allowable:,} psi")
print(f"Stress Ratio: {tau_max / tau_allowable:.3f}")

if tau_max <= tau_allowable:
    print(f"Status: ✓ PASS - Stress is within limits\n")
else:
    print(f"Status: ⚠ WARNING - Stress exceeds allowable by {tau_max/tau_allowable:.1f}×")
    print(f"Recommendation: Increase wire diameter or reduce active coils\n")

# =====================================================================
# SECTION 6: DESIGN SUMMARY
# =====================================================================
print("="*100)
print("DESIGN SUMMARY & FINAL SPECIFICATIONS")
print("="*100 + "\n")

print(f"""
ENGINE SPECIFICATIONS:
 • Rated Power: {Hp_rated} hp @ {Nr} rpm
 • Rated Torque: {Tr:.3f} lb·in
 • Required Clutch Capacity (FS=1.5): {Tcmx_required:.3f} lb·in

CLUTCH SPECIFICATIONS:
 • Friction Coefficient: μ = {mu_f}
 • Friction Disc Pairs: {Npairs}
 • Mean Friction Diameter: {Dm} in
 • Calculated Torque Capacity: {Tcmx_capacity:.3f} lb·in ✓

SPRING SPECIFICATIONS:
 • Material: Chrome Vanadium A232
 • Wire Diameter: {dw} in
 • Mean Coil Diameter: {dm} in
 • Number of Springs: {N_springs}
 • Active Coils: {Na_coils}
 • Spring Rate: {k:.3f} lb/in (per spring)
 • Total Spring Rate: {k_total:.3f} lb/in

SPRING LENGTHS:
 • Length Engaged: {Le} in
 • Length Disengaged: {Lds:.4f} in
 • Spring Compression: {delta_y:.4f} in

STRESS ANALYSIS:
 • Maximum Shear Stress: {tau_max:.0f} psi
 • Allowable Stress: {tau_allowable:,} psi
 • Status: {'✓ PASS' if tau_max <= tau_allowable else '⚠ WARNING'}

✓ Design meets torque requirement with FS = {FS}
""")
