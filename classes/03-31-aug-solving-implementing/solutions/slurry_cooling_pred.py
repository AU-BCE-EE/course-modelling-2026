"""
File: slurry_cooling_pred.py
Authors: Sasha D. Hafner and Frederik R. Dalby
Course: Modelling 2026

Description:
    Application of the `salt()` and `salt_num()` model functions.
"""
import matplotlib.pyplot as plt
import sys
sys.path.append('modules')
import slurry_cooling_mods as sc

preds = sc.slur_cool(
    M_in = 500 * 6/(60*60*24), 
    T_in = 37,
    M_init = 40000, 
    T_init = 20, 
    A = 200,
    h = 10,
    Cp = 4200,
    T_floor = 12,
    time_range=(0., 60 * 60 * 24 * 500), 
    dt = 60 * 60
)

print(preds)

plt.plot(preds['times']/60/60/24, preds['T'], label = "numerical")
plt.ylabel('Temp, degC')
plt.xlabel('Time, days')
plt.legend()
plt.show()

plt.plot(preds['times']/60/60/24, preds['M'], label = "numerical")
plt.ylabel('Slurry mass, kg')
plt.xlabel('Time, days')
plt.legend()
plt.show()
