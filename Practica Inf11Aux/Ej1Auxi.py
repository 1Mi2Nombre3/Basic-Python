import math


def RotIzq():
    aux = L1[0]
    o = len(L1)
    for iz in range(1, o):
        L1[iz - 1] = L1[iz]
    L1[o - 1] = aux
    return L1


def RotDer():
    p = len(L1)
    aux = L1[p - 1]
    for de in range(1, p):
        L1[p - de] = L1[p - (de + 1)]
    L1[0] = aux
    return L1


n, m, num = map(int, input().split())
cd = int(math.log10(num) + 1)
L = [0] * cd
lon = cd
y = 0
for i in range(cd):
    y = num // int(math.pow(10, cd - 1))
    num = num % int(math.pow(10, cd - 1))
    L[i] = y
    cd = cd - 1

# **********PARES********** #

for n1 in range(n):
    cd = 0
    for i in range(lon):
        if L[i] % 2 == 0:
            cd = cd + 1
    Ln = [0] * cd
    L1 = [0] * cd
    a = 0
    for i in range(lon):
        if L[i] % 2 == 0:
            L1[a] = L[i]
            Ln[a] = i
            a = a + 1
    print(L)   # Numero original
    print(Ln)  # Posiciones de los pares
    print(L1)  # Pares en una lista distinta
    L1 = RotIzq()  # Rotamos los pares a la izquierda (funcion)
    print(L1)
    b = 0
    for j in range(lon):
        if L[j] % 2 == 0:
            L[j] = L1[b]
            b = b + 1
    print(L)   # Nueva lista modificada
    print("__________________________________")

# **********IMPARES********** #

for m1 in range(m):
    cd = 0
    for i in range(lon):
        if L[i] % 2 != 0:
            cd = cd + 1
    Ln = [0] * cd
    L1 = [0] * cd
    a = 0
    for i in range(lon):
        if L[i] % 2 != 0:
            L1[a] = L[i]
            Ln[a] = i
            a = a + 1
    print(L)   # Numero original
    print(Ln)  # Posicion de los numeros impares
    print(L1)  # Impares en una lista distinta
    L1 = RotDer()  # Rotamos los impares a la derecha (funcion)
    print(L1)
    b = 0
    for j in range(lon):
        if L[j] % 2 != 0:
            L[j] = L1[b]
            b = b + 1
    print(L)  # Nueva lista modificada
    print("__________________________________")
for lis in L:
    print(lis, end="")
