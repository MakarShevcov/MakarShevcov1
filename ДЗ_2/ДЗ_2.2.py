with open("input.txt", "r") as f:
    a = f.readlines()
    a = list(map(lambda x: x.split(), a))
print(a)
b = int(input())
x = ''
for i in range(len(a)):
     x += str(i % b) + ' ' + str(a[i][0]) + "\n"
print(x)
with open("output.txt", "w") as f:
    f.writelines(x)

with open("input1.txt", "r") as f:
    a = f.readlines()
    a = list(map(lambda x: x.split(), a))
b = len(a)
print(a)
x = []
for i in range(len(a)):
     x += [a[i][0]]
print(x)
x1 = sorted(x, key = lambda i: -i[0] )
k = ''
for i in range(len(x1)):
    k += str(x1[i][0]) + ' ' + str(x1[i][1]) + "\n"
with open("output.txt", "w") as f:
    f.writelines(k)






with open("input1.txt", "r") as f:
    a = f.readlines()
    a = list(map(lambda x: x.split(), a))
b = len(a)
x = []
for i in range(len(a)):
     x += [[i % b, a[i]]]
x1 = sorted(x, key = lambda i: -i[0] )
n = []
for i in range(len(x1)):
    k = []
    for j in range(len(x1[i][1])):
        k += x1[i][1][j]
    n += [k]
print(n)
y1 = []
for i in range(len(n)):
    y = []
    for j in range(len(n[i])):
        y += [[j % len(n[i]), n[i][j]]]
    y1 += [y]
w = []
for i in range(len(y1)):
     y2 = sorted(y1[i], key = lambda x: -x[0] )
     w += [y2]
print(w)