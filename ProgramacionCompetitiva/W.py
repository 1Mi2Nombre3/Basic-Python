x = int(input())
while x < 1 or x > 1000:
    x = int(input())
y = ""
while x != 0:
    d = str(x % 3)
    x = int(x / 3)
    y = d + y
print(y)
