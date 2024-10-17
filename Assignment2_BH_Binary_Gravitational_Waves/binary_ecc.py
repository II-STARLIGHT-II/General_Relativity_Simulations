import numpy as np
import matplotlib.pyplot as plt

G = 6.67430e-11  # Gravitational constant
M1 = 1.989e30  # Mass of black hole 1 (in kg)
M2 = 1.989e30  # Mass of black hole 2 (in kg)

# Initial conditions
r = np.array([1.5e11, 0.0])  # Initial distance between black holes
v = np.array([0.0, 30000.0])  # Initial velocity (m/s)

def leapfrog_eccentric_binary(r, v, total_time, dt):
    positions = []
    for t in range(0, total_time, dt):
        r_half = r + 0.5 * v * dt
        acceleration = -G * (M1 + M2) * r_half / np.linalg.norm(r_half) ** 3
        v += acceleration * dt
        r = r_half + 0.5 * v * dt
        positions.append(r)
    return positions

total_time = 365 * 24 * 3600  # 1 year in seconds
dt = 60  # time-step in seconds
positions = leapfrog_eccentric_binary(r, v, total_time, dt)

positions = np.array(positions)
plt.plot(positions[:, 0], positions[:, 1])
plt.xlabel('x position (m)')
plt.ylabel('y position (m)')
plt.title('Eccentric Binary Black Hole Orbit')
plt.show()


