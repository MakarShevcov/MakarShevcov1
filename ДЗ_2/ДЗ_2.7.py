with open("input.txt", "r", encoding="utf-8") as f:
    a = list(map(lambda x: x.rstrip().split(), f.readlines()))
y1 = ''
for i in range(9, 12):
    k = []
    for j in range(len(a)):
        if int(a[j][2]) == i:
            k += [int(a[j][3])]
    y = sorted(k,key = lambda x: -x)
    y1 += str(y[0]) + ' '
with open("output.txt", "w") as f:
    f.writelines(y1)    