# Dado un lote de n Números, verificar si cada número es perfecto.
# (Un número es perfecto cuando la suma de sus divisores es igual al número
# Ejm: si N=6, sus divisores son: 1,2,3 y la suma de sus divisores es 6)

n=int(input("Lotes: "))
while n<=0:
    n = int(input("Lotes: "))
a=0

for i in range(n):
    x=int(input())
    while x<=0:
        x = int(input())
    a=0
    for j in range(1,x):
        if x%j==0:
            print(j,end=" ")
            a=a+j
    if x==a:
        print("=",a,)