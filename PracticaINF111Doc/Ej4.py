#Ej4
Prod1=int(input("Precio del 1er producto: "))
while Prod1 <= 0:
    Prod1 = int(input("Precio del 1er producto: "))
Prod2=int(input("Precio del 2do producto: "))
while Prod2 <= 0:
    Prod2 = int(input("Precio del 2do producto: "))

if Prod1 >= 300:
    Monto1 = Prod1 - (Prod1*20)/100
elif Prod1 < 300 and Prod1 >= 200:
    Monto1 = Prod1 - (Prod1*15)/100
elif Prod1 < 200 and Prod1 >= 100:
    Monto1 = Prod1 - (Prod1*7)/100
else:
    Monto1 = Prod1

print(Monto1)

if Prod2 >= 300:
    Monto2 = Prod2 - (Prod2*20)/100
elif Prod2 < 300 and Prod2 >= 200:
    Monto2 = Prod2 - (Prod2*15)/100
elif Prod2 < 200 and Prod2 >= 100:
    Monto2 = Prod2 - (Prod2*7)/100
else:
    Monto2 = Prod2

print(Monto2)
CobroT = Monto1+Monto2

print("El monto total a cobrar es de: ",CobroT,"Bs")


