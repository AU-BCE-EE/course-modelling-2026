"""
File: salt_mods
Authors: Sasha D. Hafner and Frederik R. Dalby
Course: Modelling 2026

Description:
    A module with a two function (analytical and numerical)
    models for salt concentration in tank.
"""
import numpy as np
from scipy.integrate import solve_ivp

def salt(F_in, V, C_init, C_inlet, time_range, dt):

    """
    Simulate salt concentration in a CSTR with a analytical model.
    
        Parameters
        ----------
        F_in: float
            Volume flow into the tank (m3/sec)
        V: float
            Volume of salt water
        C_init: float
            Initial concnetration of salt (kg/m3)
        C_inlet: float
            Concentration of salt in inlet flow (kg/m3)
        time_range: tupple
            tupple with start and end simulation times (sec)
        dt: float
            time step in solution (sec)
        
        Returns
        -------
        dict with keys 'times' (s) and 'C' (kg/m3)
    """
    
    times = np.arange(time_range[0], time_range[-1] + dt, dt)
    F = F_in
    K = F/V

    # derivation of analytica model
    # dC/dt = K * C_inlet - K * C
    # gather C's
    # dC/dt = K * (C_inlet - C)
    # separate vars
    # dC/(C_inlet - C) = K *dt
    # integrate
    # -ln(C_inlet - C) = K*t + C1
    # mult by -1 to get clean ln on LHS
    # ln(C_inlet - C) = -K*t - C1
    # C_inlet - C = exp(-K*t - C1) = exp(-C1) * exp(-K*t)
    # sub exp(-C1) with C2
    # C_inlet - C = C2 * exp(-K*t)
    # isolate C
    # -C = C2 * exp(-K*t) - C_inlet
    # C = -C2 * exp(-K*t) + C_inlet
    # set t = 0, then C0 = -C2 + C_inlet --> -C2 = C0 - C_inlet --> C2 = C_inlet - C0

    C2 = C_inlet - C_init
    # now write analytical solution
    C = -C2 * np.exp(-K * times) + C_inlet

    return{
          'times': times,
          'C': C,
       }


def salt_num(F_in, V, C_init, C_inlet, time_range, dt):

    """
    Simulate salt concentration in a CSTR with numerical model.
    
        Parameters
        ----------
        F_in: float
            Volume flow into the tank (m3/sec)
        V: float
            Volume of salt water
        C_init: float
            Initial concnetration of salt (kg/m3)
        C_inlet: float
            Concentration of salt in inlet flow (kg/m3)
        time_range: tupple
            tupple with start and end simulation times (sec)
        dt: float
            time step in solution (sec)
        
        Returns
        -------
        dict with keys 'times' (s) and 'C' (kg/m3)
    """
    
    times = np.arange(time_range[0], time_range[-1] + dt, dt)
    F_out = F_in

    def rates(t, C):
        return (F_in * C_inlet - F_out * C)/V

    res = solve_ivp(rates,
                t_span = [time_range[0], time_range[-1]],
                y0 = [C_init],
                t_eval = times)

    return{
          'times': res.t,
          'C': res.y[0,:],
       }
