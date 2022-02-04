### MODULO ###
import math


def leerMP(a, n, m):
    s = 2
    for i in range(n):
        b = [0] * m
        for j in range(m):
            b[j] = s
            s = s + 2
        a[i] = b


def mostrarM(a, n, m):
    for i in range(n):
        for j in range(m):
            if j != m - 1:
                print(a[i][j], end=" ")
            else:
                print(a[i][j], end="")
        print()


def SumaFilas(a, b, n, m):
    for i in range(n):
        s = 0
        for j in range(m):
            s = s + a[i][j]
        b[i] = s
        cd = int(math.log10(b[i]) + 1)
        while cd != 0:
            d = b[i] // int(math.pow(10, cd - 1))
            b[i] = b[i] % int(math.pow(10, cd - 1))
            print(d, end=" ")
            cd = cd - 1
        print()


### MAIN ###

n = int(input())
m = int(input())
a = [0] * n
leerMP(a, n, m)
mostrarM(a, n, m)
print()
b = [0] * n
SumaFilas(a, b, n, m)
