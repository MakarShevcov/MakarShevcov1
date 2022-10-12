import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.size'] = 16
plt.figure(figsize=(7,7))
plt.title(r"Это название  графика  $y = x^3$ - да, можно использовать LaTeX:")
plt.ylabel("Это ось Y")
plt.xlabel(r"Это ось X, $F(x) = \int f(x) dx + С$")
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