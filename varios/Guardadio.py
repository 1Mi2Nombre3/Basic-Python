n = int(input())

while n <= 0 or n > 100:
    n = int(input())
s = 0
t = 0
y = 1
for i in range(1, n + 1):
    if i % 2 == 0:
        s = (y * -2)
        t = y + s
        x=t
    else:
        i = i + t
        x=i
    y = i
    print(x,end=" ")
