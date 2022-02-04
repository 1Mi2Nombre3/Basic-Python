cad = input()
Newcad = ""
alp = "abcdefghijklmnopqrstuvwxyz"
cad2 = ""
aux = ""

for i in cad:
    if i != " ":
        Newcad = Newcad + i

for i in Newcad:
    for j in alp:
        if i != j:
            cad2 = cad2 + j
    alp = cad2
    cad2 = ""
if alp == "":
    print("NO SE IGNORO A NINGUN CARACTER")
else:
    print(alp)
