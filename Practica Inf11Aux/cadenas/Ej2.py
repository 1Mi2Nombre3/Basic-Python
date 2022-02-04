cad = input()
aux = ""
c = 0
c1 = 0

for i in cad:
    for j in cad:
        if i == j:
            c = c + 1
    if c == 1:
        c1 = c1 + 1
    c = 0
    if c1 == 2:
        aux = i
        c1 = 3

if aux == "":
    print("*")
else:
    print(aux)