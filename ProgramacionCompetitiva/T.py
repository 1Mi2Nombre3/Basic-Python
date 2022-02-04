import math
import sys

for datos in sys.stdin:
    x, d = map(int, datos.split(" "))
    x1 = x
    cd = int(math.log10(x)) + 1
    cd1 = cd
    L = []
    y = ""
    while x1 != 0:
        d1 = x1 // int(math.pow(10, cd1 - 1))
        x1 = x1 % int(math.pow(10, cd1 - 1))
        cd1 = cd1 - 1
        L.append(d1)

    if max(L) != d:
        for i in range(len(L)):
            if L[i] == d:
                L[i] = max(L)
    else:
        max1 = max(L)
        L1=[]
        for i in range(len(L)):
            if L[i] != max1:
                L1.append(L[i])
        max1 = max(L1)
        for j in range(len(L)):
            if L[j] == d:
                L[j] = max1
    for i in L:
        y = y + str(i)
    print(int(y))
