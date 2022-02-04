#fibonacci
n = int(input())
while n <= 0 or n>1000:
    n = int(input())
y=0
x=1
for i in range(1,n+1):
    print(y,end=" ")
    y=y+x
    x=y-x


