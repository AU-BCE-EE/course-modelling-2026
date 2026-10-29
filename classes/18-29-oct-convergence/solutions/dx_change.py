import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Defining the rates function or dT/dt function
def dTdt(t, T, dx, a, h, p, cp, T_air):
    
    dTdt = np.zeros(len(T))
    N = len(T) - 1
    dTdt[0] = 0 # K/s
    TN1_ghost = T[N-1] - 2*dx*h/k * (T[N] - T_air)
    dTdt[N] = a * (TN1_ghost - 2*T[N] + T[N-1])/dx**2 # K/s

    for i in range(1, N):
        dTdt[i] = a * (T[i+1] - 2*T[i] + T[i-1])/dx**2 # K/s
        
    return dTdt

# finding constants from the internet about copper 
cp = 385 # J/(kg * K)
k = 401 # W/(m*K)
p = 8960 # kg/m3
a = k/(cp*p) # m2/s
T_air = 20 # degree C
h = 10 # W/(K * m2)
L = 10 # length of wire, m
tmax = 60*60*1 # lets try to run for 1 hour (in seconds) 
# decide where to check the convergence. Lets go for the end of the wire
length_of_interest = 2 # m

# make a function that runs the models and depends on dx
def run_model(dx):

    x_grid = np.arange(0, 10 + dx, dx)
    T0 = np.zeros(len(x_grid))
    T0[0] = 200

    sol = solve_ivp(dTdt, [0, tmax], T0, method = 'LSODA', 
                    t_eval = np.linspace(0, tmax, 100),
                    args = (dx, a, h, p, cp, T_air))

    idx = np.argmin(abs(x_grid - length_of_interest))
    return sol.y[idx, -1]

# make array of dx_values you want to test
dx_values = [2, 1, 0.5, 0.1, 0.05, 0.01, 0.005]

# empty list to hold results
results = []

for dx in dx_values:
    results.append(run_model(dx))

for i in range(len(dx_values)):
    print("dx =", dx_values[i], "m -> c(2 m, 1 hour) =", results[i], "deg C")

plt.plot(dx_values, results, marker = "o")
plt.gca().invert_xaxis() 
plt.xlabel('dx, m')
plt.ylabel('Temperature at 2 m after 1 hour, deg C')
plt.show()