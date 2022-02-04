def SeriePrimo(n):
    y = ""
    c = 1
    p = 2
    d = 2
    while c <= n:
        if p % d == 0:
            if p == d:
                y = y + str(p) + " "
                c = c + 1
            d = 2
            p = p + 1
        else:
            d = d + 1
    print(y)


n = int(input())
SeriePrimo(n)
