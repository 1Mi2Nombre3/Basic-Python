def RotDer(rot):
    n = len(L)
    aux = L[n - 1]
    for i in range(1, n):
        L[n - i] = L[n - (i + 1)]
    L[0] = aux
    return L


n = int(input())
L = [0] * n
for i in range(n):
    L[i] = input()

print(L)
print(RotDer(L))
