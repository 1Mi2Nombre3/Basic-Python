#Generar para N términos: 0,1,1,0,0,0,1,1,1,1,0,0,0,0,0,1, ...
#Contador a diferente al i en este caso a

n=int(input("N: "))
while n<=0:
    n = int(input("N: "))
x=0
y=1
a=1
b=0
for i in range(n):
    if a%2==0:
        res=y
        b=b+1
        if a==b:
            a=a+1
            b=0
    else:
        res=x
        b=b+1
        if a==b:
            a=a+1
            b=0
    print(res,end=" ")
