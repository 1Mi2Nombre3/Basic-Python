# ---------------VALIDACIÓN-----------------#
# #-----------FECHA CORRECTA 1---------------#
print("--------FECHA 1--------")
d1 = int(input("F1Dia: "))
while d1 > 31 or d1 < 0:
    print("dia no valido: ")
    d1 = int(input("F1Dia: "))
m1 = int(input("F1Mes: "))
while m1 > 12 or m1 < 0 or m1 == 2 and d1 > 29:
    print("Mes no valido")
    m1 = int(input("F2Mes: "))
while d1 == 31 and m1 == 4 or d1 == 31 and m1 == 6 or d1 == 31 and m1 == 9 or m1 < 0:
    print("Mes no valido para ese día")
    m1 = int(input("F2Mes: "))
a1 = int(input("F1Año: "))
while a1 < 0:
    print("Año no valido")
    a1 = a1 = int(input("F1Año: "))
a1r = a1
if a1 % 400 == 0:
    a1 = -1
elif a1 % 100 == 0:
    a1 = 1
elif a1 % 4 == 0:
    a1 = -1
else:
    a1 = 1

while (m1 == 2 and d1 == 28 and a1 == -1) or (m1 == 2 and d1 == 29 and a1 == 1):
    print("No existe ese año para", d1, "dias")
    a1 = int(input("F1Año: "))
    if a1 % 400 == 0:
        a1 = -1
    elif a1 % 100 == 0:
        a1 = 1
    elif a1 % 4 == 0:
        a1 = -1
    else:
        a1 = 1
# -----------FECHA CORRECTA 1---------------#
# -----------FECHA CORRECTA 2---------------#
print("--------FECHA 2--------")
d2 = int(input("F2Dia: "))
while d2 > 31 or d2 < 0:
    print("dia no valido: ")
    d2 = int(input("F2Dia: "))
m2 = int(input("F2Mes: "))
while m2 > 12 or m2 < 0 or m2 == 2 and d2 > 29:
    print("Mes no valido")
    m2 = int(input("F2Mes: "))
while d2 == 31 and m2 == 4 or d2 == 31 and m2 == 6 or d2 == 31 and m2 == 9:
    print("Mes no valido para ese día")
    m2 = int(input("F2Mes: "))
a2 = int(input("F1Año: "))
while a2 < 0:
    print("Año no valido")
    a2 = a2 = int(input("F1Año: "))
while a2 <= a1r:
    print("El año 2 debe ser mayor al año 1")
    a2 = int(input("F1Año: "))
a2r = a2
if a2 % 400 == 0:
    a2 = -1
elif a2 % 100 == 0:
    a2 = 1
elif a2 % 4 == 0:
    a2 = -1
else:
    a2 = 1
    while (m2 == 2 and d2 == 28 and a2 == -1) or (m2 == 2 and d2 == 29 and a2 == 1):
        print("No existe ese año para", d2, "dias")
        a2 = int(input("F1Año: "))
        if a2 % 400 == 0:
            a2 = -1
        elif a2 % 100 == 0:
            a2 = 1
        elif a2 % 4 == 0:
            a2 = -1
        else:
            a2 = 1
