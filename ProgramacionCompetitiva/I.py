Mayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Minus = "abcdefghijklmnopqrstuvwxyz"
c = input()
cv = 0
for i in Mayus:
    if c == i:
        cv = 1
for j in Minus:
    if c == j:
        cv = 0
if cv == 0:
    print(c.upper())
else:
    print(c.lower())