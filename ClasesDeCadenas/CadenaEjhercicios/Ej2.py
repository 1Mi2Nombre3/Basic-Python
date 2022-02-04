# Anagrama.- 2 palabras que tengan el mismo tamaño, y las mismas letras
A = input()
B = input()
NewA = ""
NewB = ""
con = 1
C = 0
Cv = 0
# Eliminamos cualquier espacio que haya en A o B
for i in A:
    if i != " ":
        NewA = NewA + i
for j in B:
    if j != " ":
        NewB = NewB + j
# _______________________________________________
for k in NewA:
    for l in NewB:
        if k == l:
            C = 1
    if C == 0:
        Cv = 1
    C = 0
# Misma longitud en las nuevas palabras sin espacios
lonA = len(NewA)
lonB = len(NewB)
if lonA != lonB:
    Cv = 1
# ________________________________________________
if Cv == 0:
    print("Son anagramas")
else:
    print("No son anagramas")