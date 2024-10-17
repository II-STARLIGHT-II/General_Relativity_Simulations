import math
import numpy as np

# Constants
G = 1
Msun = 1.0
c = 63197.8  # Speed of light in code units (AU/day)

# PN acceleration function
def grav_accel_pn(r, v, M):
    r_norm = np.linalg.norm(r)
    v_norm = np.linalg.norm(v)
    
    # Newtonian term
    a_newtonian = -G * M / r_norm**3 * r
    
    # 1PN and 2PN corrections
    a_pn = ((2 + v_norm**2) * a_newtonian) - (4 * G * M / (c**2 * r_norm**2)) * r
    
    return a_newtonian + a_pn

# Leapfrog integrator with PN corrections
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

# Simulation duration
t_max = 88  # Mercury's orbital period
positions = []
a_mercury = grav_accel_pn(x_mercury, v_mercury, Msun)
dt = 0.01

time = 0
while time < t_max:
    x_mercury, v_mercury, a_mercury = leapfrog_pn(x_mercury, v_mercury, a_mercury, dt)
    positions.append(x_mercury)
    time += dt

# Plotting and analysis of precession will follow the same method as Week 5.

