#la base 3 se puede modificar por una entrada de base en este caso el 3 es en base 3
x=int(input())
while x<=0:
    x=int(input())
y=""
while x!=0:
    d=str(x%3)
    x=x//3
    y=d+y
print(y)