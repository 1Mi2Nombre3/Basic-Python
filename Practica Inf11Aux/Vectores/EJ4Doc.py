def leer(a, n):
    for i in range(n):
        a[i] = int(input())


def show(a, n):
    print(a)


def bus_sec(a, n, x):
    pos = -1
    for i in range(n):
        if a[i] == x:
            pos = i
            print("found in", pos)
    if pos == -1:
        print("not found")


# main

n = int(input("n: "))
x = int(input("x: "))
b = [0] * n
leer(b, n)
show(b, n)
bus_sec(b, n, x)
