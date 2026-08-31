"""
File: evap_pred.py
Authors: Sasha D. Hafner and Frederik R. Dalby
Course: Modelling 2026

Description:
    Application of the `evap()` and `evap_num()` model functions.
"""
import matplotlib.pyplot as plt
import sys
sys.path.append('modules')

import evap_mods as ev

preds = ev.evap(
    k=0.01, 
    M_init=500, 
    time_range=(0., 60 * 60), 
    dt = 60
)

print(preds)

plt.plot(preds['times'], preds['M'], label = "analytical")
plt.ylabel('Mass, g')
plt.xlabel('Time, sec')
plt.legend()
plt.show()

preds_num = ev.evap_num(
    k=0.01, 
    M_init=500, 
    time_range=(0., 60 * 60), 
    dt = 60
)

print(preds_num)

plt.plot(preds_num['times'], preds_num['M'], label = "numerical")
plt.ylabel('Mass, g')
plt.xlabel('Time, sec')
plt.legend()
plt.show()
