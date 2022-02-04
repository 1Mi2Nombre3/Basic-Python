def RotIzq(lan):
    aux = L1[0]
    n1 = len(L1)
    for i1 in range(1, n1):
        L1[i1 - 1] = L1[i1]
    L1[n1 - 1] = aux


n = int(input("lon: "))
K = int(input("k: "))

L = [0] * n
for i in range(n):
    L[i] = int(input())
print(L)

a = n // K
a1 = n - (a * K)
a2 = K * a
b = 0
L2 = []

for i in range(a):
    L1 = [0] * K
    for j in range(K):
        L1[j] = L[b]
        b = b + 1
    RotIzq(L1)
    L2 = L2 + L1

L1 = [0] * a1
if len(L1) > 0:
    for l1 in range(a1):
        L1[l1] = L[a2]
        a2 = a2 + 1
    RotIzq(L1)
L2 = L2 + L1
print(L2)