"""
File name: ice_mods.py
Author: Sasha D. Hafner
Course: Modelling 2026

Description:
    This module defines a numerical model for disappearance of a 
    melting block of ice. Assumes hemispherical shape and no heat
    transfer through bottom.

Usage:
    See ice_sol.qmd (or ice_sol.html) for examples.
"""

# Load packages 
import pandas as pd
import numpy as np
from scipy.integrate import solve_ivp

# Define model function
def melt(mass_0,
         temp_air,
         h, 
         t_range, 
         t_step,
         dens = 920,
         temp_freeze = 0,
         Hf = 333000
    ):  

    """ 
    Dynamic model for heat transfer to a melting block of ice, with 
    disappearance of the ice over time. 

    Parameters
    ----------
    mass_0 : float
        Initial mass of ice (kg) 
    temp_air : float
        Air temperature (deg. C)
    h : float
        Convection heat transfer coefficient (W/m2-K)
    t_range : list or tuple of two floats 
        Minimum and maximum time in output (s) 
    t_step : float
        Time step in output (s)
    dens : float
        Ice density (kg/m3)
    temp_freeze : float
        Freezing point (deg. C)
    Hf : float
        Heat of fusion (J/kg)

    Returns
    -------
    dictionary
        With elements 't' for time (s) and 'm' for ice mass remaining (kg)
 
    """
     
    # Define rates function
    def rates(t, mass_t):

        # Skip when there is very little ice remaining (avoid power caculation error)
        if mass_t > 1e-10:
            # Get current exposed upper area, assuming hemisphere
            area = 2 * np.pi * (3 * mass_t / (2 * np.pi * dens))**(2/3)

            # Heat flow (W)
            Q = area * h * (temp_air - temp_freeze)

            # Melting rate (kg/s)
            dmdt = - Q / Hf

            return dmdt
        else:
            return 0.


    res = solve_ivp(
        rates, 
        t_span = t_range, 
        y0 = [mass_0], 
        t_eval = np.arange(t_range[0], t_range[1] + t_step, t_step)
    )

    # Return user-friendly results object (dictionary here)
    out = {
        "t": res.t, 
        "m": res.y[0, :]
    }

    return out
