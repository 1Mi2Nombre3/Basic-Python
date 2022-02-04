def desc(cad):
    voc = "aeiou"
    aux = ""
    aux1 = ""
    cv = 0
    for i in cad:
        cv = 0
        for j in voc:
            if i != j:
                aux = i
            else:
                cv = 1
        if cv == 0:
            aux1 = aux1 + aux
        aux = ""
    return aux1


print(desc("holacomoestasamigomio dawd"))
