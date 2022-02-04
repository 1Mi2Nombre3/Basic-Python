cad = input()
voc = "aeiou"
cons = "bcdfghjklmnpqrstvwxyz"    # sin vocales
alp = "abcdfghijklmnpqrstuvwxyz"  # sin (e) y (o)

aux = ""
aux1 = ""
aux2 = ""
aux3 = ""
Cv = 0
Cv1 = 0

for i in cad:
    for j in voc:
        if i == j:
            Cv1 = 1
            aux1 = ""
            aux = aux + j
        elif len(aux) > 2:
            Cv = 1
    for k in cons:
        if i == k:
            aux = ""
            aux1 += k
        elif len(aux1) > 2:
            Cv = 1
    for l in alp:
        if i == l:
            if l != aux3:
                aux3 = l
            else:
                Cv = 1
if Cv == 1:
    print("is not acceptable")
elif Cv1 == 0:
    print("is not acceptable")
else:
    print("is acceptable")