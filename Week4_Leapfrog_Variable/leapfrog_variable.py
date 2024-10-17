import math
import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 1
Msun = 1.0  # Mass of the Sun
epsilon = 1e-10  # Small value to prevent division by zero

# Leapfrog with variable time-step
def leapfrog_variable(x, v, a, dt):
    v_half = v + 0.5 * a * dt  # Half step for velocity
    x_new = x + v_half * dt  # Update position
    a_new = grav_accel(x_new, Msun)  # Calculate new acceleration
    v_new = v_half + 0.5 * a_new * dt  # Full step velocity
    return x_new, v_new, a_new

# Gravitational acceleration
def grav_accel(r, M):
    r_norm = np.linalg.norm(r)
    if r_norm < epsilon:  # Prevent division by zero
        r_norm = epsilon
    return -G * M / r_norm**3 * r  # Gravitational acceleration formula

# Variable time-step function
def time_step(r, eta=0.01):
    return eta * math.sqrt(r**3 / G)

# Initial conditions for Mercury
x_mercury = np.array([0.387098, 0, 0])  # AU
v_mercury = np.array([0, 0.04787, 0])  # AU/day
M_mercury = Msun

# Simulation duration
t_max = 88  # One orbit of Mercury (days)
positions = []

# Initial acceleration and time step
a_mercury = grav_accel(x_mercury, M_mercury)
dt = time_step(np.linalg.norm(x_mercury))

time = 0
while time < t_max:
    x_mercury, v_mercury, a_mercury = leapfrog_variable(x_mercury, v_mercury, a_mercury, dt)
    positions.append(x_mercury)
    dt = time_step(np.linalg.norm(x_mercury))  # Recompute time-step based on current position
    time += dt

# Convert list to array for plotting
positions = np.array(positions)

# Plot Mercury’s orbit
plt.plot(positions[:, 0], positions[:, 1])
plt.xlabel('x [AU]')
plt.ylabel('y [AU]')
plt.title('Mercury Orbit with Variable Time-Step Leapfrog')
plt.show()
