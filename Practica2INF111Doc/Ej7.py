def Esprimo(a):
    c = 0
    suma = 0
    for i in range(1, a + 1):
        if a % i == 0:
            c = c + 1
    if c == 2:
        suma = a
        return suma
    else:
        suma = 0
        return suma


n = int(input())
L = [0] * n
Prom = 0
for i in range(n):
    L[i] = int(input())

print(L)
for j in range(n):
    Prom = Prom + Esprimo(L[j])
print(Prom)
