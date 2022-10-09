a = [i for i in range(1, 27)]
b = [chr(i) for i in range(ord('a'), ord('z')+1)]
print(dict(zip(a, b)))
