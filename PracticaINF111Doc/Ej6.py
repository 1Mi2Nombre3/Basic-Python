#Hallar el mayor y el menor de 5 números ingresados desde teclado.

a=int(input("Num1: "))
b=int(input("Num2: "))
c=int(input("Num3: "))
d=int(input("Num4: "))
e=int(input("Num5: "))

may=a
men=a

if b>may:
    may=b
if c>may:
    may=c
if d>may:
    may=d
if e>may:
    may=e

if b<men:
    men=b
if c<men:
    men=c
if d<men:
    men=d
if e<men:
    men=e

print(may,men)


