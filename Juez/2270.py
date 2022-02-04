n = int(input())
m = (n // 100)
cm = n - (m * 100)
k = m // 1000
if m >= 1000:
    m = m//10
print(n, "centímetros son", k, "km", m, "m", cm, "cm")
