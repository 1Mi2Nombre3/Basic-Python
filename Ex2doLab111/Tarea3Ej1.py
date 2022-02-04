# La suma de los 3 numeros anteriores.
n = int(input())
a = 0
b = 0
c = 1
d = 1
res = 0

for i in range(1, n + 1):
    if i <= 2:
        print(0, end=" ")
    elif i <= 4:
        print(1, end=" ")
    else:
        res = a + b + c + d
        print(res, end=" ")
        a = b
        b = c
        c = d
        d = res