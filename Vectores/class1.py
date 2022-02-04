# Declaration de vectors

n = int(input())
while n <= 0:
    n = int(input())
a = [0] * n   # tamaño de a
for i in range(0, n):
    a[i] = int(input())
for j in range(0, n):
    print(a[j], end="-")

