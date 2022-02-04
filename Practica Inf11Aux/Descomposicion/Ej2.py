import math
while True:
    n=int(input())
    while n<=0 or n>10**9:
        n=int(input())
    n1=n
    cd=int(math.log10(n))+1
    cd1=cd
    y=""
    while n!=0:
        s = 10
        d = n // int(math.pow(10, cd - 1))
        n = n % int(math.pow(10, cd - 1))
        s = s-d
        y1 = str(s)
        if s<10:
            y=y+y1
        cd=cd-1
    y=int(y)
    c=0
    c1=0
    res=""
    while n1!=0:
        d = n1 // int(math.pow(10, cd1 - 1))
        n1 = n1 % int(math.pow(10, cd1 - 1))
        d1 = y // int(math.pow(10, cd1 - 1))
        y = y % int(math.pow(10, cd1 - 1))
        res1=str(d)
        res2=str(d1)
        res=res+res1+res2
        cd1=cd1-1
    res=int(res)
    cd2=int(math.log10(res))+1
    while res!=0:
        d = res // int(math.pow(10, cd2 - 1))
        res = res % int(math.pow(10, cd2 - 1))
        if d!=0:
            print(d,end="")
        cd2 = cd2-1
    print()





