def InverNum(x):
    import math
    cd = int(math.log10(x) + 1)
    y = ""
    x = str(x)
    for j in range(cd - 1, -1, -1):
        y = y + x[j]
    L1[i] = int(y)


def Center(x):
    x = str(x)
    lon = len(x)
    x1 = ""
    if lon % 2 == 0 or lon == 1:
        x1 = ""
        cv = 0
        while lon >= 3:
            a = lon // 2
            x1 = x1 + x[a - 1]
            x1 = x1 + x[a]
            lon = len(x1)
            cv = 1
        if cv == 1:
            L2[i] = x1
        else:
            L2[i] = x
    else:
        a = lon // 2
        x = x[a]
        L2[i] = x


n = int(input("tamaño: "))
L = [0] * n
L1 = [0] * n
L2 = [0] * n
for i in range(n):
    L[i] = int(input())
    L1[i] = L[i]
    L2[i] = L[i]
    InverNum(L1[i])
    Center(L2[i])

print(L)
print(L1)
print(L2)
