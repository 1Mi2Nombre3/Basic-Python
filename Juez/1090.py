n=int(input())
while n<=0:
    n=int(input())
suma=0
for i in range(0,n,3):
    suma+=i
print(suma)