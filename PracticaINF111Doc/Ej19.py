#Dado un x>100, mostrar el primer y ultimo dígito. Ejem: si x=47736 --> Mostrar 4 y 6
import math
x = int(input("Valor de x: "))
while x<=100:
    x = int(input("Valor de x: "))
cd=int(math.log10(x))+1
a=cd
while x!=0:
    d=x//int(math.pow(10, cd-1))
    x=x%int(math.pow(10, cd-1))
    if cd==a:
        print(d,end=" ")
    cd = cd - 1
    if cd==0:
        print(d,end=" ")