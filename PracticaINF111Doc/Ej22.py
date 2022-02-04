#Dado un x>100, Mostrar los dígitos repetidos: Ejm: si X=47527734 -> Mostrar: 4,7

import math
x=int(input("Valor de x: "))
while x<=100:
    x = int(input("Valor de x: "))

cd = int(math.log10(x))+1
d2=0
cd2 = 0
while x!=0:
    c = 0
    d = x // int(math.pow(10, cd - 1))
    x = x % int(math.pow(10, cd - 1))
    y = x
    cd = cd - 1
    cd2 = cd
    while y!=0:
        d2 = y // int(math.pow(10, cd2 - 1))
        y = y % int(math.pow(10, cd2 - 1))
        cd2 = cd2 - 1
        if d==d2:
            c=c+1
            if c==1:
                print(d,end=" ")

