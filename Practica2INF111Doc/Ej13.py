n = int(input())
L = [0] * n
L1 = [0] * n
for i in range(n):
    L[i] = int(input())
aux = 0
for j in range(n):
    L1[j] = L[j] + aux
    aux = L1[j]
print(L)
print(L1)