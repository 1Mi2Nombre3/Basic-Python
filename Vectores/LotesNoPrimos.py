def Noprimo(a):
    for i in L:
        c = 0
        for j in range(1, i + 1):
            if i % j == 0:
                c = c + 1
        if c != 2:
            print(i, end=" ")


n = int(input())
while n <= 0:
    n = int(input())
L = [0] * n
for i in range(n):
    L[i] = int(input())

Noprimo(L)