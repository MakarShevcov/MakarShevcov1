import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.size'] = 16
plt.figure(figsize=(7,7))
plt.title(r"$y = e^(-x*sin(x))$")
plt.ylabel("ось Y")
plt.xlabel(r"ось X")
x = np.arange(10, 100, 0.01)
y = np.exp(-x * np.sin(x))
mu = np.exp(-x * np.sin(x))
sigma = np.abs(mu)**0.5
plt.grid(which='major', axis='both', alpha=1)
plt.grid(which='minor', axis='both', alpha=0.5)
plt.minorticks_on()
plt.legend()
plt.savefig('example.png')
plt.plot(x,y, 'r', label='Красные треугольники')
plt.show()
