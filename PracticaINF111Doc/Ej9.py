#Determinar si un año es bisiesto
a=int(input("Año: "))
while a<=0:
    a = int(input("Año: "))

if a % 400 == 0:
    print("si, bisiesto")
elif a % 100 == 0:
    print("no, bisiesto")
elif a % 4 == 0:
    print("si, bisiesto")
else:
    print("no,bisiesto")