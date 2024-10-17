import math

# Constants
G = 1  # Gravitational constant in code units
Msun = 1.0  # Mass of Sun in solar masses
Mearth = 3.0024584e-6  # Mass of Earth in solar masses
Mmercury = 1.65956463e-7  # Mass of Mercury in solar masses

# Orbital parameters (semi-major axis and eccentricity)
a_earth = 1  # Semi-major axis of Earth's orbit in AU
e_earth = 0.0167  # Eccentricity of Earth's orbit
a_mercury = 0.387098  # Semi-major axis of Mercury's orbit in AU
e_mercury = 0.205635  # Eccentricity of Mercury's orbit

# Calculate pericenter and apocenter
def calc_orbit_params(a, e):
    rp = a * (1 - e)  # Pericenter
    ra = a * (1 + e)  # Apocenter
    return rp, ra

# Calculate velocity at pericenter and apocenter
def calc_velocity(a, e, Mstar):
    rp, ra = calc_orbit_params(a, e)
    vp = math.sqrt(G * Mstar * (1 + e) / rp)  # Velocity at pericenter
    va = math.sqrt(G * Mstar * (1 - e) / ra)  # Velocity at apocenter
    return vp, va

# Compute initial conditions for Earth and Mercury
def compute_initial_conditions(a, e, Mstar):
    rp, ra = calc_orbit_params(a, e)
    vp, va = calc_velocity(a, e, Mstar)
    return rp, ra, vp, va

# Earth
rp_earth, ra_earth, vp_earth, va_earth = compute_initial_conditions(a_earth, e_earth, Msun)
print(f"Earth: Pericenter: {rp_earth} AU, Apocenter: {ra_earth} AU, v_p: {vp_earth}, v_a: {va_earth}")

# Mercury
rp_mercury, ra_mercury, vp_mercury, va_mercury = compute_initial_conditions(a_mercury, e_mercury, Msun)
print(f"Mercury: Pericenter: {rp_mercury} AU, Apocenter: {ra_mercury} AU, v_p: {vp_mercury}, v_a: {va_mercury}")

