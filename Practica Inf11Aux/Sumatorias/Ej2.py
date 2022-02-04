n=int(input())
while n<=0 or n>1700:
    n=int(input())
res=0
a=0
c=1
p=2
d=2
while c <= n:
    if p%d==0:
        if p==d:
            c=c+1
            a=a+1
            if a%2==0:
                b=p+(p*-2)
            else:
                b=p
            res=res+b
        d=2
        p=p+1
    else:
        d=d+1
print(res)