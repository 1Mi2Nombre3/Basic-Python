#Hallar: S = x^2/2! - x^4/4! + x^8/6! - x^16/!8
x=int(input("Valor de x: "))
n=int(input("Valor de N elementos: "))
while n<=0:
    n = int(input("Valor de N elementos: "))
a=1
b=0
fac=1
con=0
S=0

for i in range(n):
    fac=1
    a=a*2
    b=b+2
    for k in range(1,b+1):
        fac=fac*k
    if con%2==0:
        S=S+(x**a)/fac
    else:
        S=S-(x**a)/fac
    con=con+1
print(S)
