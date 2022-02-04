import sys

for datos in sys.stdin:
    n = datos
    n = int(n)
    den = 2
    num = 4
    SerIn = 3
    a = 1
    b = 0
    c = a + b
    res = 0
    for i in range(n):
        res = res + (num / den)
        num = num + SerIn
        SerIn = SerIn + c
        den = den + 2
        a = b
        b = c
        c = a + b
    print(format(res, '.4f'))
