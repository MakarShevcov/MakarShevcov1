with open("input.txt", "r") as f:
    a = f.readlines()
    a[len(a)-1] += "\n"
    a1 = a[::-1]
k = ''
for i in range(len(a1)):
    k += a1[i]
with open("output.txt", "w") as f:
    f.writelines(k)
