import sys

for datos in sys.stdin:
    n, k = map(int, datos.split(" "))
    a = 0
    b = 0

    for i in range(n + 1):
        a = ((i + k) / (2 + i + k))
        b = a + b

    b = int(b)
    print(b)