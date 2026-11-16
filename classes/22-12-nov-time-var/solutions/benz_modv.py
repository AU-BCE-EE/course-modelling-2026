"""
File name: benz_modv.py
Author: Sasha D. Hafner
Course: Modelling 2026

Description:
    This module defines numerical models for benzene volatilization
    from a wastewater lagoon. The version here includes a time-variable
    input.

Usage:
    See time_var_solution.qmd.
"""

# Load packages 
import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import PchipInterpolator

def benzv(clin, cl0, ca, wind_dat, depth, h, hrt, t_range, t_step):  

    """ 
    Dynamic numerical model for volatilization of benzene 
    from a lagoon, as a batch system.

    Parameters
    ----------
    clin : float
        Benzene concentration in untreated wastewater (g/m3) 
    cl0 : float
        Initial benzene concentration in lagoon (g/m3) 
    ca : float
        Constant ambient benzene concentration in air (g/m3)
    wind_dat : DataFrame
        Pandas DataFrame with time (s) in the first column and 
        wind speed at 2 m height above the lagoon surface (m/s)
        in the second column
    depth : float
        Lagoon depth (assumed to be uniform) (m)
    h : float
        Henry's law constant (volumetric concentration based, aq:g)
    hrt : float
        hydraulic retention time based on flow rate (in = out) and lagoon volume (s)
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

    # Create interpolation function for wind speed
    wind_func = PchipInterpolator(wind_dat.iloc[:, 0],  wind_dat.iloc[:, 1], extrapolate = False)
     
    # Define rates function
    def rates(t, cl):

        # Calculate wind speed (m/s)
        ws = wind_func(t)
        # And mass transfer coefficient (m/s)
        kg =  1e-6 * (1 + 0.1 * ws**2) / (1 + 0.1)

        # Finally, derivative (g/m3-s)
        dcdt = (clin - cl) / hrt - kg * (cl / h - ca) / depth

        return dcdt

    res = solve_ivp(
        rates, 
        t_span = t_range, 
        y0 = [cl0], 
        t_eval = np.arange(t_range[0], t_range[1] + t_step, t_step)
    )

    # Return user-friendly results object (dictionary here)
    out = {
        "t": res.t, 
        "cl": res.y[0, :]
    }

    return out
