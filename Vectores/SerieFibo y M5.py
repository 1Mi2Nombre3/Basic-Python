def fib(n):
    a = 0
    b = 1
    for i in range(n):
        a = a + b
        b = a - b
        print(b, end=" ")


def m5(n):
    a = 5
    b = 0
    for i in range(n):
        b = a + b
        print(b, end=" ")


n = int(input())
while n <= 0:
    n = int(input())
if n % 2 == 0:
    fib(n)
else:
    m5(n)
