import sys
for datos in sys.stdin:
    x,y,z = map(int, datos.split(" "))
    if x == y and x == z:
        print("Ha escrito tres veces el mismo número.")

    elif x == y or x == z:
        print("Ha escrito uno de los números dos veces.")

    else:
        print("Los tres números que ha escrito son distintos.")
