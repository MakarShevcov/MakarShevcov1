n = int(input())
m = int(input())
k = [[(i*m) + j for j in range(m)] for i in range(n)]
print(k)