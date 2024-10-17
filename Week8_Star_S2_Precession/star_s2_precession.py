import math
import numpy as np

# Constants
G = 1
M_bh = 4.3e6  # Mass of the black hole in solar masses
c = 299792.458  # Speed of light in km/s

# PN acceleration function for S2 star
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
    a_new = grav_accel_pn(x_new, v_half, M_bh)
    v_new = v_half + 0.5 * a_new * dt
    return x_new, v_new, a_new

# Initial conditions for star S2
x_s2 = np.array([5.00176, 0, 0])  # mpc
v_s2 = np.array([0, 0.515, 0])  # mpc/year
M_s2 = M_bh

# Simulation parameters
t_max = 15  # Orbital period in years
positions = []
a_s2 = grav_accel_pn(x_s2, v_s2, M_s2)
dt = 0.01  # Time step in years

time = 0
while time < t_max:
    x_s2, v_s2, a_s2 = leapfrog_pn(x_s2, v_s2, a_s2, dt)
    positions.append(x_s2)
    time += dt

# Final position of S2 after simulation
print(f"Final position of S2: {x_s2}")

