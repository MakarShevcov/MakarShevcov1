n = int(input())
def f(x, y):
    if x <= y:
        return y
    elif x >= y:
        return x
k = [[f(i,j) for j in range(n)] for i in range(n)]
print(k)