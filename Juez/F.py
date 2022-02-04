cad = input()
lon = len(cad)
while lon < 1 or lon >= 560:
    cad = input()
    lon = len(cad)

voc = "aeiou"
cons = "bcdfghjklmnpqrstvwxyz"
cadv = ""
cadv1 = ""
cadc = ""
aux = ""
c = 0
c1 = 0
c2 = 0

for i in cad:
    c2 += 1
    if i == " ":
        c += 1
        c1 = 1
    aux = aux + i

    if lon == c2:
        c1 = 1

    if c1 == 1:
        for j in voc:
            if aux[0] == j:
                cadv = cadv + aux
        for k in cons:
            if aux[0] == k:
                cadc = cadc + aux
        aux = ""
        c1 = 0
print(cadv)
print(cadc)
print(cad)
print("Espacios en blanco:",c)