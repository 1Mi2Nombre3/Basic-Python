def RotDer(a):
    n = len(L1)
    aux = L1[n - 1]
    for i in range(1, n):
        L1[n - i] = L1[n - (i + 1)]
    L1[0] = aux


def RotIzq(b):
    aux = L2[0]
    n = len(L2)
    for i in range(1, n):
        L2[i - 1] = L2[i]
    L2[n - 1] = aux


n = int(input())
while n % 2 != 0:
    n = int(input())

n1 = n // 2
L1 = [0] * n1
L2 = [0] * n1
for i in range(n1):
    L1[i] = input()
for j in range(n1):
    L2[j] = input()

RotDer(L1)
RotIzq(L2)
L3 = L1 + L2
print(L3)
