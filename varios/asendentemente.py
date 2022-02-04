a,b,c,d=map(int,input().split())

x=max(a,b,c,d)
y=min(a,b,c,d)

if x==a:
    if b==y:
        if c>d:
            print(b,d,c,a)
        elif d>c:
            print(b,c,d,a)
    elif c==y:
        if b>d:
            print(c,d,b,a)
        elif d>b:
            print(c,b,d,a)
    elif d==y:
        if b>c:
            print(d,c,b,a)
        elif c>b:
            print(d,b,c,a)
elif x==b:
    if a == y:
        if c > d:
            print(a, d, c, b)
        elif d > c:
            print(a, c, d, b)
    elif c == y:
        if a > d:
            print(c, d, a, b)
        elif d > a:
            print(c, a, d, b)
    elif d == y:
        if c > a:
            print(d, a, c, b)
        elif a > c:
            print(d, c, a, b)
elif x==c:
    if a==y:
        if b>d:
            print(a,d,b,c)
        elif d>b:
            print(a,b,d,c)
    elif b==y:
        if a>d:
            print(b,d,a,c)
        elif d>a:
            print(b,a,d,c)
    elif d==y:
        if b>a:
            print(d,a,b,c)
        elif a>b:
            print(d,b,a,c)
elif x==d:
    if a==y:
        if c>b:
            print(a,b,c,d)
        elif b>c:
            print(a,c,b,d)
    elif b==y:
        if a>c:
            print(b,c,a,d)
        elif c>a:
            print(b,a,c,d)
    elif c==y:
        if a>b:
            print(c,b,a,d)
        elif b>a:
            print(c,a,b,d)