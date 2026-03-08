#!/usr/bin/env python3
"""
=====================================================================
ME6990-02: S-10 TRUCK INPUT GEAR SET ANALYSIS
=====================================================================
Benchmark Analysis Report
Determines AGMA factors of safety using AGMA 2001-D04 standard
"""
import numpy as np
from math import pi, sin, cos, sqrt, tan, atan, log10

print("="*100)
print("S-10 TRUCK INPUT GEAR SET — AGMA ANALYSIS")
print("="*100 + "\n")

# =====================================================================
# SECTION 1: ENGINE & VEHICLE SPECIFICATIONS
# =====================================================================
print("SECTION 1: ENGINE PERFORMANCE & VEHICLE SPECIFICATIONS")
print("-"*100 + "\n")

Tq1 = 245 * 12  # Peak torque in lb·in
Nr1 = 2800      # Speed at peak torque
Hp1 = Tq1 * Nr1 / 63025
Nr2 = 4400      # Rated power speed
Hp2 = 180       # Rated power
Tq2 = Hp2 * 63025 / Nr2

print(f"Peak Torque: {Tq1} lb·in @ {Nr1} rpm")
print(f"Rated Power: {Hp2} hp @ {Nr2} rpm")
print(f"Torque at rated power: {Tq2:.0f} lb·in\n")

Weight = 3016       # Curb weight (lbf)
Pmax = 1185        # Maximum payload (lbf)
WB = 108.3         # Wheelbase (in)
Wtr = 0.43 * Weight  # Weight on rear tires
Rrr = 1.1292       # Rolling radius (ft)

print(f"Vehicle Weight: {Weight} lbf")
print(f"Maximum Payload: {Pmax} lbf")
print(f"Wheelbase: {WB} in\n")

# =====================================================================
# SECTION 2: GEAR SPECIFICATIONS
# =====================================================================
print("SECTION 2: GEAR GEOMETRY & SPECIFICATIONS")
print("-"*100 + "\n")

Np = 26              # Pinion teeth
Ng = 34              # Gear teeth
Pnd = 10.5           # Normal diametral pitch
psi = 23             # Helix angle (degrees)
phi_n = 20           # Normal pressure angle (degrees)

mG = Ng / Np
print(f"Pinion Teeth: {Np}")
print(f"Gear Teeth: {Ng}")
print(f"Gear Ratio: {mG:.4f}\n")

# Derived gear geometry
phi_t = np.degrees(np.arctan(np.tan(np.radians(phi_n)) / np.cos(np.radians(psi))))
Dp = Np / (Pnd * np.cos(np.radians(psi)))
Dg = Ng / (Pnd * np.cos(np.radians(psi)))
CD = (Dp + Dg) / 2
Dpo = Dp + 2 / Pnd
Dgo = Dg + 2 / Pnd
F = 1.0  # Face width (in)

print(f"Pitch Diameter (Pinion): {Dp:.4f} in")
print(f"Pitch Diameter (Gear): {Dg:.4f} in")
print(f"Center Distance: {CD:.4f} in")
print(f"Face Width: {F} in\n")

# Contact ratio
p = pi * Dp / Np
Rbp = (Dp/2) * np.cos(np.radians(phi_t))
Rbg = (Dg/2) * np.cos(np.radians(phi_t))

Z = sqrt((Dpo/2)**2 - Rbp**2) + sqrt((Dgo/2)**2 - Rbg**2) - CD * np.sin(np.radians(phi_t))
pb = 2 * pi * Rbp / Np
mF = F * np.tan(np.radians(psi)) / p
mp = Z / pb
CR = mF + mp

print(f"Face Contact Ratio (mF): {mF:.4f}")
print(f"Transverse Contact Ratio (mp): {mp:.4f}")
print(f"Total Contact Ratio (CR): {CR:.4f}")
print(f"Status: {'✓ PASS (CR > 2.0)' if CR > 2.0 else '✗ FAIL (CR < 2.0)'}\n")

# =====================================================================
# SECTION 3: AGMA FACTORS & CORRECTIONS
# =====================================================================
print("SECTION 3: AGMA CORRECTION FACTORS")
print("-"*100 + "\n")

# Material properties
Sac = 225000  # Allowable contact stress (psi) - carburized steel Rc 58
Sat = 65000   # Allowable bending stress (psi)

