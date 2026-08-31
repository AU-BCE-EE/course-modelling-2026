"""
File: salt_pred.py
Authors: Sasha D. Hafner and Frederik R. Dalby
Course: Modelling 2026

Description:
    Application of the `salt()` and `salt_num()` model functions.
"""
import matplotlib.pyplot as plt
import sys
sys.path.append('modules')
import salt_mods as cstr

preds = cstr.salt(
    F_in =0.05, 
    V = 5, 
    C_init = 4,
    C_inlet = 0.5, 
    time_range=(0., 60 * 60), 
    dt = 60
)

print(preds)

plt.plot(preds['times'], preds['C'], label = "analytical")
plt.ylabel('C, kg/m3')
plt.xlabel('Time, sec')
plt.legend()
plt.show()


preds_num = cstr.salt_num(
    F_in =0.05, 
    V = 5, 
    C_init = 4,
    C_inlet = 0.5, 
    time_range=(0., 60 * 60), 
    dt = 60
)

print(preds_num)

plt.plot(preds_num['times'], preds_num['C'], label = "numerical")
plt.ylabel('C, kg/m3')
plt.xlabel('Time, sec')
plt.legend()
plt.show()
