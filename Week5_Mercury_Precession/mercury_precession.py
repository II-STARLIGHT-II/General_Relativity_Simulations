import math
import numpy as np

# Constants
G = 1
Msun = 1.0  # Mass of the Sun
c = 63197.8  # Speed of light in code units (AU/day)

# Gravitational acceleration with Newtonian force
def grav_accel(r, M):
    return -G * M / r**3 * r

# Leapfrog with variable time-step
def leapfrog_variable(x, v, a, dt):
    v_half = v + 0.5 * a * dt
    x_new = x + v_half * dt
    a_new = grav_accel(x_new, Msun)
    v_new = v_half + 0.5 * a_new * dt
    return x_new, v_new, a_new

# Time-step function
def time_step(r, eta=0.01):
    return eta * math.sqrt(r**3 / G)

# Compute eccentricity vector
def compute_eccentricity(r, v):
    h = np.cross(r, v)
    e_vec = (np.cross(v, h) / G) - (r / np.linalg.norm(r))
    return e_vec

# Initial conditions for Mercury
x_mercury = np.array([0.387098, 0, 0])  # AU
v_mercury = np.array([0, 0.04787, 0])  # AU/day
M_mercury = Msun

# Simulation duration and setup
t_max = 88  # One orbit of Mercury in days
positions = []
eccentricities = []

a_mercury = grav_accel(x_mercury, M_mercury)
dt = time_step(np.linalg.norm(x_mercury))

time = 0
while time < t_max:
    x_mercury, v_mercury, a_mercury = leapfrog_variable(x_mercury, v_mercury, a_mercury, dt)
    ecc_vector = compute_eccentricity(x_mercury, v_mercury)
    eccentricities.append(np.linalg.norm(ecc_vector))
    positions.append(x_mercury)
    dt = time_step(np.linalg.norm(x_mercury))
    time += dt

# Final eccentricity
ecc_start = eccentricities[0]
ecc_end = eccentricities[-1]
print(f"Initial Eccentricity: {ecc_start}, Final Eccentricity: {ecc_end}")

# Output precession
phi_start = math.atan2(x_mercury[1], x_mercury[0])
phi_end = math.atan2(positions[-1][1], positions[-1][0])
precession = phi_end - phi_start
precession_arcsec = precession * 206264.806  # Convert to arcseconds
print(f"Precession: {precession_arcsec} arcseconds per orbit")

