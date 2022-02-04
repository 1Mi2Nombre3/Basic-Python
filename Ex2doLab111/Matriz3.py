import numpy as np

n = int(input())
matriz = np.zeros((n, n))

a = 1
b = 0
for i in range(n):
    if i % 2 == 0:
        for j in range(n):
            matriz[j, b] = a
            a += 1
    else:
        for k in range(n - 1, -1, -1):
            matriz[k, b] = a
            a += 1
    b = b + 1
print(matriz)
