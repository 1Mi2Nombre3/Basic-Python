n = int(input())
while n <= 0 or n > 10 ** 4:
    n = int(input())
a = 1
b = 1
c = 1
res = 0
d = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        b = a
        a = a + (a * -2)
    else:
        if a <= 0:
            a = b
            a = a + 2
    c = c + a
    d = d + 1
    if d == 1:
        print(c, end=" ")
    elif d % 2 == 0:
        c1 = (c * -2) + c
        print("-", c1, end=" ")
    else:
        print("+", c, end=" ")
    a = a + 2
    res = res + c
print("=", res)
