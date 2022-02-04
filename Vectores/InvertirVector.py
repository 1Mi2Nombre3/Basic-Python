def InverVec(L):
    lon = len(L)
    L1 = []
    for i in range(lon - 1, -1, -1):
        L1.append(L[i])
    print(L1)


L = [12, 64, 91]
InverVec(L)
