import sys

for datos in sys.stdin:
    n = int(datos)
    while n < 0 or n > 100:
        n = datos
    a = 1
    b = 1
    y = ""
    for i in range(1, n + 1):
        if i == n:
            y = y + str(a * b)
        else:
            y = y + str(a * b) + " "
        a = a + 1
        b = b + 2
    print(y)
