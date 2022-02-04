x=int(input())
while x!=100:
    d = 0
    for i in range(1,int(x/2)+1,1):
        if x%i==0:
            d=d+1
    if d=   =1:
        print(x,end=" ")
    x = int(input())