n = int(input())
a = [0] * n
b = [0] * n
c = [0] * n
for i in range(n):
    a[i] = input()
for j in range(n):
    b[j] = input()

for i in range(n):
    a[i] = a[i].upper()
    b[i] = b[i].lower()

    c[i] = a[i] + b[i]
print(c)