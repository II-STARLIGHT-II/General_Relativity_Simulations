import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11  # Gravitational constant
M1 = 1.989e30  # Mass of black hole 1
M2 = 1.989e30  # Mass of black hole 2
c = 3.0e8  # Speed of light

# Initial conditions for circular orbit
r = np.array([1.496e11, 0.0])  # Distance between black holes
v = np.array([0.0, 30000])  # Initial circular velocity

# Function to calculate kinetic energy
def kinetic_energy(mass, velocity):
    return 0.5 * mass * np.linalg.norm(velocity)**2

# Function to calculate potential energy
def potential_energy(mass1, mass2, distance):
    return -G * mass1 * mass2 / np.linalg.norm(distance)

# Gravitational wave energy loss function (Peters formula)
def gravitational_wave_energy_loss(r, v):
    return (32/5) * G**4 * M1**2 * M2**2 * (M1 + M2) / (np.linalg.norm(r)**5 * c**5)

# Leapfrog Integration with Gravitational Wave Emission for Circular Binary
def leapfrog_circular_binary(r, v, total_time, dt):
    positions = []
    semi_major_axes = []
    energy_errors = []

    # Initial energy
    initial_kinetic = kinetic_energy(M1, v)
    initial_potential = potential_energy(M1, M2, r)
    initial_total_energy = initial_kinetic + initial_potential

    for t in range(0, total_time, dt):
        # Position update (half-step)
        r_half = r + 0.5 * v * dt
        # Acceleration due to gravity
        acceleration = -G * (M1 + M2) * r_half / np.linalg.norm(r_half)**3
        # Velocity update (full-step)
        v += acceleration * dt
        # Position update (full-step)
        r = r_half + 0.5 * v * dt
        positions.append(r)

        # Gravitational wave energy loss effect
        energy_loss = gravitational_wave_energy_loss(r, v)
        v *= (1 - energy_loss * dt)  # Reducing velocity due to energy loss

        # Energy calculations
        current_kinetic = kinetic_energy(M1, v)
        current_potential = potential_energy(M1, M2, r)
        current_total_energy = current_kinetic + current_potential
        energy_error = np.abs(current_total_energy - initial_total_energy) / np.abs(initial_total_energy)
        energy_errors.append(energy_error)

        # Semi-major axis (for circular orbit, r approximates the semi-major axis)
        semi_major_axes.append(np.linalg.norm(r))

    return np.array(positions), semi_major_axes, energy_errors

# Simulate for one year
total_time = 365 * 24 * 3600  # One year
dt = 60  # Time step in seconds
positions, semi_major_axes, energy_errors = leapfrog_circular_binary(r, v, total_time, dt)

# Plotting orbital trajectory
positions = np.array(positions)
plt.plot(positions[:, 0], positions[:, 1])
plt.xlabel('x position (m)')
plt.ylabel('y position (m)')
plt.title('Circular Binary Black Hole Orbit with Gravitational Wave Decay')
plt.show()

# Plotting semi-major axis decay
plt.plot(semi_major_axes)
plt.xlabel('Time Step')
plt.ylabel('Semi-Major Axis (m)')
plt.title('Semi-Major Axis Decay Over Time (Circular Binary)')
plt.show()

# Plotting energy error
plt.plot(energy_errors)
plt.xlabel('Time Step')
plt.ylabel('Energy Error')
plt.title('Energy Error Over Time (Circular Binary)')
plt.show()


