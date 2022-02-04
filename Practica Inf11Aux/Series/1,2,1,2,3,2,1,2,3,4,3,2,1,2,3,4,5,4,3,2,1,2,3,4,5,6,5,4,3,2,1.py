n = int(input())

a=1
b=0
c=2
d=0

for i in range(1,n+1):
    if b==0:
        if c==0:
            res=a
            d=d-1
            if d == 0:
                c=a+1
                a=1
                b=1
            else:
                a=a+1
        else:
            res=a
            b=1
        print(res,end=" ")
    else:
        res=c
        print(res,end=" ")
        c=c-1
        if c==0:
            b=0
            a=a+1
        else:
            d=d+1