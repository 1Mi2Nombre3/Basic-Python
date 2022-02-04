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
a = [0] * n
s = 0
leerM(a, n, n)
mostrarM(a, n, n)
for i in range(n):
    for j in range(n):
        if i == j:
            s = s + a[i][j]
print(s)
