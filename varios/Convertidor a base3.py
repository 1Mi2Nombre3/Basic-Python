x=int(input())
while x<= 0:
    x=int(input("Ingrese x: "))
b=int(input())
while b<2:
    b = int(input("Ingrese base: "))
y=""
while x != 0:
    d=str(x%b)
    x=int(x/b)
    y=d+y
print("El nro convertido es: ",y )