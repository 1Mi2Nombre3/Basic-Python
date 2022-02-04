n=int(input())
for i in range(n):
    a,b,c=map(int,input().split())
    while (a>b or a>c) and (b>c or b>c):
        a, b, c = int(input())
    d=0
    e=a
    while a%b!=0 or a%c!=0:
        d = d + 1
        a=(b*d)
    print(a-e)