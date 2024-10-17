import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11  # Gravitational constant
M_sun = 1.989e30  # Mass of the Sun
m_earth = 5.972e24  # Mass of Earth
dt = 60  # Fixed time-step (60 seconds)

# Initial conditions
r = np.array([1.496e11, 0.0])  # Initial position (1 AU)
v = np.array([0.0, 29.78e3])  # Initial velocity (Earth's orbital velocity)

def kinetic_energy(mass, velocity):
    return 0.5 * mass * np.linalg.norm(velocity)**2

def potential_energy(mass1, mass2, distance):
    return -G * mass1 * mass2 / np.linalg.norm(distance)

# Leapfrog Integration Function (Fixed time-step)
def leapfrog_fixed(r, v, dt, total_time):
    positions = []
    energy_errors = []

    # Initial energy
    initial_kinetic = kinetic_energy(m_earth, v)
    initial_potential = potential_energy(M_sun, m_earth, r)
    initial_total_energy = initial_kinetic + initial_potential

    for t in range(0, total_time, dt):
        # Position update (half-step)
        r_half = r + 0.5 * v * dt
        # Acceleration due to gravity
        acceleration = -G * M_sun * r_half / np.linalg.norm(r_half)**3
        # Velocity update (full-step)
        v += acceleration * dt
        # Position update (full-step)
        r = r_half + 0.5 * v * dt
        positions.append(r)

        # Energy calculations
        current_kinetic = kinetic_energy(m_earth, v)
        current_potential = potential_energy(M_sun, m_earth, r)
        current_total_energy = current_kinetic + current_potential
        energy_error = np.abs(current_total_energy - initial_total_energy) / np.abs(initial_total_energy)
        energy_errors.append(energy_error)

    return np.array(positions), energy_errors

# Simulate for one year
total_time = 365 * 24 * 3600
positions, energy_errors = leapfrog_fixed(r, v, dt, total_time)

# Plotting Earth's orbit
plt.plot(positions[:, 0], positions[:, 1])
plt.xlabel('x position (m)')
plt.ylabel('y position (m)')
plt.title('Earth’s Orbit (Fixed Time-Step)')
plt.show()

# Plotting energy error
plt.plot(energy_errors)
plt.xlabel('Time Step')
plt.ylabel('Energy Error')
plt.title('Energy Error Over Time (Fixed Time-Step)')
plt.show()

