import math
import numpy as np

# Constants
G = 1
Msun = 1.0
c = 63197.8  # Speed of light in code units (AU/day)

# Post-Newtonian correction to acceleration (up to 1PN order)
def grav_accel_pn(r, v, M):
    r_norm = np.linalg.norm(r)
    v_norm = np.linalg.norm(v)
    
    # Newtonian term
    a_newtonian = -G * M / r_norm**3 * r
    
    # 1PN correction
    a_pn = ((2 + np.linalg.norm(v)**2) * a_newtonian) - (4 * G * M / (c**2 * r_norm**2)) * r
    
    return a_newtonian + a_pn

# Leapfrog with PN correction
def leapfrog_pn(x, v, a, dt):
    v_half = v + 0.5 * a * dt
    x_new = x + v_half * dt
    a_new = grav_accel_pn(x_new, v_half, Msun)
    v_new = v_half + 0.5 * a_new * dt
    return x_new, v_new, a_new

# Initial conditions for Mercury
x_mercury = np.array([0.387098, 0, 0])  # AU
v_mercury = np.array([0, 0.04787, 0])  # AU/day
M_mercury = Msun

# Simulation parameters
t_max = 88  # One orbit of Mercury (days)
positions = []
a_mercury = grav_accel_pn(x_mercury, v_mercury, M_mercury)
dt = 0.01  # Constant time step

time = 0
while time < t_max:
    x_mercury, v_mercury, a_mercury = leapfrog_pn(x_mercury, v_mercury, a_mercury, dt)
    positions.append(x_mercury)
    time += dt

# Output Mercury's final position after applying PN corrections
print(f"Final position of Mercury: {x_mercury}")

