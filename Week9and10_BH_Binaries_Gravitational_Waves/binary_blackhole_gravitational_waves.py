import math
import numpy as np

# Constants
G = 1
M1 = 8e6  # Mass of first black hole in solar masses
M2 = 8e3  # Mass of second black hole in solar masses
c = 299792.458  # Speed of light in km/s

# PN acceleration function including 2.5PN correction
def grav_accel_pn_2_5(r, v, M1, M2):
    r_norm = np.linalg.norm(r)
    v_norm = np.linalg.norm(v)
    
    # Newtonian term
    a_newtonian = -G * (M1 + M2) / r_norm**3 * r
    
    # 2.5PN correction (gravitational wave radiation)
    a_pn_2_5 = -((32 * G**3 * M1 * M2 * (M1 + M2)) / (5 * c**5 * r_norm**4)) * v
    
    return a_newtonian + a_pn_2_5

# Leapfrog with 2.5PN correction
def leapfrog_pn_2_5(x, v, a, dt):
    v_half = v + 0.5 * a * dt
    x_new = x + v_half * dt
    a_new = grav_accel_pn_2_5(x_new, v_half, M1, M2)
    v_new = v_half + 0.5 * a_new * dt
    return x_new, v_new, a_new

# Initial conditions for black hole binary
x_bh = np.array([0.2, 0, 0])  # mpc
v_bh = np.array([0, 0.01, 0])  # mpc/year

# Simulation parameters
t_max = 300  # Time in years
positions = []
a_bh = grav_accel_pn_2_5(x_bh, v_bh, M1, M2)
dt = 0.01  # Time step

time = 0
while time < t_max:
    x_bh, v_bh, a_bh = leapfrog_pn_2_5(x_bh, v_bh, a_bh, dt)
    positions.append(x_bh)
    time += dt

# Final binary separation after 300 years
print(f"Final position of black hole binary: {x_bh}")

