n=int(input())
while n<=0 or n>10**4:
    n = int(input())
s=1
a=2
b=3
c=3

d=0
e=0

for i in range(n):
    print(s, end=" ")
    if a>b:
        c=c-1
        s=s+c
        if c==2:
            a=2
            b = b + 1
            d=1

    else:
        if d==1:
            s=s+d
            e=e+1
            if e==2:
                d=0
                e=0
        else:
            s=s+a
            a=a+1
            c=b









