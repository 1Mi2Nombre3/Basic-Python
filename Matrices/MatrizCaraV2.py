def leerM(a, n, m):
    for i in range(n):
        b = [0] * m
        for j in range(m):
            b[j] = 0
        a[i] = b


def mostrarM(a, n, m):
    for i in range(n):
        for j in range(m):
            if j != m - 1:
                print(a[i][j], end=" ")
            else:
                print(a[i][j], end="")
        print()


n = int(input())
m = n
l = [0] * n
leerM(l, n, m)
G = n // 2
a = G
b = G + 1
N = 1
for i in range(1):
    for j in range(b-1, a, -1):
        print(j)