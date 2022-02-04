n = int(input())
L = [0] * n

a = 0
b = 1

c = 0
p = 2
d = 2
for i in range(1, len(L) + 1):
    if i % 2 == 0:
        a = a + b
        b = a - b
        L[i - 1] = b
    else:
        N = 0
        while N == 0:
            if p % d == 0:
                if p == d:
                    L[i - 1] = p
                    N = 1
                    c = c + 1
                d = 2
                p = p + 1
            else:
                d = d + 1
print(L)
