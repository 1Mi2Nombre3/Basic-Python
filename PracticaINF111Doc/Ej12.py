#Generar para N términos: 1,3,3,6,5,9,7,12,9,15,11, ...

n=int(input("N: "))
while n<=0:
    n = int(input("N: "))
a=1
b=3

for i in range(1,n+1):
    if i%2==0:
        res=b
        b=b+3
    else:
        res=a
        a=a+2
    print(res,end=" ")