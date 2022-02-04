import math
t=int(input())
while t<=0 or t>1000:
    t = int(input())
for i in range(t):
    y1=""
    L=[]
    x,y=map(int,input().split())
    cd=int(math.log10(x))+1

    for i in range(cd):
        d = x // int(math.pow(10, cd - 1))
        x = x % int(math.pow(10, cd - 1))

        d1 = y // int(math.pow(10, cd - 1))
        y = y % int(math.pow(10, cd - 1))

        if d>d1:
            d=str(d)
            d1=str(d1)
            L.append(d)
            L.append(d1)
        else:
            d = str(d)
            d1 = str(d1)
            L.append(d1)
            L.append(d)

        cd=cd-1
        d=int(d)
        d1=str(d1)
    for z in L:
        y1=y1+z
    print(y1)