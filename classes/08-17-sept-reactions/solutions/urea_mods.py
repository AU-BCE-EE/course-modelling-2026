"""
File name: urea_mods.py
Author: Sasha D. Hafner
Course: Modelling 2026

Description:
    This module defines a numeric and an analytical model
    for urea hydrolysis.

Usage:
    See urea.qmd
"""

# Load packages
import numpy as np
from scipy.integrate import solve_ivp

# Numerical model function
def urea_num(
    c0,
    k,
    t_range,
    t_step
):

    """
    Dynamic numerical model for urea hydrolysis.

    Parameters
    ----------
    c0 : list or tuple of floats
        Initial concentrations of urea, NH3, and CO2, in that order (mg/L)
    k : float
        First-order rate constant (1/s)
    t_range : list or tuple of two floats 
        Minimum and maximum time in output (s) 
    t_step : float
        Time step in output (s)

    Returns
    -------
    dictionary
        With elements 't' for time (s), c_urea, c_NH3, 
        and c_CO2 for solute concentrations (mg/L)
    """

    # Set molar masses (g/mol or mg/mmol)
    mm = np.array([60.056, 17.031, 44.010])

    # Stoichiometric coefficients
    ss = np.array([-1, 2, 1])

    # Define rates function
    def rates(t, conc):

        # Derivatives depend only on urea concentration
        # Let's get milimolar concentration here (mmol/L)
        cm = conc[0] / mm[0]

        # Reaction rate in mmol/L-s
        rr = k * cm 

        # Now derivatives
        dcdt = ss * mm * rr

        return dcdt

    res = solve_ivp(
        rates,
        t_span = t_range, 
        y0 = c0, 
        t_eval = np.arange(t_range[0], t_range[1] + t_step, t_step)
    )

    # Return results in dictionary

    out = {
        't': res.t,
        'c_urea': res.y[0, :],
        'c_NH3': res.y[1, :],
        'c_CO2': res.y[2, :]
    }

    return out

# Analytical model function
def urea_ana(
    c0,
    k,
    t_range,
    t_step
):

    """
    Analytical numerical model for urea hydrolysis.

    Parameters
    ----------
    c0 : list or tuple of floats
        Initial concentrations of urea, NH3, and CO2, in that order (mg/L)
    k : float
        First-order rate constant (1/s)
    t_range : list or tuple of two floats 
        Minimum and maximum time in output (s) 
    t_step : float
        Time step in output (s)

    Returns
    -------
    dictionary
        With elements 't' for time (s), c_urea, c_NH3, 
        and c_CO2 for solute concentrations (mg/L)
    """

    # Set molar masses (g/mol or mg/mmol)
    mm = np.array([60.056, 17.031, 44.010])

    # Stoichiometric coefficients
    ss = np.array([-1, 2, 1])

    t_eval = np.arange(t_range[0], t_range[1] + t_step, t_step)

    cm0 = c0[0] / mm[0]
    c_urea = cm0 * np.exp(-k * t_eval)
    c_NH3 = ss[1] * cm0 * (1 - np.exp(-k * t_eval))
    c_CO2 = ss[2] * cm0 * (1 - np.exp(-k * t_eval))

    # Return results in dictionary

    out = {
        't': t_eval,
        'c_urea': c_urea * mm[0],
        'c_NH3': c_NH3 * mm[1],
        'c_CO2': c_CO2 * mm[2]
    }

    return out


