cad = input()
lon = len(cad)
aux = ""
c = 0
c1 = 0
cv = 0
for i in range(lon):    # i --> Imprime 0,1,2,3,4...lon
    for j in cad[i]:    # j --> Indica posicion en cad[i]
        for aux1 in aux:  # aux --> Si hay una letra repetida entonces no contara
            if j == aux1:
                cv = 1
        if cv == 0:          # si hay letra repetida entonces no entrara
            for k in cad:    # Imprime letra a letra el string cad
                if j == k:    # verifica si en el string hay una letra repetida
                    c1 = c1 + 1
                    if c1 >= 2:  # verifica que la letra repetida entra 2 veces
                        c = c + 1  # Inicia el contador de las repetidas
                        aux = aux + k  # revisar el comentario de la linea 9
        c1 = 0
        cv = 0
print(c)