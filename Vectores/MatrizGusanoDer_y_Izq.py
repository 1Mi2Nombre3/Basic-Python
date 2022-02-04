# Matriz gusanito
# MODULOS #
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


def gusanitoM(a, n, m):
    s = 1
    for i in range(n):
        if i % 2 == 0:
            for j in range(m):
                a[i][j] = s
                s = s + 1
        else:
            for k in range(m - 1, -1, -1):
                a[i][k] = s
                s = s + 1
    # Para modificar de izquierda a derecha el for j = (m - 1, -1, -1):
    # y el for k = (m)


# MAIN #
n = int(input())
m = int(input())
a = [0] * n
leerM(a, n, m)
gusanitoM(a, n, m)
mostrarM(a, n, m)
