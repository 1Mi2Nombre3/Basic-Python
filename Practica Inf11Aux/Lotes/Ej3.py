#Dado un lote, determinar cuál es el máximo número de pares positivos consecutivos de ese lote.
x=0
c=0
may=0

while x!=-9999:
    c=0
    x = int(input())
    while x < (-10 ** 6) or x > (10 ** 6):
        x = int(input())

    while x>0 and x%2==0 and x!=-9999:
        c=c+1
        x = int(input())
        while x < (-10 ** 6) or x > (10 ** 6):
            x = int(input())
        if c>=may:
            may=c
print(may)



