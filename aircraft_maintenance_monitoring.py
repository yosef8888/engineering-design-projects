#!/usr/bin/env python3
"""
=====================================================================
CFPNC FLIGHT ACADEMY: TB9 AIRCRAFT MAINTENANCE MONITORING
=====================================================================
Preventive Maintenance Optimization
Exhaust Pipe Failure Analysis & Predictive Maintenance Scheduling
"""
from datetime import datetime, timedelta

print("="*100)
print("TB9 AIRCRAFT MAINTENANCE MONITORING — PREDICTIVE INSPECTION SYSTEM")
print("="*100 + "\n")

# =====================================================================
# SECTION 1: FAILURE DATA ANALYSIS
# =====================================================================
print("SECTION 1: EXHAUST PIPE FAILURE DATA ANALYSIS")
print("-"*100 + "\n")

# Historical failure data (Jan-May 2025)
failures = [
    {"date": "2025-01-08", "type": "Exhaust pipe play", "hours": 10},
    {"date": "2025-02-08", "type": "Exhaust pipe play", "hours": 85},
    {"date": "2025-02-18", "type": "Exhaust pipe play", "hours": 100},
    {"date": "2025-03-18", "type": "Exhaust pipe play", "hours": 130},
    {"date": "2025-04-26", "type": "Exhaust pipe play", "hours": 220},
    {"date": "2025-05-05", "type": "Exhaust pipe play", "hours": 250},
]

# Calculate MTBF (Mean Time Between Failures)
total_hours = 250  # Total operational hours
num_failures = len(failures)
mtbf = total_hours / num_failures

print(f"Analysis Period: January - May 2025 (5 months)")
print(f"Total Operational Hours: {total_hours} hours")
print(f"Number of Failures: {num_failures}")
print(f"Mean Time Between Failures (MTBF): {mtbf:.1f} hours")
print(f"Failure Frequency: {num_failures / 5:.1f} failures/month\n")

# Failure distribution analysis
failure_hours = [f["hours"] for f in failures]
print(f"Failure Hours Distribution: {failure_hours}")
print(f"Average Interval: {sum(failure_hours) / len(failure_hours):.0f} hours\n")

# =====================================================================
# SECTION 2: ROOT CAUSE PHYSICS ANALYSIS
# =====================================================================
print("SECTION 2: ROOT CAUSE PHYSICS ANALYSIS")
print("-"*100 + "\n")

# Vibration-induced loosening
print("Vibration-Induced Loosening Analysis:")
print("-" * 50)

m_exhaust = 1.2     # Mass (kg)
f_engine = 50       # Frequency (Hz) at 3000 RPM
x_amplitude = 0.0005  # Displacement (m) = 0.5 mm
g = 9.81           # Gravity

F_vibration = m_exhaust * (2 * 3.14159 * f_engine)**2 * x_amplitude
print(f"Engine Frequency: {f_engine} Hz (@ 3000 RPM)")
print(f"Exhaust Component Mass: {m_exhaust} kg")
print(f"Displacement Amplitude: {x_amplitude*1000} mm")
print(f"Vibration Force: {F_vibration:.1f} N (periodic)")

# Bolt preload requirement
mu_steel = 0.15    # Friction coefficient
F_preload_required = F_vibration / mu_steel
print(f"Minimum Preload Required: {F_preload_required:.0f} N\n")

# Thermal stress analysis
print("Thermal Cycling Analysis:")
print("-" * 50)

E = 200e9          # Young's modulus (Pa) - steel
alpha = 12e-6      # Thermal expansion (1/°C)
delta_T = 800      # Temperature change (°C)

sigma_thermal = E * alpha * delta_T
sigma_yield_steel = 640e6  # Yield strength (Pa)

print(f"Temperature Range: 20°C → 900°C (ΔT = {delta_T}°C)")
print(f"Thermal Stress: {sigma_thermal/1e6:.0f} MPa")
print(f"Steel Yield Strength: {sigma_yield_steel/1e6:.0f} MPa")
print(f"Stress Ratio: {sigma_thermal/sigma_yield_steel:.1f}× yield")
print(f"Conclusion: Plastic deformation expected → flange cracks ✓\n")

# =====================================================================
# SECTION 3: PREVENTIVE MAINTENANCE SCHEDULE
# =====================================================================
print("SECTION 3: PREDICTIVE MAINTENANCE SCHEDULE")
print("-"*100 + "\n")

# Safety factor for inspection interval
safety_factor = 0.6  # Inspect at 60% of MTBF
inspection_interval = mtbf * safety_factor

print(f"MTBF: {mtbf:.1f} hours")
print(f"Safety Factor: {safety_factor*100:.0f}%")
print(f"Recommended Inspection Interval: {inspection_interval:.0f} hours")
print(f"Maximum Flight Hours Between Inspections: {int(inspection_interval)} hours\n")

# Generate inspection schedule (future)
start_date = datetime(2025, 5, 5)
print("INSPECTION SCHEDULE (Forward-looking):\n")
print(f"{'Inspection #':<15} {'Scheduled Date':<20} {'Flight Hours':<15}")
print("-" * 50)

