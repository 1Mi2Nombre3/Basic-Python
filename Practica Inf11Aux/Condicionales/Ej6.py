Sb =float(input("Enter your basic salary: "))

a = float(input("Enter your years of antiguaty: "))

if a <= 5:
    b = (2*Sb)/100
elif a>=6 and a<=10:
    b = (5*Sb)/100
elif a>= 11 and a<=15:
    b = (10*Sb)/100
elif a>=16:
    b = (20*Sb)/100
else:
    print("???")

Lp = Sb+b
print("Sueldo basico es: ",Lp)