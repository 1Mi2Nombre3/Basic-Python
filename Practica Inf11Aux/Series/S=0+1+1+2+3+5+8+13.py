n = int(input())
a=-1
b=1
c=0
serie=0

for i in range(1,n+1):
    c=a+b
    a=b
    b=c
    serie=serie+c

print(serie)