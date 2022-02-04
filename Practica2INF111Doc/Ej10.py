import math

x = int(input())
cd = int(math.log10(x)) + 1

y = ""
y1 = ""
c = 0
c1 = 0

while x != 0:
    d = x // int(math.pow(10, cd - 1))
    x = x % int(math.pow(10, cd - 1))
    if d % 2 == 0:
        c = c + 1
        y = y + str(d)
    else:
        c1 = c1 + 1
        y1 = y1 + str(d)
    cd = cd - 1

LPar = [0] * c
LImpar = [0] * c1
for i in range(len(LImpar)):
    LImpar[i] = int(y1[i])
for j in range(len(LPar)):
    LPar[j] = int(y[j])

print(LImpar)
print(LPar)
