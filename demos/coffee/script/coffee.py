"""
File: coffee.py
Authors: Sasha D. Hafner and Frederik R. Dalby
Course: Modelling 2026

Description:
    A script with a simple model of a cooling 
    cup of coffee.
"""

# Load NumPy package
import numpy as np

# And plotting package
import matplotlib.pyplot as plt

# Set model inputs
cp = 4.2       # J g-1 K-1
T_init = 80    # deg. C
T_air = 20     # deg. C
mass = 300     # g
area = 0.026   # m2
h = 75         # W m-2 K-1
dt = 60 * 5    # 5 min time step (s)
times = np.arange(0, 3600 + dt, dt) # Times (s)

# Calculate model constant or coefficient, which does not change over time
con_cool = area * h / (cp * mass)

# Create vector of temperatures to fill later
T_coffee = np.zeros_like(times)

# Set the first value
T_coffee[0] = T_init

# Implement an explicit forward finite difference method in a loop
for i in range(1, len(T_coffee)):
    T_coffee[i] = T_coffee[i - 1]  - con_cool * (T_coffee[i - 1] - T_air) * dt

print(T_coffee)

# Plot predictions
plt.plot(times / 60, T_coffee, 'ro-', label = 'Euler')
plt.legend()
plt.xlabel('Time (min)')
plt.ylabel(r'Predicted coffee temperature $(^\circ\mathregular{C})$')
plt.show()

