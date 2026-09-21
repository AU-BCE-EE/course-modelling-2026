"""
File name: benz_mods.py
Author: Sasha D. Hafner
Course: Modelling 2026

Description:
    This module defines analytical models for benzene volatilization
    from a wastewater lagoon.

Usage:
    See benz_sol.qmd (or benz_sol.html) for examples.
"""

# Load packages 
import numpy as np
from scipy.integrate import solve_ivp

# Define model function
def benzvol_batch(cl0, ca, kg, depth, h, t_range, t_step):  

    """ 
    Dynamic analytical model for volatilization of benzene 
    from a lagoon, as a batch system.

    Parameters
    ----------
    cl0 : float
        Initial benzene concentration in lagoon (g/m3) 
    ca : float
        Constant ambient benzene concentration in air (g/m3)
    kg : float
        Overall interface mass transfer coefficient in gas phase units (m/s)
    depth : float
        Lagoon depth (assumed to be uniform) (m)
    h : float
        Henry's law constant (volumetric concentration based, aq:g)
    t_range : list or tuple of two floats 
        Minimum and maximum time in output (s) 
    t_step : float
        Time step in output (s)

    Returns
    -------
    dictionary
        With elements 't' for time (s) and 'cl' for benzene concentration 
        in wastewater (g/m3)
 
    """
     
    # Sort out evaluation times
    t_eval = np.arange(t_range[0], t_range[1] + t_step, t_step)

    # And the solution
    cl = cl0 * np.exp(-kg / h / depth * t_eval)

    # Return dictionary of results
    out = {
        "t": t_eval, 
        "cl": cl 
    }

    return out
