n = int(input())
while n <= 0:
    n = int(input())

if n%2 == 0 and n%3 == 0:
    print(n, "es divisible entre 2 y 3.")
elif n%2 == 0 or n%3 == 0:
        print(n, "es divisible entre 2 o 3.")
        print(n, "es divisible entre 2 o 3, pero no ambos.")
else:
    print(n, "no es divisible entre 2 y 3.")