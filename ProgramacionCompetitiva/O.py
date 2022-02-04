L = "MURCIELAGO"
lon = len(L)
n = int(input())
for i in range(n):
    cv = 0
    cad2 = ""
    cad = input()
    cad = cad.upper()
    for i in cad:
        cv = 0
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
