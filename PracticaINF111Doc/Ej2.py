# Determinar si una persona estará habilitada para votar, dado su año de nacimiento.
# El año de nacimiento debe debe ser positivo.

AñodeNac=int(input("Ingrese año de nacimiento: "))
while AñodeNac<=0 or AñodeNac>=2021:
    AñodeNac=int(input("Ingrese su edad: "))

Año = 2021
edad=(Año-AñodeNac)

if edad >= 18:
    if edad >= 70:
        print("Tiene", edad, "años de edad, usted no esta habilitado")
    else:
        print("Tiene", edad, "años de edad, usted esta habilitado")
else:
    print("Tiene",edad,"años de edad, usted no esta habilitado")


