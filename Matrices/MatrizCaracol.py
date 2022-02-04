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
a = 0
b = n - 1
N = 1

for i in range(len(l)):
    for j in range(a, b + 1):
        l[a][j] = N
        N = N + 1
    for j in range(a + 1, b + 1):
        l[j][b] = N
        N = N + 1
    for j in range(b - 1, a-1, -1):
        l[b][j] = N
        N = N + 1
    for j in range(b - 1, a, -1):
        l[j][a] = N
        N = N + 1
    a = a + 1
    b = b - 1
mostrarM(l, n, m)