# Elastic and geometric factors
Cp = 2300     # Elastic coefficient (psi^0.5)
Ko = 1.00     # Overload factor

# Dynamic factor (Kv)
Av = 8
B = 0.25 * (12 - Av)**(2/3)
A = 50 + 56 * (1 - B)
Vt_5th = Nr1 * 2 * pi * Dp / 12 @ 3118  # Approximate operating point
Kv = ((A + sqrt(Vt_5th)) / A)**2

print(f"Allowable Contact Stress (Sac): {Sac:,} psi")
print(f"Allowable Bending Stress (Sat): {Sat:,} psi")
print(f"Dynamic Factor (Kv) @ 5th gear: {Kv:.4f}\n")

# Size and load distribution factors
Pd = Pnd * np.cos(np.radians(psi))
Ks = 1.192 * (F * sqrt(0.47 / Pd))**0.0535

Cpf = F / Dp
Cma = 0.0675 + 0.0128*F - 0.926e-4 * F**2
Km = 1.0 + 1.0 * (Cpf * 1.0 + Cma * 1.0)

print(f"Size Factor (Ks): {Ks:.4f}")
print(f"Load Distribution Factor (Km): {Km:.4f}\n")

# Geometry factors
mN = pb / (0.95 * Z)
I = sin(np.radians(phi_t)) * cos(np.radians(phi_t)) / (2 * mN) * mG / (mG + 1)
Jp = 0.470
Jg = 0.500

print(f"Pitting Geometry Factor (I): {I:.4f}")
print(f"Bending Factor (Pinion): {Jp}")
print(f"Bending Factor (Gear): {Jg}\n")

# =====================================================================
# SECTION 4: LOAD CASE ANALYSIS
# =====================================================================
print("SECTION 4: LOAD CASE ANALYSIS (4 Cases)")
print("-"*100 + "\n")

# Load Case 1: 5th gear highway speed
Tq_lc1 = 2868  # lb·in
Wt_lc1 = Tq_lc1 * 2 / Dp
cycles_lc1 = 28e6
Zn_lc1 = 0.948
Yn_lc1 = 0.960

# Load Case 2: 3rd gear
Tq_lc2 = 1046
Wt_lc2 = Tq_lc2 * 2 / Dp
cycles_lc2 = 2.8e6
Zn_lc2 = 1.000
Yn_lc2 = 1.000

# Load Case 3: Wheel slip
Tq_lc3 = 2831
Wt_lc3 = Tq_lc3 * 2 / Dp
cycles_lc3 = 7000
Zn_lc3 = 1.520
Yn_lc3 = 1.700

# Load Case 4: Clutch grab
Tq_lc4 = 3397
Wt_lc4 = Tq_lc4 * 2 / Dp
cycles_lc4 = 1000
Zn_lc4 = 1.520
Yn_lc4 = 1.700

load_cases = [
    ("5th Gear (28M cycles)", Wt_lc1, 3.752, Zn_lc1, Yn_lc1),
    ("3rd Gear (2.8M cycles)", Wt_lc2, 3.565, Zn_lc2, Yn_lc2),
    ("Wheel Slip (7K cycles)", Wt_lc3, 1.000, Zn_lc3, Yn_lc3),
    ("Clutch Grab (1K cycles)", Wt_lc4, 1.000, Zn_lc4, Yn_lc4)
]

print(f"{'Load Case':<25} {'Tq (lb·in)':<15} {'Wt (lbf)':<15} {'SH':<12} {'SF':<12}")
print("-"*80)

for name, Wt, Kv_case, Zn, Yn in load_cases:
    # Contact stress
    Sc = Cp * sqrt(Wt * Ko * Kv_case * Ks * (Km / (Dp * F * I)))
    SH = (Sac / Sc) * (Zn / 1.0)  # KR = 1.0
    
    # Bending stress
    St = Wt * Ko * Kv_case * Ks * (Pd / (F * Jp)) * (Km / 1.0)  # KB = 1.0
    SF = (Sat * Yn) / St
    
    status = "✓" if min(SH, SF) >= 1.0 else "✗"
    print(f"{name:<25} {Wt*Dp/2:<15.0f} {Wt:<15.0f} {SH:<12.3f} {SF:<12.3f} {status}")

print("\n✓ Analysis complete. See detailed load case results in reports.")
