N=int(input())
while N>=100 or N<=0:
    N = int(input())

x=int(input())
while x>10 or x<=0:
    x=int(input())
fac=1
a=1
c=0

c2=0

Tit=0
c3=0
c4=0
for i in range(N):
    fac = 1
    a = 1
    for j in range(a,c+1):
        fac=fac*j
    c=c+1
    if c==4:
        c=0
        a=1

    c2=c2+1
    if c2==4:
        c2=1
        x1 = x ** c2
    else:
        x1=x**c2

    Tit=Tit+1
    if Tit==1:
        print("Sumatoria Generada:")

    c3=c3+1
    x1 = str(x1)
    fac = str(fac)
    if c3==1:
        print(x1+"/"+fac,end=" ")

    c4=c4+1
    if c3>1 and c4%2==1:
        print("+ "+x1+"/"+fac,end=" ")
    if c3>1 and c4%2==0:
        print("- "+x1+"/"+fac,end=" ")
    x1 = int(x1)
    fac = int(fac)