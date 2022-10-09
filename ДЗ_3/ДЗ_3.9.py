x = input()
x1 = x.split(' ')
d = dict()
s = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
p = 100/len(x) // 1
for j in range(len(x1)):
    for i in x1[j]:
        if i in s:
            continue
        elif i in d:
            d[i] += p
        else:
            d[i] = p
print(d)
