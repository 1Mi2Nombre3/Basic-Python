#primos

n = int(input())
while n <= 0:
    n = int(input())
y=1
x=0
serie = 0
for i in range(1,n+1):

        y=y+x
        x=y-x
        print(y, end=" ")