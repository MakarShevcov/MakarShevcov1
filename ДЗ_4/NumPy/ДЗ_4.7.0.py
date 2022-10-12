import numpy as np
a = []
for i in range(1,100):
    a += [i]
a = np.array(a, float)
b = a[::3]
b = b.reshape(11, 3)
p = b.T
p = p[::2]
x = []
for i in range(2):
    p[i][1] = p[i][4]
    p[i][2] = p[i][8]
    x += [p[i][:3]]
print(np.array(x))
