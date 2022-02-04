def MasRep(cad):
    c = 0
    aux = 0
    for i in cad:
        for j in cad:
            if i == j:
                c = c + 1
        if aux < c:
            aux = c
        c = 0
    print(aux)

MasRep("3344559900")
