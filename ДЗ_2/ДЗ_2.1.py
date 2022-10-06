with open("input.txt", "r") as f:
    a = f.readlines()
    a = list(map(lambda x: x.split(), a))
    a1 = []
    for i in range(len(a)):
        for j in range(len(a[i])):
            a1 += [list(a[i][j])]
b = sorted(a1, key=lambda x: -len(x))
c = []
for i in range(len(b[0])):
    k = 0
    for j in range(len(b)):
        if i < len(b[j]):
            k += int(b[j][i])
    c += str(k) + ' '
with open("output.txt", "w") as f:
    f.writelines(c)
