def fib(x):
    a = 1
    b = 0
    for i in range(n):
        a = a + b
        b = a - b
        print(b, end=" ")


def M3(x):
    a = 0
    for i in range(x):
        a += 3
        print(a,end=" ")


def Pot(a, b):
    import math
    c = math.pow(a, 2) + math.pow(b, 2)
    return c


def Primo(x):
    c = 0
    for i in range(1, x + 1):
        if x % i == 0:
            c = c + 1
    if c == 2:
        print("Si es primo", x)
    else:
        print("No es primo", x)

print("MENU")
print("""1. SERIE FIBONACCI
2. SERIE MULTIPLOS DE 3
3. SUMA DE POTENCIAS DE 2
4. VERIFICAR PRIMO
5. SALIR
ELIJA LA OPCION: """)
Ind = int(input())

if Ind == 1:
    n = int(input("tamaño de la serie: "))
    fib(n)
elif Ind == 2:
    n = int(input("tamaño de la serie: "))
    M3(n)
elif Ind == 3:
    a = int(input("Number 1: "))
    b = int(input("Number 2: "))
    print(Pot(a, b))
elif Ind == 4:
    x = int(input("Primo: "))
    Primo(x)
elif Ind == 5:
    print("Gracias.")
else:
    print("ERROR")