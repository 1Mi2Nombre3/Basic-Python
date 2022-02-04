n = int(input())
a=2
b=2

for i in range(1,n+1):
    print(a,end=" ")
    a=a-1
    if a == 0:
        b=b+1
        a=b
