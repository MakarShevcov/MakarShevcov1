n = int(input())
x = []
y = []
for i in range(n):
    a = input('Введите пару синонимов: ').split(' ')
    x += [a[0]]
    y += [a[1]]
d1 = dict(zip(x, y))
d2 = dict(zip(y, x))
while True:
    w = input()
    if w in x:
        print(d1[w])
    elif w in y:
        print(d2[w])
    else:
        print('NO')
