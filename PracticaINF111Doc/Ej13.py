#Generar para N términos: 1,2,0,1,4,0,1,6,0,1, ...

n=int(input("N: "))
while n<=0:
    n = int(input("N: "))
a=1
b=2
c=0
d=0

for i in range(n):
    if i%3==0:
        res=a
        c=0
    else:
        res=b
        c=c+1
        if c==2:
            b=d+2
        else:
            d=b
            b=0
    print(res,end=" ")