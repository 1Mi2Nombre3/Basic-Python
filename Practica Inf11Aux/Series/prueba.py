#0 1 0 0 1 0 0 0 1 0 0 0 0 1 0 0 0 0 0
N = int(input())
c=0
c2=1

for i in range(1,N+1):
    if c%c2==0:
        c=c+2
        print(0,end=" ")
    else:
        c2 = c2 + 1
        c=0
        print(1,end=" ")