x=1
may=0
c=0
L=[]
while x!=0:
    x=int(input())
    while x<0 or x>=10:
        print("no valido")
        x=int(input())
    if x>=may:
        may=x
    L.append(x)
for i in L:
    if may==i:
        c=c+1
print("El número mayor es:",may,"y se repite:",c)
