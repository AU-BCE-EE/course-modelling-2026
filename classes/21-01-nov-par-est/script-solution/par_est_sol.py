# Parameter estimation solution
# Course: Modelling 2026
# Author: Sasha D. Hafner
# Description: A script-based alternative solution to the qmd original for the par est exercise

# Get packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# We need to get least_squares() from the scipy.optimize module
# Normal approach is to get only that function when we just need one
from scipy.optimize import least_squares

# Our model function and fit statistic functions
import diff_mod as dm
import mod_fit as mf

# Let's get the measurement data.
measdat = pd.read_csv('col_salt.csv')
print(measdat)

# Seems we have even 1 d spacing in time, which is convenient.
# We can match that exactly without changing the `diff1D()` function and
# align model output and measurements without a merge operation.

# We need a function for model residuals.
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
    Function for calculating residuals for estimation of the diffusivity D
    from measured total salt mass in a column, using diff1D()

    Parameters
    ----------
    x : float or np.ndarray
        Guess for the value of the D parameter (diffusivity) (m2/s)
    L : float
        Column length (m)
    n : integer
        Number of spatial layers/cells/nodes
    bc : list or tuple
        Boundary conditions, fixed concentrations (kg/m3), bc[0] = left or bottom, bc[1] = right or top
    ci : float
        Initial concentration (kg/m3)
    times : list, tuple, or array
        Times for model evaluation (s), must match measurement times
    area : float
        Column cross-sectional area (m2)
    meas_salt : array-like
        Measured total salt mass in the column (kg) at each time in times

    Returns
    -------
    np.ndarray
        Residuals, model minus measured salt mass (kg)
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


# Now use it.
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

print(lspar)
# Different ways to get the estimate
print(lspar.x)
print(lspar["x"])
print(lspar.x[0])

# Now see how the value does--validation.
# We will use the same times as in the measurements, so we can do some
# quantitative validation as well as graphical.
# Normally for graphical we would use more times for a smooth model curve.
pred01 = dm.diff1D(
    L = 0.1,
    n = 10,
    D = lspar.x[0],
    bc = [36, 0],
    ci = 0,
    t_eval = np.linspace(0, 20 * 86400, 21)
)

area = np.pi * (0.02 / 2)**2
print(area)

salt_mod = (pred01['c'] * pred01['dx'] * area).sum(0)
print(salt_mod)

mmdat = measdat.copy()

# And add the model output we processed above.
# We are trusting that the time alignment is OK.
mmdat['salt_mod_mg'] = salt_mod * 1E6
print(mmdat)

# Plot results
plt.plot(mmdat.time_d, mmdat.salt_mg, marker = 'o', label = 'Measured')
plt.plot(mmdat.time_d, mmdat.salt_mod_mg, label = 'Model output')
plt.xlabel('Time (d)')
plt.ylabel('Column NaCl (mg)')
plt.legend()
plt.savefig('salt_validation.png')

# We could export the combined DataFrame too
mmdat.to_csv('salt_validation.csv')

# And for quantitative validation, use the fit statistic functions from
# mod_fit.
# If you just use one, probably RMSE is the best choice, but it is only
# better than MAE because it is more popular.
print(mf.rmse(mmdat.salt_mg, mmdat.salt_mod_mg))

# We cannot always have low error (RMSE, MAE, or high model efficiency
# (`nsme()`)), but we *should* always have low bias after parameter
# estimation.
print(mf.mbe(mmdat.salt_mg, mmdat.salt_mod_mg))
# We do.

# Troubleshooting:
# If you had trouble, these tips might help.
#
# * Check units, must match
# * Use breakpoint() to check model call inside residuals function
# * print(x) or `sum(res**2)` etc.
#
# Other things to try:
#
# * How much does n cells affect result?
# * Did you try different starting values to check for global vs. local minima?
