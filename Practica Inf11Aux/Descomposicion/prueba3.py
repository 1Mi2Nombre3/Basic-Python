import math
import sys

for datos in sys.stdin:
    x,d = map(int, datos.split(" "))
    cd = int(math.log10(x)) + 1
    x1 = x
    x2 = x
    may=0
    may1=0
    c=0
    while x!=0:
        n = x % 10
        n1 = n
        x = x // 10
        if may < n:
            may = n
    y=""
    if may == d:
        c=1
        while x2!=0:
            n = x2 % 10
            x2 = x2 // 10
            if n != d:
                n=str(n)
                y = y+n
                n=int(n)
        y=int(y)
        while y != 0:
            n = y % 10
            n2 = n
            y = y // 10
            if may1 < n:
                may1 = n
        d=may1
    if c==0:
        while x1!=0:
            n = x1 // int(math.pow(10, cd - 1))
            x1 = x1 % int(math.pow(10, cd - 1))
            cd=cd-1
            if n == d:
                n = may
            print(n,end="")
    else:
        while x1!=0:
            n = x1 // int(math.pow(10, cd - 1))
            x1 = x1 % int(math.pow(10, cd - 1))
            cd=cd-1
            if n == may:
                n = may1
            print(n,end="")
    print()