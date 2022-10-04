with open("input.txt", "r") as f:
    a = f.readlines()
    a = list(map(lambda x: x.split(), a))
print(a[0][1])
b = []
for i in range(len(a)):
    for j in range(len(a[i])):
        b += [a[i][j]]
import collections
from collections import Counter
n = int(input('n = '))
m = collections.Counter(b).most_common(n)
for i in m:
    print(i[0], end = ", ")