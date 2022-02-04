n=int(input())

y=0
x=1
serie=0

a=1
b=2
c=2


for i in range(n):
    if i%2==0:
        for j in range(0,1):
            serie=y
            y = y + x
            x = y - x
    else:
        while a<=1:
            if b % c == 0:
                if b == c:
                    serie = b
                    a = a + 1
                c = 2
                b = b + 1
            else:
                c = c + 1
        a=1
    print(serie,end=" ")