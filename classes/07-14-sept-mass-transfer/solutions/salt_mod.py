"""
File name: salt_mod.py
Author: Sasha D. Hafner
Course: Modelling 2026

Description:
    Implementation of analytical ocean salt
    accumulation model in salty() function. 

Usage:
    See demo script in this directory.

"""

def salty(
    conc_init,
    conc_river,
    to_rate,
    times    
):

    """
    ...fill this in!
    """

    conc = conc_init + to_rate * conc_river * times

    return conc
