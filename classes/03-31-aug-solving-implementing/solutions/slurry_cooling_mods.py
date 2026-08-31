"""
File: slurry_cooling_mods
Authors: Sasha D. Hafner and Frederik R. Dalby
Course: Modelling 2026

Description:
    A module with a numerical model for slurry cooling
"""
import numpy as np
from scipy.integrate import solve_ivp

def slur_cool(M_in, T_in, M_init, T_init, A, h, Cp, T_floor, time_range, dt):

    """
    Simulate temperature of slurry in pit that is being cooled from below.
    
        Parameters
        ----------
        M_in: float
            Mass flow rate of manure into the pit (kg/sec)
        T_in: float
            Temperature of ingoing manure (deg C)
        M_init: float
            Initial mass of slurry in the pit (kg)
        T_init: float
            Initial temperature of slurry in the pit (degC)
        A: float
            Area of pit bottom (m2)
        h: float
            heat transfer coefficient (W/(m2 * degC))
        Cp: float
            heat capacity of slurry (J/(kg * degC))
        T_floor: float
            Temperature of pit floor (degC)
        time_range: tupple
            tupple with start and end simulation times (sec)
        dt: float
            time step in solution (sec)
        
        Returns
        -------
        dict with keys 'times' (s), 'M' (kg), 'T' (degC)
    """
    
    times = np.arange(time_range[0], time_range[-1] + dt, dt)
    
    def rates(t, y):
        M = y[0]
        T = y[1]
        dTdt = M_in/M * (T_in - T) - A * h * (T - T_floor)/(M * Cp)
        dMdt = M_in 
        return np.array([dMdt, dTdt])

    res = solve_ivp(rates,
                t_span = [time_range[0], time_range[-1]],
                y0 = [M_init, T_init],
                t_eval = times)

    return{
          'times': res.t,
          'M': res.y[0,:],
          'T': res.y[1,:]
       }
