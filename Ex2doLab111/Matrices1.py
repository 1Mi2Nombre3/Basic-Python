import numpy as np

n = int(input())
matriz = np.zeros((n, n))
print(matriz)
print()
for i in range(n):
    matriz[i, 0] = 1
print(matriz)
print()
for i in range(n):
    matriz[i, i] = 1
print(matriz)
print()
a = 1
for i in range(n):
    for j in range(n):
        matriz[i, j] = a
        a = a + 1
print(matriz)
print()
a = 0
b = 1

import numpy as np
n = int(input())
matriz = np.zeros((n, n))
for i in range(n):
    for j in range(a, n):
        matriz[i, j] = b
        b = b + 1
    a = a + 1
print(matriz)