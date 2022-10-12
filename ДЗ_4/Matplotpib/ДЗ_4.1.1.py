import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.size'] = 16
plt.figure(figsize=(7,7))
x = np.arange(0, 100, 10)
y = np.sin(x)
mu = np.sin(x)
sigma = np.abs(mu)**0.5
plt.legend()
plt.savefig('example.png')
plt.plot(x,y, 'r.', label='Красные треугольники')
plt.show()
