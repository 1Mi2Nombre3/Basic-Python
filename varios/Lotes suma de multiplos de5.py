n=int(input())
while n<=0:
    n=int(input())
s=0
for i in range(n):
    x=int(input())
    if x%5==0:
        s=s+x

print(s)
