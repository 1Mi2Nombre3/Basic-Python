cad = input()
pal = input()
n = len(pal)
c = 0
while n != 1:
    pal = input()
    n = len(pal)

for i in cad:
    if i == pal:
        c = c + 1
print("la letra", pal, "se repite", c)
