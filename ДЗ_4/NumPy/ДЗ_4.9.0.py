import numpy as np
def fibonacci_number(n: int):
    if n == 0:
        return [0]
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        c = 1
        k = 1
        a = [1, 1]
        for i in range(n-2):
            x = c+k
            a += [x]
            c = k
            k = x
    return a
def prime_number(j: int):
    if j == 1:
        return [2]
    a = [2]
    c = 1
    i = 3
    while c <= j-1:
        k = 0
        for t in range(2, i):
            if i % t == 0:
                k += 1
        if k == 0:
            a += [i]
            c += 1
        i += 1
    return a
y = int(input())
a = np.array(prime_number(y))
b = np.array(fibonacci_number(y))
print(a)
print(b)
n = 0
for i in range(len(a*b)):
    n += (a*b)[i]
print(n)
