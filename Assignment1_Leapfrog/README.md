# Assignment 1: Numerical Integration with Leapfrog Algorithm

This assignment involves writing a numerical integrator using the Leapfrog algorithm with both fixed and variable time-steps. The project focuses on the integration of the Earth-Sun and Mercury-Sun systems, along with analyzing energy conservation and convergence.

## Features
- Leapfrog integration with both fixed and variable time-steps.
- Integration of Earth-Sun and Mercury-Sun orbits.
- Energy error analysis for different time-steps.
- Comparison of numerical and theoretical results.

## Getting Started

### Prerequisites
- Python 3.x
- NumPy
- Matplotlib

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/General_Relativity_Simulations.git
    ```
2. Navigate to the Assignment 1 folder:
    ```bash
    cd General_Relativity_Simulations/Assignment1_Leapfrog
    ```

3. Install the required libraries:
    ```bash
    pip install numpy matplotlib
    ```

### Running the Simulation

#### Fixed Time-Step Simulation
To run the fixed time-step Leapfrog simulation for Earth and Mercury:
```bash
python leapfrog_fixed.py

