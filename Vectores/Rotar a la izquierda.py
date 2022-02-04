def RotIzq(lan):
    aux = L[0]
    n = len(L)
    for i in range(1, n):
        L[i - 1] = L[i]
    L[n - 1] = aux
    return L


n = int(input())
L = [0] * n
for i in range(n):
    L[i] = input()

print(L)
print(RotIzq(L))
