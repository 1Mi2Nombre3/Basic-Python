n=int(input())
c=0
a=0
for i in range(1,n+1):
    if n%i==0:
        c=c+1
if c==2:
    print("si prim")
else:
    print("no primo")