cad = input()
NewCad = ""
aux = ""
aux1 = ""
C = 0
for i in cad:
    if i != " ":
        aux = aux + i
    else:
        lon = len(aux)
        for j in range(lon-1, -1, -1):
            NewCad = NewCad + aux[j]
        NewCad = NewCad + " "
        aux = ""
lon = len(aux)
for j in range(lon-1, -1, -1):
    NewCad = NewCad + aux[j]
print(NewCad)