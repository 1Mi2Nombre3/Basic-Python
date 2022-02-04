x,n = map(int,input().split())
while x>100 and n > 100:
    x, n = map(int, input().split())

for i in range(1,n+1):
    print(x*i,end=" ")