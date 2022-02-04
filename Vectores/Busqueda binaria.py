def BusBin(a):
    n = len(a)
    x = int(input())
    li = 0
    ls = n - 1
    ce = (li + ls) // 2
    while x != a[ce] and li <= ls:
        if x > a[ce]:
            li = ce + 1
        else:
            ls = ce - 1
        ce = (li + ls) // 2
    if x == a[ce]:
        print("encontrado posicion", ce)
    else:
        print("no encontrado")


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


a = [1, 2, 3, 52, 5, 6, 7, 8, 9, 10, 21, 7, 124, 788, 1234, 6, 371, 61, 317, 1]
print(a)
OrdenNum(a)
print(a)
BusBin(a)
