import math


def Men(a1):
    aux = a1[0]
    for i in a1:
        if i <= aux:
            aux = i
    return aux


x = int(input())
cd = int(math.log10(x)) + 1
a = [0] * cd
b = 0

while x != 0:
    d = x // int(math.pow(10, cd - 1))
    x = x % int(math.pow(10, cd - 1))
    cd = cd - 1
    a[b] = d
    b = b + 1
print(a)
print(Men(a))
