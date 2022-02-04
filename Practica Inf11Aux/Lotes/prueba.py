import math
x=int(input())
cd=int(math.log10(x))+1
while x!=0:
    d = x // int(math.pow(10, cd - 1))
    x = x % int(math.pow(10, cd - 1))
    cd=cd-1
    print(d)