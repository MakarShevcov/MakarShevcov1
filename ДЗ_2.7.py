with open("input.txt", "r") as f:
    a = f.readlines()
    a = list(map(lambda x: x.split(), a))
b = len(a)
x = []
for i in range(len(a)):
     x += [[i % b, a[i]]]
x1 = sorted(x, key = lambda i: -i[0] )
k = ''
for i in range(len(x1)):
    for j in range(len(x1[i][1])):
        k += str(x1[i][1][j]) + ' '
    k += "\n"
with open("output.txt", "w") as f:
    f.writelines(k)
