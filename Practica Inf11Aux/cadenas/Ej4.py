AlpMin = "abcdefghijklmnopqrstuvwxyz"
AlpMay = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Numb = "123456789"
Carac = "!@#$%^&*,-+="
cad = input()
lon = len(cad)
while lon < 6:
    cad = input()
    lon = len(cad)
C = 0
C1 = 0
C2 = 0
C3 = 0
R = 0
# abc123
for i in cad:
    for j in AlpMin:
        if i == j:
            C = 1
    for l in Numb:
        if i == l:
            C1 = 1
            if C2 == 1:
                C = 1
            elif C == 1:
                C = 0
    for k in AlpMay:
        if i == k:
            C2 = 1
    for m in Carac:
        if i == m:
            C3 = 4
R = C + C1 + C2 + C3
if R == 1:
    print("CLAVE NO SEGURA")
elif R == 2:
    print("CLAVE DEBIL")
elif R == 3:
    print("CLAVE MEDIA")
else:
    print("CLAVE SEGURA")