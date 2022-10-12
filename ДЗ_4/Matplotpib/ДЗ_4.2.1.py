import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.size'] = 16
plt.figure(figsize=(7,7))
plt.title(r"$y = sin(x)/x^2$")
plt.ylabel("ось Y")
plt.xlabel(r"ось X, $F(x) = \int f(x) dx + С$")
x = np.arange(0, 100, 10)
y = np.sin(x)
mu = np.sin(x)
sigma = np.abs(mu)**0.5
plt.grid(which='major', axis='both', alpha=1)
plt.grid(which='minor', axis='both', alpha=0.5)
plt.legend()
plt.savefig('example.png')
plt.plot(x,y, 'r.', label='Красные треугольники')
plt.show()
