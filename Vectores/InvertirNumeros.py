def InverNum(x):
    import math
    cd = int(math.log10(x) + 1)
    y = ""
    x = str(x)
    for j in range(cd - 1, -1, -1):
        y = y + x[j]
    L[i] = int(y)

#Funciona con una lista ya definida con sus x elementos