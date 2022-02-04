n = int(input())
L = [0] * n
for i in range(n):
    print("cad: ", i+1)
    L[i] = input()

x = input("elemento a buscar: ")
print(L)
c = 0
for j in range(n):
    lon = len(L[j])
    aux = L[j]
    for k in range(lon):
        if aux[k] == x:
            c = c + 1

print("el elemento [", x, "] se halla", c, "veces")
