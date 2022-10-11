import numpy as np
l = np.random.rand(120)
l1 = l.reshape((12, 10))
max1 = l1.argmax(axis=1)
min1 = l1.argmin(axis=1)
print(max1, '\n'), print(min1, '\n')
