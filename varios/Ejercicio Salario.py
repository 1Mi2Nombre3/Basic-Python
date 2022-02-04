Sb =float(input("Enter your basic salary: "))


Aa = float(input("Enter your years of antiguaty: "))

if Aa > 30:
    Aa = 30

x = ((Sb*5)/100)
x = x*Aa
Lp = x + Sb

print("Payable liquid to collect is of: ",Lp)





