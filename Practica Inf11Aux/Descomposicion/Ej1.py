#0 , 1 , 1 , 2 , 3 , 5 , 8 , 13
import math
while True:
    x = int(input())
    while x<=0 or x>10**6:
        x = int(input())
    cd = int(math.log10(x)) + 1
    x1 = x
    a = 0
    b = 1
    y = ""
    while x!=0:
        d = x // int(math.pow(10, cd - 1))
        x = x % int(math.pow(10, cd - 1))
        cd=cd-1
        a = 0
        b = 1
        c=0
        for i in range(d+1):
            a = a + b
            b = a - b
            if d==a:
                d=str(d)
                if d=="1":
                    c=1
                    #------------------
                    if x1%2==0:
                        y = y+"1"+d+"2"
                        c=1
                    else:
                        y = y+"0"+d+"1"
                        c=1
                    #------------------
                elif d=="2":
                    y=y+"1"+d+"3"
                    c=1
                elif d=="3":
                    y=y+"2"+d+"5"
                    c=1
                elif d=="5":
                    y=y+"3"+d+"8"
                    c=1
                elif d=="8":
                    y=y+"5"+d+"3"
                    c=1
        if c==0:
            d = str(d)
            y=y+d
            d = int(d)
    y=int(y)
    print(y)



