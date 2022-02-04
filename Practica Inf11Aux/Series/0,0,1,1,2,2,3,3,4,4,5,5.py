#Generar para N términos: 0,0,1,1,2,2,3,3,4,4, ...

n=int(input())
a=0
for i in range(n):
    if i%2==0:
        print(a,end=" ")
    else:
        print(a,end=" ")
        a=a+1
