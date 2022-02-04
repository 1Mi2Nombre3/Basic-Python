# inicio
a = input("Digite un número: ")
b = input("Digite un número: ")
print(a, b)

if a > b:
    print("El mayor es: ", a)
else:
    print("El mayor es: ", b)
# fin


#inicio
# Ordenar mediante el uso de condicionales tres numeros de manera descendente

a = input("Number 1: ")
b = input("Number 2: ")
c = input("Number 3: ")

if (a > b) and (b > c):
    print(a, b, c)
elif (a > c) and (c > b):
    print(a, c, b)
elif (b > a) and (a > c):
    print(b, a, c)
elif (b > c) and (c > a):
    print(b, c, a)
elif (c > a) and (a > b):
    print(c, a, b)
elif (c > a) and (b > a):
    print(c, b, a)
else:
    print("Error")
#fin