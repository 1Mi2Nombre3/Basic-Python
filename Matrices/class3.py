### MODULO ###

def leerM(a, n, m):
    for i in range(n):
        b = [0] * m
        for j in range(m):
            b[j] = 0
        a[i] = b


def mostrarM(a, n, m):
    for i in range(n):
        print(a[i])


### MAIN ###

n = int(input())
m = int(input())
a = [0] * n
leerM(a, n, m)
Nat = 1
for i in range(n):
    if i % 2 == 0:
        for j in range(m):
            a[i][j] = Nat
            Nat = Nat + 1
    else:
        for k in range(m - 1, -1, -1):
            a[i][k] = Nat
            Nat = Nat + 1
mostrarM(a, n, m)
