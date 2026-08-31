"""
File: evap_mods
Authors: Sasha D. Hafner and Frederik R. Dalby
Course: Modelling 2026

Description:
    A module with a two function (analytical and numerical)
    models for evaporation of gasoline.
"""
import numpy as np
from scipy.integrate import solve_ivp

def evap(k, M_init, time_range, dt):

    """
    Simulate evaporation of gasoline from puddle with analytical model.
    
        Parameters
        ----------
        k: float
            mass transfer coefficient (1/sec)
        M_init : float
            Initial mass of gasoline spilled (g)
        time_range: tupple
            tupple with start and end simulation times (sec)
        dt: float
            time step in solution (sec)
        
        Returns
        -------
        dict with keys 'times' (s) and 'M' (g)
    """
    
    times = np.arange(time_range[0], time_range[-1] + dt, dt)
    M = M_init * np.exp(- k * times)

    return{
          'times': times,
          'M': M,
       }



def evap_num(k, M_init, time_range, dt):

    """
    Simulate evaporation of gasoline from puddle with numerical model.
    
        Parameters
        ----------
        k: float
            mass transfer coefficient (1/sec)
        M_init : float
            Initial mass of gasoline spilled (g)
        time_range: tupple
            tupple with start and end simulation times (sec)
        dt: float
            time step in solution (sec)
        
        Returns
        -------
        dict with keys 'times' (s) and 'M' (g)
    """
    
    times = np.arange(time_range[0], time_range[-1] + dt, dt)

    def rates(t, M):
        return - k * M

    res = solve_ivp(rates,
                    t_span = [time_range[0], time_range[-1]],
                    y0 = [M_init],
                    t_eval = times)
    
    return{
          'times': res.t,
          'M': res.y[0,:],
       }
