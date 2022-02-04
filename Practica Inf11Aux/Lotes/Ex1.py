import math

n=int(input())
while n<=0:
    n = int(input())

for i in range(n):
    x=int(input())
    cd=int(math.log10(x))+1
    while x<=0 or cd<=1:
        x = int(input())
        cd = int(math.log10(x)) + 1

    d = x // int(math.pow(10, cd - 1))
    x = x % int(math.pow(10, cd - 1))
    print(d,end=" ")
    cd=cd-1