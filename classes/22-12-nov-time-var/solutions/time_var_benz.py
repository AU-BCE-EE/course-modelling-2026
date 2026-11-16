"""
File: time_var_benzene.py
Class: Modelling 2026
Author: Sasha D. Hafner

Description:
    A script that demonstrates a version of the benzene volatilization
    model with a time-variable input.
"""

# Load modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# The model module
import benz_modv as bmv

# The measurement data
weather = pd.read_csv('weather.csv')

# The model function docstring says we need time in s in the first column and wind speed in m/s in second
# Best option may be to make a new DataFrame
wind = pd.DataFrame(dict(time_s = weather['time_hr'] * 3600, wind_m_s = weather['wind_m_s']))

# Let's start from a high (fresh) benzene concentration . . .
pred_high = bmv.benzv(
    clin=10, 
    cl0=10, 
    ca=0, 
    wind_dat=wind, 
    depth=1,
    h=5,
    hrt=21 * 86400,
    t_range = (0, 40 * 86400),
    t_step = 3600
)

# and a low one
pred_low = bmv.benzv(
    clin=10, 
    cl0=0, 
    ca=0, 
    wind_dat=wind, 
    depth=1,
    h=5,
    hrt=21 * 86400,
    t_range = (0, 40 * 86400),
    t_step = 3600
)

# And make some higher wind speed just for fun
wind2 = pd.DataFrame(dict(time_s = weather['time_hr'] * 3600, wind_m_s = 5 * weather['wind_m_s']))

pred_windy = bmv.benzv(
    clin=10, 
    cl0=3, 
    ca=0, 
    wind_dat=wind2, 
    depth=1,
    h=5,
    hrt=21 * 86400,
    t_range = (0, 40 * 86400),
    t_step = 3600
)


plt.plot(pred_low['t'] / 86400, pred_low['cl'], label = 'Low start')
plt.plot(pred_high['t'] / 86400, pred_high['cl'], label = 'High start')
plt.plot(pred_windy['t'] / 86400, pred_windy['cl'], label = 'Windy, high start')
plt.xlabel('Time (days)')
plt.ylabel('Benzene conc. (g/m3)')
plt.savefig('benz1.png')
