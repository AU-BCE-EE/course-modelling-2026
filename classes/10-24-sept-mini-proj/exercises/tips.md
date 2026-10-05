# Some suggestions on slurry model inputs

## 1. Henry's law constant
We have worked with a dimensionless form of Henry's law constant. 
Here is some Python code for calculating it as a function of temperature

```
# 1. temp_c is input temperature in degrees C but the calculations are based on Kelvin
temp_k = temp_c + 273.15
# 2. Universal gas constant (atm L/mol-K)
R = 0.082057
# 3. Henry's law constant in mol / L - atm
kh = 10**(-3.51645 - 0.0013637 * temp_k + 1701.35 / temp_k)
# 4. Henry's law constant in dimensionless form aq:g (e.g., g/m3 aq. per g/m3 gas, g/L per g/L, etc.)
hen = R * temp_k * kh
```

At 25 $\degC$ you should get a value of 1485.
This high value reflects the high solubility of ammonia; it means the concentration in the liquid phase (e.g., g/m3) is $> 1000$ times as large as the concentration in the gas phase (also in g/m3, but here m3 of *gas*).

This equation for `kh' comes from:

Clegg, S., Brimblecombe, P., 1989. Solubility of ammonia in pure aqueous and multicomponent solutions. Journal of Physical Chemistry 93 (20), 7237-7248.

Technically the $L$ is $kg$ of water, but the substitution is good enough for our work.

## 2. Conversion of liquid and gas phase overall mass transfer coefficients

An overall mass transfer coefficient for interphase mass transfer must be for the appropriate phase.
If the flux is to be calculated using gas phase concentrations, the mass transfer coefficient must be in gas phase units, e.g., 

$$
J = K_G \cdot (c_g^* - c_g).
$$

If, on the other hand, liquid (aqueous) phase units are used for concentrations, $K_L$, in liquid phase units, must be used:

$$
J = K_L \cdot (c_l - c_l^*).
$$

We saw in class how these two equations are equivalent, i.e., they will return the exact same value of the flux $J$ if the conversion is done correctly.
To convert between $K_L$ and $K_G$, it is helpful to think of the units as having a separate numerator and denominator.
$K_L$ in $\mps$ actually means flux in $\gpspms$ per difference in concentration in $\gpmc$.
(Show that the units work out.)
Of course the $\mc$ bit of the expression is liquid phase volume, because this is $K_L$.
So to convert to $K_G$, use:

$$
K_G = K_L \cdot H,
$$

where $H=$ dimensionless Henry's law constant (aq:g).

## 3. Values for overall mass transfer coefficient

The value for an mass transfer coefficient for ammonia volatilization from slurry exposed to the atmosphere would be expected to depend on air flow and slurry properties. 
But a reasonable value from a recent literature review of measurements (<https://doi.org/10.1016/j.biosystemseng.2022.08.007>) is 0.01 $\mps$ for uncovered slurry.


## 4. What to do with free ammonia?

There was some confusion in class about what exactly should be done with free ammonia, $\ce{NH3(aq)}$.
One thing we saw that was not correct was trying to write a governing equation (GE) for that chemical species.
If you assume chemical equilibrium between $\ce{NH4+}$ and $\ce{NH3(aq)}$, you only need a GE for total ammonia (TAN) and not one for $\ce{NH3(aq)}$.
Why not?
Well, you cannot both assume that the time derivative of free ammonia is determined by its volatilization rate *and* that free ammonia is in equilibrium with ammonium.
The first assumption is consistent with a kinetic model and the second an equilibrium model.
Try it, conceptually, thinking about how solute concentrations would change over time steps to see that it won't work.

So, what should you do? 
Think carefully about the state variable(s) for this model. Do you need more than one? You only need one GE per state variable.
Instead of thinking about tracking the concentration of free ammonia over time, think about tracking the TAN concentration, and *linking* the rate of TAN loss to free ammonia volatilization with the chemical speciation equation (pH and temperature dependent equations). 
It may help to recognize that you could write a GE for TAN that does not even explicitly include free ammonia, but instead a constitutive equation that depends on pH and temperature, incorporating the speciation bit directly in the GE.
But you don't have to do this; it is fine to use free ammonia concentration as an intermediate variable in a numerical model.

## 5. Other inputs

Remember you are welcome to ask us for numeric values for other inputs!
