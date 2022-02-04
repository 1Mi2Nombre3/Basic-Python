#Serie 1,5,2,2,7,3,3,10,4....
n=int(input())
a=1
b=5
c=0

for i in range(n):
    if i%3 == 0:
        res=a
        a=a+1
    else:
        c=c+i
        if c==i:
            res=b
            b=b+a
        else:
            res=a
            c=0
    print(res,end=" ")