# ---------------VALIDACIÓN-----------------#
print("---------------------")
# ---------------RESOLUCIÓN-----------------#
d1 = str(d1)
m1 = str(m1)
a1r = str(a1r)
d2 = str(d2)
m2 = str(m2)
a2r = str(a2r)
print(d1 + "-" + m1 + "-" + a1r + " " + d2 + "-" + m2 + "-" + a2r)
d1 = int(d1)
m1 = int(m1)
a1r = int(a1r)
d2 = int(d2)
m2 = int(m2)
a2r = int(a2r)
c = 0
c2 = 0
c3 = 0
c4 = 0
m1r = 0
m2r = 0
for i in range(a1r, a2r - 1):
    if i % 4 == 0:
        c = c + 1
        if m1 == 1:
            m1r = (31 - d1) + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31
        elif m1 == 2:
            m1r = (29 - d1) + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31
        elif m1 == 3:
            m1r = (31 - d1) + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31
        elif m1 == 4:
            m1r = (30 - d1) + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31
        elif m1 == 5:
            m1r = (31 - d1) + 30 + 31 + 31 + 30 + 31 + 30 + 31
        elif m1 == 6:
            m1r = (30 - d1) + 31 + 31 + 30 + 31 + 30 + 31
        elif m1 == 7:
            m1r = (31 - d1) + 31 + 30 + 31 + 30 + 31
        elif m1 == 8:
            m1r = (31 - d1) + 30 + 31 + 30 + 31
        elif m1 == 9:
            m1r = (30 - d1) + 31 + 30 + 31
        elif m1 == 10:
            m1r = (31 - d1) + 30 + 31
        elif m1 == 11:
            m1r = (30 - d1) + 31
        elif m1 == 12:
            m1r = (31 - d1)
    else:
        c2 = c2 + 1
        if m1 == 1:
            m1r = (31 - d1) + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31
        elif m1 == 2:
            m1r = (28 - d1) + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31
        elif m1 == 3:
            m1r = (31 - d1) + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31
        elif m1 == 4:
            m1r = (30 - d1) + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31
        elif m1 == 5:
            m1r = (31 - d1) + 30 + 31 + 31 + 30 + 31 + 30 + 31
        elif m1 == 6:
            m1r = (30 - d1) + 31 + 31 + 30 + 31 + 30 + 31
        elif m1 == 7:
            m1r = (31 - d1) + 31 + 30 + 31 + 30 + 31
        elif m1 == 8:
            m1r = (31 - d1) + 30 + 31 + 30 + 31
        elif m1 == 9:
            m1r = (30 - d1) + 31 + 30 + 31
        elif m1 == 10:
            m1r = (31 - d1) + 30 + 31
        elif m1 == 11:
            m1r = (30 - d1) + 31
        elif m1 == 12:
            m1r = (31 - d1)
        if i % 4 == 0:
            c3 = c3 + 1
    if m2 == 1:
        m2r = d2
    elif m2 == 2:
        m2r = 31 + d2
    elif m2 == 3:
        m2r = 31 + 29 + d2
    elif m2 == 4:
        m2r = 31 + 29 + 31 + d2
    elif m2 == 5:
        m2r = 31 + 29 + 31 + 30 + d2
    elif m2 == 6:
        m2r = 31 + 29 + 31 + 30 + 31 + d2
    elif m2 == 7:
        m2r = 31 + 29 + 31 + 30 + 31 + 30 + d2
    elif m2 == 8:
        m2r = 31 + 29 + 31 + 30 + 31 + 30 + 31 + d2
    elif m2 == 9:
        m2r = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + d2
    elif m2 == 10:
        m2r = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + d2
    elif m2 == 11:
        m2r = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + d2
    elif m2 == 12:
        m2r = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + d2
    else:
        c4 = c4 + 1
        if m2 == 1:
            m2r = d2
        elif m2 == 2:
            m2r = 31 + d2
        elif m2 == 3:
            m2r = 31 + 28 + d2
        elif m2 == 4:
            m2r = 31 + 28 + 31 + d2
        elif m2 == 5:
            m2r = 31 + 28 + 31 + 30 + d2
        elif m2 == 6:
            m2r = 31 + 28 + 31 + 30 + 31 + d2
        elif m2 == 7:
            m2r = 31 + 28 + 31 + 30 + 31 + 30 + d2
        elif m2 == 8:
            m2r = 31 + 28 + 31 + 30 + 31 + 30 + 31 + d2
        elif m2 == 9:
            m2r = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + d2
        elif m2 == 10:
            m2r = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + d2
        elif m2 == 11:
            m2r = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + d2
        elif m2 == 12:
            m2r = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + d2
s1 = c * 366
s2 = c2 * 365
s3 = c3 * 366
s4 = c4 * 365
T = s1 + s2 + m1r + m2r - 1
print(T)
# ---------------RESOLUCIÓN-----------------#
