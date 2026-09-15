
import numpy as np
import salt_mod as sm

sm.salty(
    conc_init=35, 
    conc_river=0.01, 
    to_rate=3.6e-5, 
    times = np.linspace(0, 1000)
)
