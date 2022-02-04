#Dado un x>100, eliminar el digito más pequeño: Ejm: si X=47527734 -> Y=4757734
import math

x=int(input("Valor de x: "))
while x<=100:
    x = int(input("Valor de x: "))

cd = int(math.log10(x))+1
cd2=cd
men=9
y=x
a=0

while x!=0:
    d = x // int(math.pow(10, cd - 1))
    x = x % int(math.pow(10, cd - 1))
    if d<=men:
        men=d
    cd = cd - 1

while y!=0:
    d = y // int(math.pow(10, cd2 - 1))
    y = y % int(math.pow(10, cd2 - 1))
    if d!=men:
        print(d,end="")
    cd2=cd2-1


