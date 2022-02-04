import math

n=int(input())
while n<=0 or n>99999:
    n = int(input())
cd=int(math.log10(n))+1
cd1=(cd//2)+1

if cd%2==1:
    for i in range(cd1):
        d=n%10
        n=n//10
    print(d)
else:
    print("*")
