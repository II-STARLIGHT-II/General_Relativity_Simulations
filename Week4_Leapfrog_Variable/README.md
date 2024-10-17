# Week 4: Leapfrog with Variable Time-Step

This project enhances the Leapfrog integrator by introducing a variable time-step to improve efficiency. The time-step varies based on the current position of the object in orbit, leading to more efficient simulations without sacrificing accuracy.

## Features
- Variable time-step Leapfrog integration.
- Improved computational efficiency for highly elliptical orbits (e.g., Mercury).

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
2. Navigate to the Week 4 project folder:
    ```bash
    cd General_Relativity_Simulations/Week4_Leapfrog_Variable
    ```

3. Install the required libraries:
    ```bash
    pip install numpy matplotlib
    ```

### Running the Simulation

To simulate Mercury’s orbit using the Leapfrog integrator with variable time-step:
```bash
python leapfrog_variable.py

