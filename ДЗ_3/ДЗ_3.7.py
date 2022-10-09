a = [i for i in range(1, 27)]
b = [chr(i) for i in range(ord('a'), ord('z')+1)]
d = dict(zip(b, a))
x = input('введите слово: ')
m = list(set(x))
k = 0
for i in range(len(m)):
    for j in m[i]:
        k += d[j]
print('сумма: ', k, end = ' ')
