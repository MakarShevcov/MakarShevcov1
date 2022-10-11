import numpy as np
l = np.random.rand(120)
l1 = l.reshape((12, 10))
sum0 = l1.sum(axis=0)
sum1 = l1.sum(axis=1)
std0 = l1.std(axis=0)
std1 = l1.std(axis=1)
sred0 = sum0/l1.shape[0]
sred1 = sum1/l1.shape[1]
print(sum0, '\n'), print(sum1, '\n'), print(std0, '\n'), print(std1, '\n'), print(sred0, '\n'), print(sred1, '\n')
