x=int(input())

while x<100:
    x = int(input())

while x != 0:
    d = x % 10
    x = x // 10
    if d % 2 == 0:
        print(d,end=" ")
