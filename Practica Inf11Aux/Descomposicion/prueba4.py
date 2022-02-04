x1=int(input())
may=8
y=""
while x1!=0:
    n1 = x1 % 10
    x1 = x1 // 10
    if may == n1:
        x1 = x1 // 10
        print(n1,end="")