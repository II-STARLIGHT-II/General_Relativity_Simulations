import numpy as np
import matplotlib.pyplot as plt

G = 6.67430e-11  # Gravitational constant
M_sun = 1.989e30  # Mass of the Sun
m_earth = 5.972e24  # Mass of Earth
dt = 60  # Fixed time-step in seconds

r = np.array([1.496e11, 0.0])  # Initial position (1 AU)
v = np.array([0.0, 29.78e3])  # Initial velocity (Earth's orbital velocity)

def leapfrog_fixed(r, v, dt, total_time):
    positions = []
    for t in range(0, total_time, dt):
        r_half = r + 0.5 * v * dt
        acceleration = -G * M_sun * r_half / np.linalg.norm(r_half) ** 3
        v += acceleration * dt
        r = r_half + 0.5 * v * dt
        positions.append(r)
    return positions

total_time = 365 * 24 * 3600  # Simulate for one year
positions = leapfrog_fixed(r, v, dt, total_time)

positions = np.array(positions)
plt.plot(positions[:, 0], positions[:, 1])
plt.xlabel('x position (m)')
plt.ylabel('y position (m)')
plt.title('Earth’s Orbit (Fixed Time-Step)')
plt.show()

