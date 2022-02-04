import math
N=int(input())
while N%3!=0 or N<=0 or N>3*(10**5):
    N=int(input())
A=0
sem=0
per=0
con=0
con2=0
a=0
b=0
c=0
for i in range(1,N+1):
    x=int(input())
    con=con+1
    if con==1:
        a=x
    elif con==2:
        b=x
    elif con==3:
        c=x
    per=per+x
    if i%3==0:
        sem=per/2
        sa=sem-a
        sb=sem-b
        sc=sem-c
        if sa<0:
            con2=con2+1
        elif sb<0:
            con2=con2+1
        elif sc<0:
            con2=con2+1
        if con2%2==0:
            Area=math.sqrt(sem*(sa)*(sb)*(sc))
            print("Area:",Area)
        else:
            print("No hay area")  #area con acento xD
        con=0
        per=0
        con2=0