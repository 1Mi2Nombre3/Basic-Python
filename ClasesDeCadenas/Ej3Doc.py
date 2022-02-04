#dada una cadena, buscar o contar cuantas veces aparece el caracter x ingresado desde teclado
cad1 = input()
x = input()
x1 = len(x)
c = 0
while x1 > 1:
    x = input()
    x1 = len(x)
for i in cad1:
    if x == i:
        c += 1
print(c)