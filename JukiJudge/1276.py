n = int(input())
while n < 1 or n > 10 ** 12:
    n = int(input())
for i in range(1, n + 1):
    if n % i == 0:
        a = n // i
        print(i, a)
