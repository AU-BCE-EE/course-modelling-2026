"""
File: coffee_demo.py
Authors: Sasha D. Hafner and Frederik R. Dalby
Course: Modelling 2026

Description:
    Application of the `cool_rk()` model function.
"""

import sys
sys.path.append('modules')

import cooling_mods as cm

preds = cm.cool(
    T_init=80, 
    T_air=20, 
    mass=300, 
    area=0.026, 
    h=75, 
    time_range=(0., 60 * 60), 
    dt = 5 * 60
)

print(preds)

# Plot predictions
plt.plot(times / 60, T_coffee, 'ro-', label = 'Euler')
plt.legend()
plt.xlabel('Time (min)')
plt.ylabel(r'Predicted coffee temperature $(^\circ\mathregular{C})$')
plt.show()


