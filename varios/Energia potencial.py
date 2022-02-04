m = int(input("Da el valor de la masa: "))
while m <= 0:
    m = int(input("Ingrese un numero valido: "))

h = int(input("Da el valor de la altura: "))
while h < 0:
    h = int(input("Ingrese un numero valido: "))

Ep = m*h*9.81
print("El resultado de su energia potencial es: ", Ep)
