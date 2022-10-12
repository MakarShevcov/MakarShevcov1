import numpy as np
a = []
for i in range(1,100):
    a += [i]
a = np.array(a, float)
b = a[::3]
b = b.reshape(11, 3)
c = np.array([[1], [0], [-1], [-2], [-3], [-4], [-5], [-6], [-7], [-8], [-9]])
p = c.T*b.T
x = []
for i in range(len(p)):
    x += [[sum(p[i])]]
print(np.array(x))
