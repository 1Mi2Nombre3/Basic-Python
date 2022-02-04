n = int(input())

a=0
c=-1
d=1
e=0

for i in range(n):
    if i%2 == 0:
        a=a+2
        res=a
    else:
        e=c+d
        c=d
        d=e
        res=e
    print(res,end=" ")