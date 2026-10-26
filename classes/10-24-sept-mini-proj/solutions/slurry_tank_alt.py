
"""
File name: slurry_tank_alt.py
Author: Sasha D. Hafner and Frederik Dalby
Course: Modelling 2026

Description:
    This module defines functions for modeling ammonia volatilization
    from a slurry storage tank.

Usage:
    See other files in this directory

"""

# Load packages 
import numpy as np
from scipy.integrate import solve_ivp

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def dynmod(rt,
           depth,
           c_TAN_0,
           c_urea_0,
           c_bg,
           pH,
           ku,
           kl,
           t_range, 
           t_step,
           hen = 2000.,
           pka = 9.24):
    """ 
    Dynamic model for ammonia volatilization from a manure storage 
    tank with constant and equal manure flow in and out and a constant
    volume of manure. Includes urea hydrolysis.

    Parameters
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
    t_range : tuple, list, or array (length 2)
        Initial and final time requested in output (s).
    t_step : float
        Time step requested for output (s).
    hen : float
        Henry's law constant (dimensionless, aq:g).
    pka : float
        Negative log_10 of the equilibrium constant 
        (acid dissociation constant) for NH4+ -> NH3 + H +
        (dimensionless).
 
    """
  
    # Sort out some constants
    frac_NH3 = 1/(1 + 10**(pka - pH))

    # Define rates function
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
    res = solve_ivp(rates, t_span = t_range, y0 = [c_TAN_0, c_urea_0], 
                    t_eval = np.arange(t_range[0], t_range[1] + t_step, t_step))

    # Return results
    return(res)

def ssmod(rt,
          depth,
          c_TAN_0,
          c_bg,
          pH,
          ku,
          kl,
          hen = 2000.,
          pka = 9.24):
    """ 
    Steady-state model for ammonia volatilization from a manure storage 
    tank with constant and equal manure flow in and out and a constant
    volume of manure. Does not include urea.

    Parameters
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
  
    # Sort out some constants
    frac_NH3 = 1/(1 + 10**(pka - pH))

    # And our two grouped constants K and B
    kk = rt * kl * frac_NH3 / depth
    bb = rt * kl * c_bg / depth

    c_TAN = (c_TAN_0 - bb) / (1 + kk)

    # Return results
    return(c_TAN)


