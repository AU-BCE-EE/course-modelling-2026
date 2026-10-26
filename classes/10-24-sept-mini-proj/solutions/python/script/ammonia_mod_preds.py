
"""
File name: ammonia_mods_demo.py
Author: Sasha D. Hafner
Course: Modelling 2025

Description:
    This demo implements and applies a model for ammonia 
    volatilization from a manure storage tank. Model is dynamic and 
    includes urea hydrolysis. The model is programmed directly in 
    this script, in contrast to a module-based approach.

Usage:
    Run in Python3 interactively or with 
    `python3 ammonia_mod_preds.py` to get output.

"""

# Load packages 
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

""" 
Model inputs
----------
rt : float
    Retention time of manure in the tank (s)
depth : float
    Depth of manure in the tank (m).
c_TAN_0 : float
    Concentration of TAN in fresh manue (kg/m3 as N).
c_urea_0 : float
    Concentration of urea in fresh manue (kg/m3 as N).
c_bg : float
    Converted concentration of NH3 (g) in ambient (background) 
    air (kg/m3 as N in aqueous phase).
pH : float
    Manure pH (pH units).
ku : float
    First-order reaction rate constant for urea hydrolysis (1/s).
kl : float
    Overall liquid-phase mass transfer coefficient (m/s).
hen : float
    Henry's law constant (dimensionless, aq:g).
pka : float
    Negative log_10 of the equilibrium constant 
    (acid dissociation constant) for NH4+ -> NH3 + H +
    (dimensionless).

"""

# Inputs (see docstring above for description and units)
rt = 200 * 86400
depth = 4
c_bg = 0. * 2300
kl = 0.01 / 2300
pka = 9.24
pH = 7.
c_TAN_0 = 3
c_urea_0 = 0
ku = 0.
frac_NH3 = 1/(1 + 10**(pka - pH))
hen = 2000.

# Define rates function
# Will use inputs from global environment
def rates(t, conc):

    c_TAN = conc[0]
    c_urea = conc[1]

    TAN_in = c_TAN_0 / rt
    TAN_out = c_TAN / rt

    urea_in = c_urea_0 / rt
    urea_out = c_urea / rt

    urea_hyd = ku * c_urea

    volat = kl / depth * (frac_NH3 * c_TAN - c_bg / hen)

    dc_TAN_dt = TAN_in - TAN_out + urea_hyd - volat
    dc_urea_dt = urea_in - urea_out - urea_hyd

    return np.array([dc_TAN_dt, dc_urea_dt])


# Now solve with solve_ivp()
pred_ref = solve_ivp(rates, t_span = [0, 86400*730], y0 = [c_TAN_0, c_urea_0], 
                t_eval = np.arange(0, 86400*730 + 3600, 3600))

# Print results
pred_ref

# Plot results
plt.close()
plt.plot(pred_ref.t / 86400, pred_ref.y[0, :])
plt.ylim(0, 3.1)
plt.xlabel('Time (d)')
plt.ylabel('Tank TAN conc. (kg/m3)')
plt.savefig('ref.png')

# Additional solve_ivp() calls could come below. . .
