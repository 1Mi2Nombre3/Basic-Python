def ClaveMur(cad):
    cad = cad.upper()
    L = "MURCIELAGO"
    lon = len(L)
    cad2 = ""
    for i in cad:
        cv = 0
        aux = 0
        for j in range(lon):
            if i == L[j]:
                aux = j
                cv = 1
                break
        if cv == 0:
            cad2 = cad2 + i
        else:
            cad2 = cad2 + str(aux)
    print(cad2)


ClaveMur("BOLIVIA")
