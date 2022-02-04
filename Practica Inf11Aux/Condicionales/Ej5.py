cm = int(input())

while cm <= 0:
    cm = int(input())

m = ((cm * 1) // 100)
km = ((m * 1) // 1000)
Rm = (m % 1000)
Rcm = (cm % 100)

print(cm, "centímetros son", km, "km", Rm, "m", Rcm, "cm")
