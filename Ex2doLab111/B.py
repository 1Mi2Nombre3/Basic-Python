import math

n = int(input())
cd = int(math.log10(n)+1)
while cd < 4:
    n = int(input())
    cd = int(math.log10(n) + 1)

L = []
L1 = [0] * cd
cd1 = cd
while n != 0:
    d = n // int(math.pow(10, cd - 1))
    n = n % int(math.pow(10, cd - 1))
    cd = cd - 1
    L.append(d)
aux = L[0]

for i in range(len(L)):
    if i < cd1-1:
        if L[i] % 2 == 0:
            if L[i+1] % 2 == 0:
                L1[i+1] = L[i]
            else:
                aux = L[i]
                L1[i+1] = L[i+1]
        else:
            L1[i+1] = aux
    else:
        L1[0] = aux
y = ""
for i in L1:
    y = y + str(i)
print(int(y))
