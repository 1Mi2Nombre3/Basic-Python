c1 = input()
c2 = ""
c = 1
for i in c1:
    if c == 1:
        c2 = c2 + i
        c = 0
    if i == " ":
        c = 1
print(c2)