import numpy as np
a = []
for i in range(1,100):
    a += [i]
a = np.array(a, float)
b = a[::3]
b = b.reshape(11, 3)
sum0 = b.sum(axis=1)
print(sum0)
