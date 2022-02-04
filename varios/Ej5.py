S = float(input("Ingrese saldo: "))

if S <= 40:
    p = S*16
    print("Su monto a cobrar es de: ",p)
else:
    e = S-40
    S = 40*16
    e = e*20
    p = e+S
    print("Su monto a cobrar es de: ", p)
