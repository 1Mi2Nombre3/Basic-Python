A, B, C = map(int, input("Ingrese 3 valores seguidos separados por un espacio: ").split())

A = A * 2
B = A + B
C = C * (-1)
C = C / B
C = str(C)
print("X=" + C)
