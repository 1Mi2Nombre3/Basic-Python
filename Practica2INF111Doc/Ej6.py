def InverPares(x):
    import math
    cd = int(math.log10(x) + 1)
    y = ""

    if x % 2 == 0:
        x = str(x)
        for j in range(cd - 1, -1, -1):
            y = y + x[j]
        L[i] = int(y)
    else:
        return x


n = int(input())
L = [0] * n
for i in range(n):
    L[i] = int(input())
    InverPares(L[i])
print(L)
