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


def Matriz(a, n, m):
    for i in range(n):
        for j in range(n):
            if i >= j and (i + j) < n:
                a[i][j] = 1
        for k in range(m):
            if k >= i and (i + k) >= n-1:
                a[i][k] = 1


### MAIN ###

n = int(input())
while n % 2 == 0 or n < 3:
    n = int(input())
m = n
a = [0] * n
leerM(a, n, m)
Matriz(a, n, m)
mostrarM(a, n, m)
