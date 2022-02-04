n = int(input())
a = []
for i in range(n):
    x = int(input())
    a.append(x)

Lpar = []
Limp = []

for i in a:
    if i % 2 == 0:
        Lpar.append(i)
    else:
        Limp.append(i)

lonP = len(Lpar)
lonI = len(Limp)
b = 0
for j in range(b,lonP):
    b = b + 1
    for k in range(lonP):
        if Lpar[j] < Lpar[k]:
            aux = Lpar[j]
            Lpar[j] = Lpar[k]
            Lpar[k] = aux
b = 0
for j in range(b, lonI):
    b = b + 1
    for k in range(lonI):
        if Limp[j] < Limp[k]:
            aux = Limp[j]
            Limp[j] = Limp[k]
            Limp[k] = aux
a = len(Lpar)
b = len(Limp)
while a > b:
    b = b + 1
while b > a:
    a = a + 1
c = a + b
L = []
a = len(Lpar)
b = len(Limp)
x = 0
y = 0
for i in range(c):
    if i % 2 == 0:
        if x < a:
            L.append(Lpar[x])
            x += 1
        else:
            if i + 1 != c:
                L.append(0)
    else:
        if y < b:
            L.append(Limp[y])
            y += 1
        else:
            if i + 1 != c:
                L.append(0)

lon = len(L)
for h in range(lon):
    if h != lon-1:
        print(L[h],end=" ")
    else:
        print(L[h],end="")
