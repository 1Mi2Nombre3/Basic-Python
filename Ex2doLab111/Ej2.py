import numpy as np

n = int(input())
matriz = np.zeros((n, n))

Na = ((n ** 2) // 2) + 1
N = 1

a = 0
b = 1

c = 0
d = 1
cv = 0
for i in range(2):
    if cv == 0:
        for i in range(2):
            matriz[0, a] = N
            N += 1
            a += 1
        for j in range(2):
            matriz[b, 0] = N
            N += 1
            b += 1
        if c % 2 == 0:
            for k in range(c + 1, 0, -1):
                matriz[c+1, d] = N
                N += 1
        else:
            for li in range(c + 1, 0, -1):
                matriz[d, c+1] = N
                N += 1
        c += 1
        d += 1
        cv = 1
    elif cv == 1:
        for i in range(2):
            matriz[0, a] = N
            N += 1
            a += 1
        if c % 2 == 0:
            for k in range(c + 1, 0, -1):
                matriz[c+1, d] = N
                N += 1
        else:
            for li in range(c + 1, 0, -1):
                matriz[d, c+1] = N
                N += 1
        for j in range(2):
            matriz[b, 0] = N
            N += 1
            b += 1
    elif cv == 2:
        if c % 2 == 0:
            for k in range(c + 1, 0, -1):
                matriz[c, d] = N
                N += 1
                cv = 1
        else:
            for li in range(c + 1, 0, -1):
                matriz[d, c] = N
                N += 1
        c += 1
        d += 1
print(matriz)