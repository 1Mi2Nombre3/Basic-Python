def extraerVoc(c):
    voc = "aeiou"
    cad1 = ""
    for i in c:
        cv = 0
        for j in voc:
            if i == j:
                cv = 1
        if cv == 0:
            cad1 = cad1 + i
    print(cad1)


cad = "hola mundo como estan"
extraerVoc(cad)
