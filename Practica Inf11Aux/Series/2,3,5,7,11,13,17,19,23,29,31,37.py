# Serie:  2 3 5 7 11 13 17 19 23 29...
n = int(input())

c = 1
div = 2
d = 2
while c <= n:
    if div % d == 0:
        if div == d:
            print(div, end=" ")
            c = c + 1
        div = div + 1
        d = 2
    else:
        d = d + 1
