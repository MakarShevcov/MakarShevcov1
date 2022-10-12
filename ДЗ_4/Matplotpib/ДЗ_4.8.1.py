import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.size'] = 16
plt.figure(figsize=(7,7))
plt.title(r"$y = e^(x*sin(x))$")
plt.ylabel("ось Y логарифмический масштаб")
plt.xlabel(r"ось X")
x = np.arange(10, 100, 0.1)
y = np.exp(x * np.sin(x))
mu = np.exp(x * np.sin(x))
sigma = np.abs(mu)**0.5
plt.grid(which='major', axis='both', alpha=1)
plt.grid(which='minor', axis='both', alpha=0.5)
plt.minorticks_on()
plt.savefig('example.png')
plt.plot(x,y, 'r', label=r"$y = e^(x*sin(x))$")
plt.legend()
plt.yscale('log')
plt.show()
