a = input('напишите несколько чисел: ')
a1 = a.split(' ')
m = []
M = {'0','1','2','3','4','5','6','7','8','9'}
for i in range(len(a1)):
    m += [set(a1[i])]
j = 0
while j < len(m):
    M &= m[j]
    j += 1
print(M)
