with open("input.txt", "r", encoding="utf-8") as f:
    a = list(map(lambda x: x.rstrip().split(), f.readlines()))
y1 = ''
for i in range(9, 12):
    k = 0
    c = 0
    for j in range(len(a)):
        if int(a[j][2]) == i:
            k += float(a[j][3])
            c += 1
    print(k / c, end = ' ')
