n=int(input())
a=1
c = 1
div = 2
d = 2

for i in range(1,n+1):
    if i%2==1:
        while c <= 1:
            if div % d == 0:
                if div == d:
                    print(div, end=" ")
                    c = c + 1
                div = div + 1
                d = 2
            else:
                d = d + 1
        c=1
    else:
        print(a,end=" ")
        a=a+1

