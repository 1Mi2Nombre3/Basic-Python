n = int(input())
while n<=0 or n>1000:
    n = int(input())
a=0
c2=0
Nul=0

while n!=-1:
    c=0
    P=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    if c==2:
        a=a+n
        c2=c2+1
        if c2==3:
            P=a//3
            print(P)
            Nul=P
            p=0
            c2=0
            a=0
    n=int(input())

if Nul==0:
    print("No hubo ningún promedio de primos.")