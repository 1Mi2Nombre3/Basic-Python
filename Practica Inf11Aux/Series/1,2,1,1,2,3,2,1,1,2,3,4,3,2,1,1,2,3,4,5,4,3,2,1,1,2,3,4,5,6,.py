n=int(input())

a=1
b=1
c=1
d=1
res=0

for i in range(1,n+1):
    if a==1:
        res=b
        d=d-1
        c=c+1
        if d==0:
            a=0
            b=1
        else:
            b=b+1
    else:
        res=c
        d=d+1
        c=c-1
        if c==0:
            a=1
            c=1

    print(res,end=" ")