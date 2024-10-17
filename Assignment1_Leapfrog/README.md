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

**Results and Comparison of Fixed vs Variable Time-Step Methods**

1. Orbital Trajectories:
Both the fixed time-step and variable time-step methods accurately simulate Earth's orbit around the Sun.
The shape of the orbit remains elliptical in both cases, showing that the Leapfrog method is well-suited for long-term integration of orbital systems.
The variable time-step method adapts to the distance between Earth and the Sun, making it more efficient in regions where precise calculations are needed, such as when Earth is closest to the Sun.
2. Energy Conservation:
Energy conservation is an important measure of the accuracy of a numerical integrator. In both methods, the total energy (kinetic + potential) is tracked over time.

Fixed Time-Step Method:
The energy error is relatively small but accumulates over time due to the fixed time-step.
The fixed time-step method tends to introduce more noticeable drift in total energy, particularly for longer simulation periods.
Variable Time-Step Method:
The variable time-step method shows better energy conservation because it adjusts the time-step dynamically based on the system's state.
The energy error is significantly smaller compared to the fixed time-step method, especially when Earth is closest to the Sun, where more precision is needed.
This makes the variable time-step method more accurate and efficient for simulating highly elliptical orbits.
3. Performance and Efficiency:
The fixed time-step method is straightforward but requires a large number of time steps to achieve high accuracy, which can be computationally expensive.
The variable time-step method, on the other hand, dynamically adjusts the time-step, allowing for greater precision where necessary while using larger time steps when the system is less sensitive. This results in better computational efficiency without sacrificing accuracy.
4. Overall Findings:
For long-term orbital simulations, the variable time-step method is generally more accurate and conserves energy better than the fixed time-step method.
The fixed time-step method is easier to implement but can introduce significant energy drift, especially for longer periods of simulation.
