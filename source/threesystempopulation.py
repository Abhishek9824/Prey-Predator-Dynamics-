

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def three_species(y, t, r, K, a, b, c, d, e, f):
    P, D, W = y
    dPdt = r * P * (1 - P / K) - a * P * D
    dDdt = b * P * D - c * D * W - d * D
    dWdt = e * D * W - f * W
    return [dPdt, dDdt, dWdt]

# Initial conditions: [grasses, deer, wolves]
y0 = [50, 10, 5]

# Parameters
r = 1.0
a = 0.01
b = 0.1
c = 0.01
d = 0.1
e = 0.01
f = 0.1
K = 100


t = np.linspace(0, 200, 1000)


sol = odeint(three_species, y0, t, args=(r, K, a, b, c, d, e, f))
P, D, W = sol.T

#for plotting
plt.figure(figsize=(12,6))
plt.plot(t, P, label='Plants', color='green')
plt.plot(t, D, label='Deer', color='orange')
plt.plot(t, W, label='Wolves', color='red')
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('Three-Species Predator–Prey Dynamics')
plt.legend()
plt.grid(True)
plt.show()