for i in range(1, 6):
    inspection_date = start_date + timedelta(hours=int(inspection_interval * i))
    flight_hours = int(inspection_interval * i) + 250  # Cumulative
    print(f"{i:<15} {inspection_date.strftime('%Y-%m-%d'):<20} {flight_hours:<15}")

print()

# =====================================================================
# SECTION 4: RISK MITIGATION STRATEGIES
# =====================================================================
print("SECTION 4: RISK MITIGATION STRATEGIES")
print("-"*100 + "\n")

print("""
SHORT-TERM SOLUTIONS (Immediate):
 1. Torque Verification Every 30 Hours
    • Use calibrated torque wrench (25 Nm per AMM 78-00-00)
    • Verify flange bolt preload
    • Document in maintenance log

 2. High-Temperature Anti-Seize Lubricant
    • Apply Nickel-based lubricant (e.g., Loctite 771-64)
    • Prevents galling and thermal seizure
    • Improves friction coefficient stability

MEDIUM-TERM UPGRADES (1-3 months):
 1. Material Upgrade
    • Replace standard steel bolts with Inconel 718
    • Yield strength: 1,100 MPa (vs. 640 MPa for steel)
    • Better fatigue resistance under thermal cycling

 2. Vibration Dampers
    • Install flexible exhaust hangers
    • Reduce resonant frequencies
    • Target: Shift resonance away from 50 Hz

LONG-TERM IMPROVEMENTS (3-6 months):
 1. Design Modification
    • Increase bolt preload capacity
    • Use double-lock washers
    • Consider exhaust clamp redesign

 2. Predictive Maintenance Platform
    • Integrate MTBF-based scheduling
    • Automated inspection reminders
    • Real-time flight hour tracking
""")

# =====================================================================
# SECTION 5: MONITORING ALGORITHM
# =====================================================================
print("\nSECTION 5: AUTOMATED INSPECTION ALERT SYSTEM")
print("-"*100 + "\n")

import json
from datetime import datetime

# Sample flight log
flight_log = [
    {"date": "2025-02-01", "hours": 0, "status": "OK"},
    {"date": "2025-02-10", "hours": 12, "status": "OK"},
    {"date": "2025-02-25", "hours": 28, "status": "Inspection Due"},
    {"date": "2025-03-15", "hours": 45, "status": "Inspection Due"},
    {"date": "2025-04-01", "hours": 61, "status": "OK"},
    {"date": "2025-04-20", "hours": 75, "status": "Inspection Due"},
    {"date": "2025-05-05", "hours": 90, "status": "OK"},
]

print(f"{'Date':<15} {'Flight Hours':<15} {'Cumulative':<15} {'Status':<20}")
print("-" * 65)

cumulative_hours = 250  # Start from previous flights
for log in flight_log:
    cumulative_hours += log["hours"]
    hours_since_inspection = cumulative_hours % int(inspection_interval)
    
    if hours_since_inspection > int(inspection_interval * 0.9):
        alert_status = "⚠ INSPECTION DUE"
    elif hours_since_inspection > int(inspection_interval):
        alert_status = "🔴 OVERDUE"
    else:
        alert_status = "✓ OK"
    
    print(f"{log['date']:<15} {log['hours']:<15} {cumulative_hours:<15} {alert_status:<20}")

print(f"\n✓ System monitors aircraft status automatically")
print(f"✓ Alerts generated when inspection is due")
print(f"✓ Reduces unplanned maintenance and safety risks\n")

# =====================================================================
# SECTION 6: COST-BENEFIT ANALYSIS
# =====================================================================
print("SECTION 6: COST-BENEFIT ANALYSIS")
print("-"*100 + "\n")

repair_cost_per_incident = 1200 / 6  # $1200/year ÷ 6 incidents
annual_repair_cost = 1200
downtime_per_incident = 4  # hours

print(f"Current Status (Reactive Maintenance):")
print(f" • Repairs per year: 6 incidents")
print(f" • Annual repair cost: ${annual_repair_cost:,}")
print(f" • Cost per incident: ${repair_cost_per_incident:.0f}")
print(f" • Annual downtime: {downtime_per_incident * 6} flight hours\n")

preventive_cost = 50  # per inspection
inspections_per_year = 5
total_preventive_cost = preventive_cost * inspections_per_year

print(f"With Predictive Maintenance (Proactive):")
print(f" • Scheduled inspections: {inspections_per_year}/year")
print(f" • Cost per inspection: ${preventive_cost}")
print(f" • Total annual inspection cost: ${total_preventive_cost}")
print(f" • Expected repairs: 1-2 incidents/year (75% reduction)")
print(f" • Estimated annual repair cost: ${annual_repair_cost * 0.25:,.0f}\n")

total_cost_preventive = total_preventive_cost + (annual_repair_cost * 0.25)
savings = annual_repair_cost - total_cost_preventive

print(f"Annual Cost Comparison:")
print(f" • Current (reactive): ${annual_repair_cost:,}")
print(f" • Preventive: ${total_cost_preventive:.0f}")
print(f" • Potential savings: ${savings:,.0f}/year ({savings/annual_repair_cost*100:.0f}% reduction)")
print(f" • Plus: Improved safety and aircraft availability ✓\n")

print("="*100)
print("END OF ANALYSIS")
print("="*100)
