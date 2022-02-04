x = int(input())
while x<=1 and x<=1000:
    x = int(input())

L=[]
while (x>=1):
    L.append(x%3)
    x = x//3
B=L[::-1]
for i in B:
    print(i, end="")