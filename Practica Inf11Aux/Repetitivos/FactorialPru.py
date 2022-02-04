x=int(input())
fac=1
c=0
for i in range(1, x+1):
    fac=fac*i
    c=c+1
    if x==fac:
        print(c,"si")
        c=0