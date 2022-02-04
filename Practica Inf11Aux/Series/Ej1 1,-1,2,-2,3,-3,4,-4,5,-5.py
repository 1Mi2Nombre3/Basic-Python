n = int(input())
while n <= 0 or n>1000:
    n = int(input())
s=0
t=0
y=1

for i in range(1,n+1):
    if i%2 == 1:
        s = (y*-2)
        t = y+s
        x = y
    else:
        y=y+1
        x=t
    print(x,end=" ")

