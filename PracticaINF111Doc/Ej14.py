#Generar la siguiente serie: Si N=20 -> 20,15,10,5,0

n=int(input("N: "))
while n<=0:
    n = int(input("N: "))

for i in range(n,-1,-5):
    print(i,end=" ")
    if i==1 or i==2 or i==3 or i==4:
        print(0,end=" ")
