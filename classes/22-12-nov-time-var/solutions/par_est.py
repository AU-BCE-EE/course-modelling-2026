"""
File: par_est.py
Class: Modelling 2026
Author: Sasha D. Hafner

Description:
    A script for parameter estimation for a benzene volatilization model.
    This script loads a model module and includes the definition of a 
    function for calculating residuals directly.
"""

# Load modules
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# The model module
import benz_mod as bnm

