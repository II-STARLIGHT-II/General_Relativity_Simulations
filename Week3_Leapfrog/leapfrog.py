import math
import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 1
Msun = 1.0  # Mass of the Sun
epsilon = 1e-10  # Small value to prevent division by zero

# Leapfrog integrator
def leapfrog(x, v, a, dt):
    v_half = v + 0.5 * a * dt  # Half step for velocity
    x_new = x + v_half * dt  # Update position
    a_new = grav_accel(x_new, Msun)  # Calculate new acceleration
    v_new = v_half + 0.5 * a_new * dt  # Full step velocity
    return x_new, v_new, a_new

# Gravitational acceleration
def grav_accel(r, M):
    r_norm = np.linalg.norm(r)
    if r_norm < epsilon:  # Check to prevent division by zero
        r_norm = epsilon
    return -G * M / r_norm**3 * r

# Initial conditions for Earth (apocenter)
x_earth = np.array([1, 0, 0])  # AU
v_earth = np.array([0, 0.017202, 0])  # AU/day
M_earth = Msun

# Time step and simulation duration
dt = 0.01  # Step size in days
t_max = 365  # Simulate one year
steps = int(t_max / dt)

# Store positions for plotting
positions = np.zeros((steps, 3))

# Initial acceleration
a_earth = grav_accel(x_earth, M_earth)

for step in range(steps):
    x_earth, v_earth, a_earth = leapfrog(x_earth, v_earth, a_earth, dt)
    positions[step] = x_earth

# Plot Earth’s orbit
plt.plot(positions[:, 0], positions[:, 1])
plt.xlabel('x [AU]')
plt.ylabel('y [AU]')
plt.title('Earth Orbit using Leapfrog')
plt.show()
