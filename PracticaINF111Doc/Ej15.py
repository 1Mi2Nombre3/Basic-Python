#Generar para N términos: 2,3,5,7,11,13, ...

n = int(input("N: "))
while n<=0:
    n = int(input("N: "))
a=1
b=2
c=2

while a<=n:
    if b%c==0:
        if b==c:
            print(b,end=" ")
            a=a+1
        b=b+1
        c=2
    else:
        c=c+1
