#Ej25
import math

n,k=map(int,input().split())
while n<=0:
    n = int(input())
cd=int(math.log10(n))+1
cd1=cd
a=0
while n!=0:
    d = n // int(math.pow(10,cd-1))
    n = n % int(math.pow(10,cd-1))
    a=a+1
    cd=cd-1
    if a==k:
        d1=d
print(cd1,d1)