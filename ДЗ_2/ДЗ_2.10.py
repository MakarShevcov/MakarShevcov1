with open("input.txt", "r", encoding="utf-8") as f:
    a = list(map(lambda x: x.rstrip().split(), f.readlines()))
y = []
for i in range(len(a)):
    if int(a[i][3]) > 74:
        if int(a[i][2]) in y:
            continue
        else:
            y += [int(a[i][2])]
y = sorted(y,key = lambda x: x)
for i in range(len(y)):
    print(y[i], end = ' ')
