n = int(input())
m = int(input())
def f(x, y):
    if x == y:
        return 0
    elif x > y:
        return 2
    else:
        return 1
k = [[f(i,j) for j in range(m)] for i in range(n)]
print(k)