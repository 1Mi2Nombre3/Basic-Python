import math
while True:
    n=int(input())
    while n<=0 or n<10**6:
        n = int(input())
    n1=n
    n2=n
    y=""
    y2=""
    men=9
    while n!=0:
        d=n%10
        n=n//10
        if d>=5:
            d = str(d)
            y=y+d
            d = int(d)
    if y!="":
        y=int(y)
        y1=y
        y2=""
        y3=y
        y4=y
        cd = int(math.log10(y)) + 1
        while y!=0:
            d1 = y % 10
            y = y // 10
            if men > d1:
                men = d1
        men1=men
        while y3!=0:
            for i in range(1,cd+1):
                d3 = y4 % 10
                y4 = y4 // 10
                if d3 == men1:
                    d3=str(d3)
                    y2=y2+d3
                    d3=int(d3)
                    y3 = y3 // 10
            men1=men1+1
            y4=y1
    yR1=y2
    y=""
    y2="0"
    men=9
    while n1!=0:
        d=n1%10
        n1=n1//10
        if d<5:
            d = str(d)
            y=y+d
            d = int(d)
    if y!="":
        y=int(y)
        y1=y
        y2=""
        y3=y
        y4=y
        cd = int(math.log10(y)) + 1
        while y!=0:
            d1 = y % 10
            y = y // 10
            if men > d1:
                men = d1
        men1=men
        while y3!=0:
            for i in range(1,cd+1):
                d3 = y4 % 10
                y4 = y4 // 10
                if d3 == men1:
                    d3=str(d3)
                    y2=y2+d3
                    d3=int(d3)
                    y3 = y3 // 10
            men1=men1+1
            y4=y1
    y5 = y2
    y6 = ""
    y5=int(y5)
    while y5!=0:
        d = y5 % 10
        y5 = y5 // 10
        d=str(d)
        y6 = y6+d
        d=int(d)

    c=0
    while n2!=0:
        d = n2 % 10
        n2 = n2 // 10
        if d==0:
            c=1
    if yR1=="":
        if c==1:
            print(y6+"0")
        else:
            print(y6)
    elif y6=="":
        if c==1:
            print("0"+yR1)
        else:
            print(yR1)
    else:
        if c==1:
            print(y6+"0"+yR1)
        else:
            print(y6+yR1)
