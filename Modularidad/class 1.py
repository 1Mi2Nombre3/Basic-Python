# creo una funcion para factorial
import math


def fac(a):
    b = 1
    for j in range(1, a + 1):
        b = b * j
    return b


S = int(input())
x = int(input())
y = int(input())
res = 0
for i in range(1, S + 1):
    res = res + (math.pow(x, fac(i * 2) - 1) / (fac(i * y)))
print(res)
