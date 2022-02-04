#Hallar: S = (x^1)/3 + (x^3)/6 + (x^5)/9 + (x^7)/12

x=int(input("Valor de x: "))
n=int(input("Valor de N elementos: "))
while n<=0:
    n=int(input("Valor de N elementos: "))

a=1
b=3
S=0

for i in range(n):
    S=S+((x**a)/b)
    a=a+2
    b=b+3
print(S)


