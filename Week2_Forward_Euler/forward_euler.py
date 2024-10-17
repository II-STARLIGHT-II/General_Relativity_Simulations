import math
import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 1  # Gravitational constant
Msun = 1.0  # Mass of Sun in solar masses
epsilon = 1e-10  # Small threshold to prevent division by zero

# Forward-Euler integration
def forward_euler(x, v, a, dt):
    x_new = x + v * dt  # Update position
    v_new = v + a * dt  # Update velocity
    return x_new, v_new

# Calculate gravitational acceleration
def grav_accel(r, M):
    r_norm = np.linalg.norm(r)  # Calculate the norm of the position vector
    if r_norm < epsilon:
        r_norm = epsilon  # Prevent division by zero by using a small value
    return -G * M / r_norm**3 * r  # Calculate acceleration

# Initial conditions for Earth (apocenter position)
x_earth = np.array([1, 0, 0])  # AU
v_earth = np.array([0, 0.017202, 0])  # AU/day
M_earth = Msun  # Earth-Sun system

# Time step and duration
dt = 0.01  # Step size in days
t_max = 365  # Simulate for one year
steps = int(t_max / dt)

# Store positions for plotting
positions = np.zeros((steps, 3))

for step in range(steps):
    r = np.linalg.norm(x_earth)
    a = grav_accel(x_earth, M_earth)  # Compute acceleration
    x_earth, v_earth = forward_euler(x_earth, v_earth, a, dt)  # Update position and velocity
    positions[step] = x_earth

# Plot Earth’s orbit
plt.plot(positions[:, 0], positions[:, 1])
plt.xlabel('x [AU]')
plt.ylabel('y [AU]')
plt.title('Earth Orbit using Forward-Euler')
plt.show()
