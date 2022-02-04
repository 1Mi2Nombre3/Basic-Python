n=int(input())
while n<=0:
    print(n)
aux=0
for i in range(n):
    x=int(input())
    if i == 0:
        aux=x
    else:
        aux=aux+x
        print(aux)