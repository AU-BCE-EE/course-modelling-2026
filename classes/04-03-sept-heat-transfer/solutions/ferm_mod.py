"""
File name: ferm_mod.py
Author: Sasha D. Hafner
Course: Modelling 2026

Description:
    This module defines an analytical steady-state
    model for the temperature of a heated fermenter.

Usage:
    See ferm_sol.qmd

"""

def ferm_temp(
    temp_jack,
    temp_air,
    u_jack,
    u_top,
    area_jack,
    area_top
    ):

    """
    Steady-state model of a fermenter heated with a water jacket.

    Parameters
    ----------
    temp_jack : float
        Temperature of water in water jacket (deg. C)
    temp_air : float
        Temperature of ambient air (deg. C)
    u_jack : float
        Overall heat transfer coefficient between bulk jacket water and bulk fermenter contents (W/m2-K)
    u_top : float
        Overall heat transfer coefficient between bulk fermenter contents and air (W/m2-K)
    area_jack : float
        Area of water jacket/fermenter interface (m2)
    area_top : float
        Area of fermenter top exposed to air (m2)

    Returns
    -------
    float
        With predicted temperature of bulk fermenter fluid
 
    """

    num = (area_jack * u_jack * temp_jack + area_top * u_top * temp_air)
    dem = (area_jack * u_jack + area_top * u_top)
    temp_ferm =  num / dem 

    return temp_ferm


