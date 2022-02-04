def Noprimos(x):
    c = 0
    if x == 1:
        print(x)
    else:
        for i in range(1, x + 1):
            if x % i == 0:
                c = c + 1
    if c > 2:
        print(x)


while True:
    x = int(input())
    Noprimos(x)
