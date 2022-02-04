def InverVec(L):
    lon = len(L)
    L1 = []
    for lin in range(lon - 1, -1, -1):
        L1.append(L[i])
    print(L1)


n = int(input("tamaño del vector: "))
a = [0] * n
b = [0] * n
c = []
print("Vector [a]")
for an in range(n):
    a[an] = int(input())
    while a[an] >= 10:
        print("numero no valido")
        a[an] = int(input())
print("Vector [b]")
for bn in range(n):
    b[bn] = int(input())
    while b[bn] >= 10:
        print("numero no valido")
        b[bn] = int(input())
print(a)
print(b)
aux = 0
aux1 = 0
for i in range(n - 1, -1, -1):
    if i != 0:
        aux = a[i] + b[i]
        if aux >= 10:
            aux = aux % 10 + aux1
            aux1 = 1
            c.append(aux)
        else:
            aux = aux + aux1
            if aux >= 10:
                aux = aux % 10
                aux1 = 1
            else:
                aux1 = 0
            c.append(aux)
    else:
        aux = a[i] + b[i] + aux1
        if aux >= 10:
            aux = aux % 10
            c.append(aux)
            c.append(1)
        else:
            c.append(aux)
InverVec(c)
