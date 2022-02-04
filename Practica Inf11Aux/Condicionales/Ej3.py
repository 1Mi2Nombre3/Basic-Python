import sys

for datos in sys.stdin:
    a, b = map(int, datos.split(" "))
    while a < 0 or b < 0:
        a, b = map(int, datos.split(" "))
    d = a // b
    e = a % b
    if e == 0:
        print("La división es exacta. Cociente:", d)
    else:
        print("La división no es exacta. Cociente:", d, "Resto:", e)
