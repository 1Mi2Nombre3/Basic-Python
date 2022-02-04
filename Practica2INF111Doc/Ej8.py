import math

x = int(input())
cd = int(math.log10(x)) + 1
c = 0
y = ""

while x != 0:
    d = x // int(math.pow(10, cd - 1))
    x = x % int(math.pow(10, cd - 1))
    cd = cd - 1
    if d % 2 == 0:
        c = c + 1
        y = y + str(d)

L = [0] * c
for i in range(len(y)):
    L[i] = int(y[i])

print(L)
