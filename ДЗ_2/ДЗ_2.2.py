with open("input.txt", "r") as f:
    a = f.readlines()
    a = list(map(lambda x: x.split(), a))
b = int(input())
x = ''
for i in range(len(a)):
     x += str(i % b) + ' ' + str(a[i][0]) + "\n"
with open("output.txt", "w") as f:
    f.writelines(x)
