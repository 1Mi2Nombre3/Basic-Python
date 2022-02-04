n, m = map(int, input().split())
a = [0] * n
for i in range(n):
    b = [0] * m
    for j in range(m):
        b[j] = 0
    a[i] = b

N = 1
cv = 0
cv1 = 0

for i in range(n):
    for j in range(m):
        if i % 2 == 0:
            if cv == 0:
                a[i][1] = 1
                a[i][4] = 1
            else:
                a[i][3] = 1
        else:
            if cv1 == 0:
                if j == 2:
                    a[i][j] = N
                    N = N ** 2
                    cv1 = 1
                else:
                    a[i][j] = N
                    N = N * 2
                    cv = 1
            else:
                a[i][j] = N
                N = N * 2

for i in range(n):
    for j in range(m):
        if j != m - 1:
            print(a[i][j], end=" ")
        else:
            print(a[i][j], end="")
    print()
