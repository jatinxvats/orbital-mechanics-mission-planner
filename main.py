from physics.orbit_visualization import animate_orbit

from physics.orbital_calculations import *

print("=== Orbital Mechanics Mission Planner ===")

altitude_km = float(input("Enter orbital altitude (km): "))

altitude_m = altitude_km * 1000

r = R + altitude_m

v = orbital_velocity(r)
ve = escape_velocity(r)
T = orbital_period(r)

print("\nResults")
print("--------------------------")
print(f"Orbital Radius: {r/1000:.2f} km")
print(f"Orbital Velocity: {v/1000:.2f} km/s")
print(f"Escape Velocity: {ve/1000:.2f} km/s")
print(f"Orbital Period: {T/60:.2f} minutes")

animate_orbit(r, T)