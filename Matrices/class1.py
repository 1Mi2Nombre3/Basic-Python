### MODULO ###

def leerM(a, n, m):
    for i in range(n):
        b = [0] * m
        for j in range(m):
            b[j] = int(input())
        a[i] = b


def mostrarM(a, n, m):
    for i in range(n):
        print(a[i])


### MAIN ###

n = int(input())
m = int(input())
a = [0] * n
leerM(a, n, m)
mostrarM(a, n, m)
