import numpy as np
import matplotlib.pyplot as plt

k = 0.5
y0 = 10
tmax = 20

def rates(t, y):
    return -k * y

# exact solution on many time points
t_exact = np.linspace(0, tmax, 1000)
y_exact = []
for i in range(len(t_exact)):
    y_exact.append(y0 * np.exp(-k * t_exact[i]))

# forward Euler for a given dt
def euler(dt):
    n_steps = int(round(tmax / dt))
    t = []
    y = []
    t.append(0.0)
    y.append(y0)
    for i in range(n_steps):
        y_new = y[i] + dt * rates(t[i], y[i])
        t.append(t[i] + dt)
        y.append(y_new)
    return t, y

dt_values = [1, 4.1, 3.9]

plt.figure()
plt.plot(t_exact, y_exact, 'k-', label="exact")
for dt in dt_values:
    t, y = euler(dt)
    plt.plot(t, y, 'o-', label="forward Euler, dt = " + str(dt))

plt.xlabel("time, s")
plt.ylabel("y")
#plt.yscale("symlog", linthresh=1e-3)
plt.legend()
plt.show()