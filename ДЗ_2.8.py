with open("input.txt", "r") as f:
    a = f.read()
    a1 = a[::-1]
with open("output.txt", "w") as f:
    f.writelines(a1)
