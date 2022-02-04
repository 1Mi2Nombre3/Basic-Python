n = int(input())
while n <= 0 or n>1000:
    n = int(input())
y=1
x=0
z=1
serie = 0
for i in range(1,n+1):
    if i%2 == 0:
        serie = y
        y=y+x
        x=y-x
    else:
        serie = z
        z = z+1
    print(serie,end=" ")