# 2. dado un vector ingresado desde teclado, mostrar el vector original y los elementos pares.
n = int(input())
while n <= 0:
    n = int(input())
a = [0] * n

for i in range(n):
    a[i] = int(input())

for i in range(n):
    print(a[i], end=" ")
print()

for i in range(n):
    if a[i] % 2 == 0:
        print(a[i], end=" ")
