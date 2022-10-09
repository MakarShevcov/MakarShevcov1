a = input('напишите 3 слова: ')
a1 = a.split(' ')
m = []
for i in range(len(a1)):
    m += [set(a1[i])]
print(m[0] & m[1] & m[2])
