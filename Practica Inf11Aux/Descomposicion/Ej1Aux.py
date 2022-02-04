import math

a, b, c = map(int, input().split())
print(c)
cd = int(math.log10(c)) + 1
y = ""
for i in range(cd):
    d = c // int(math.pow(10, cd - 1))
    c = c % int(math.pow(10, cd - 1))
    cd = cd - 1
    if d % 2 == 0:
        d = str(d)
        for j in range(a):
            



