import pandas as pd

measdat = pd.read_csv('col_salt.csv')
measdat

def res_func(
    x,
    L,       
    n,       
    bc,      
    ci,      
    times,
    area,
    meas_salt
):

    """
    Function for calculating residuals for  . . . 

    Parameters
    ----------
    x : float
        Guess for values for the D parameter (diffusivity)
    . . . 


    Returns
    -------
    np.ndarray
        Residuals
    """

    # Model call
    pred = dm.diff1D(
        L=L,
        n=n,
        D=x,
        bc=bc,
        ci=ci,
        t_eval=times 
    )

    # Calculate residuals 
    mod_salt = (pred['c'] * pred['dx'] * area).sum(0)

    res = mod_salt - meas_salt
    
    print(x)
    print(sum(res**2))

    # Return residuals
    return res


import diff_mod as dm

import numpy as np

# We need to get least_squares() from the scipy.optimize module
# Normal approach is to get only that function when we just need one 
from scipy.optimize import least_squares

lspar = least_squares(
    res_func, 
    x0=2E-9, 
    kwargs=dict(
        L=0.1,
        n=10,
        bc=[36, 0],
        ci=0,
        times=np.linspace(0, 20 * 86400, 21),
        area=np.pi * (0.02 / 2)**2,
        meas_salt=measdat['salt_mg'] / 1e6
    )
)

lspar
lspar.x
lspar["x"]
lspar.x[0]

area = np.pi * (0.02 / 2)**2 
area

pred01 = dm.diff1D(
    L = 0.1,
    n = 10,
    D = lspar.x[0],
    bc = [36, 0],
    ci = 0,
    t_eval = np.linspace(0, 20 * 86400, 21)
)

area = np.pi * (0.02 / 2)**2 
area

salt_mod = (pred01['c'] * pred01['dx'] * area).sum(0)
salt_mod

mmdat = measdat.copy()

mmdat['salt_mod_mg'] = salt_mod * 1E6
mmdat

import matplotlib.pyplot as plt
plt.plot(mmdat.time_d, mmdat.salt_mg, marker = 'o', label = 'Measured')
plt.plot(mmdat.time_d, salt_mod, marker = 'o', label = 'Model output')
plt.xlabel('Time (d)')
plt.ylabel('Column NaCl (mg)')
plt.legend()

