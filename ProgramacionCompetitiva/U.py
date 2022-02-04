import sys

for datos in sys.stdin:
    x, t, z = map(int, datos.split(" "))
    x1 = ""
    x2 = ""
    x = str(x)
    a = (len(x) - t)
    a1 = a
    for i in range(t):
        x1 = x1 + x[a]
        a = a + 1

    L = []
    for j in x1:
        L.append(j)

    if int(x) % 2 == 0:
        for par in range(z):
            n = len(L)
            aux = L[n - 1]
            for i in range(1, n):
                L[n - i] = L[n - (i + 1)]
            L[0] = aux
    else:
        for im in range(z):
            aux = L[0]
            n = len(L)
            for i in range(1, n):
                L[i - 1] = L[i]
            L[n - 1] = aux

    for i in range(a1):
        x2 = x2 + x[i]
    for j in L:
        x2 = x2 + j
    print(x2)
