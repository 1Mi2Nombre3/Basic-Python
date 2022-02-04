x=int(input())
while x<2 and x>10**9:
     x=int(input())
q=1
while x!=-1:
    a=0
    fac=1
    print("Case#",q)
    q=q+1
    c=0
    for i in range(1,x+1):
        fac=fac*i
        c=c+1
        if x==fac:
            if x!=1:
                x=str(x)
                c=str(c)
                print("El número "+x+" = "+c+"!.")
                x=int(x)
                c=int(c)
                a=1
    if a==1:
        a=0
    else:
        print("El número",x,"no es un factorial.")
        a=0
    x=int(input())
print("---------FIN DE ARCHIVO---------")