import numpy as np
l = np.random.rand(120)
l1 = l.reshape((12, 10))
max0 = l1.max(axis=0)
min0 = l1.min(axis=0)
print(max0, '\n'), print(min0, '\n')
