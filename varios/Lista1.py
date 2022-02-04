import math

x=int(input())
L=[]
for i in range(1,x+1):
    c=x//10
    d=x%10
    x=c
    L.append(d)
    if x==0:
        break
print(L)
L=L[::-1]
y=0
for i in L:
    y=y+i

print(y)

math.log10()