# Hallar el factorial de los números comprendidos en el rango [a..b], donde a < b
fac=1
a=int(input("Rango1: "))
b=int(input("Rango2: "))
while a>b:
    a = int(input("Rango1: "))
    b = int(input("Rango2: "))

for i in range (a,b+1):
    for j in range(1,i+1):
        fac=fac*j
    print(fac,end=" ")
    fac=1