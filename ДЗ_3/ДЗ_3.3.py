a = input('напишите несколько слов: ')
a1 = a.split(' ')
m = []
M = set()
for i in range(len(a1)):
    m += [set(a1[i])]
for i in range(len(m)):
    M |= m[i]
for i in range(len(m)):
    M &= m[i]
print(M)
