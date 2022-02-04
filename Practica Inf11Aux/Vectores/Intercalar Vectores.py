n = int(input("Vector 1: "))
L = [0] * n
for i in range(n):
    L[i] = input()

n1 = int(input("Vector 2: "))
L1 = [0] * n1
for i in range(n1):
    L1[i] = input()

n2 = n + n1
L2 = [0] * n2
a = 0
b = 0
c = 0
d = 0
for i in range(n2):
    if i%2 == 0:
        if a <= n-1:
            L2[i] = L[a]
        else:
            c = 1
        a = a + 1
    else:
        if b <= n1-1:
            L2[i] = L1[b]
        else:
            d = 1
        b = b + 1

    if c == 1:
        L2[i] = L1[b]
    if d == 1:
        L2[i] = L[a]

    print(L2)