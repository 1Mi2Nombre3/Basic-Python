n,k=map(int,input().split())
while (n<1 or n>100) or (k<1 or k>100):
    n, k = map(int, input().split())
a=0
b=0

for i in range(n+1):
    a=((i+k)/(2+i+k))
    b=a+b
b=int(b)
print(b)