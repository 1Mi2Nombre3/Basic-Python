#Dado un lote de N números, mostrar los divisores de los impares

n=int(input("Lotes: "))
while n<=0:
    n=int(input("Lotes: "))
a=0
for i in range(n):
    x=int(input())
    while x<=0:
        x=int(input())
    a=x%2
    if a==1:
        for j in range(1,x+1):
            if x%j==0:
                print(j,end=" ")
