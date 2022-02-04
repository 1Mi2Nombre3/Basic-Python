import numpy as np

n = int(input())
matriz = np.zeros((n, n))

N = 1
a = 0
for i in range(2):
    matriz[0, a] = N
    N += 1
    a += 1
print(matriz)
