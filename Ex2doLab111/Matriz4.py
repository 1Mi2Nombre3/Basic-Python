import numpy as np

n = int(input())
matriz = np.zeros((n, n))

col = n
lin = n
N = 1
a = 0
b = 1

for i in range(lin):
    for j in range(col):
        matriz[i, j] = N
        N = N + 1
    for k in range(b, lin):
        matriz[k, col-1] = N
        N = N + 1
    b = b + 1
    col = col - 1
print(matriz)