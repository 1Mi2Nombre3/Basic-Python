def OrdenNum(L):
    lon = len(L)
    b = 0
    for j in range(lon):
        b = b + 1
        for k in range(b, lon):
            if L[j] > L[k]:
                aux = L[j]
                L[j] = L[k]
                L[k] = aux


L = [5, 3, 2, 7, 6, 56, 1, 26, 1, 67, 1, 12, 42, 1, 0]
print(L)
OrdenNum(L)
print(L)
