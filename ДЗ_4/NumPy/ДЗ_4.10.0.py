import numpy as np
def exp(X, n):
    fact = 1
    Xtemp = np.eye(X.shape[0])
    s = np.eye(X.shape[0])
    for i in range(1, n+1):
        fact*=i
        Xtemp = Xtemp @ X
        s += Xtemp/fact
    return s
x = input().split(' ')
for i in range(len(x)):
    x[i] = int(x[i])
n = int(input())
x = np.array(x)
X = x.reshape(n,n)
print(exp(X, n))
