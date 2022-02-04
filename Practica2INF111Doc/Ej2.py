def NumMen(a):
    men = a[0]
    lon = len(a)
    y = ""
    Nul = "Nul"
    if lon > 1:
        for i in range(lon):
            if men > a[i]:
                men = a[i]
        for j in range(lon):
            if a[j] != men:
                y = y + a[j]
        return y
    else:
        return Nul


n = int(input())
print("agrega los numeros en linea recta separada por espacio")
a = list(map(int, input().split()))

lon = len(a)
for i in range(lon):
    a[i] = NumMen(str(a[i]))
    if a[i] != "Nul":
        a[i] = int(a[i])
print(a)
