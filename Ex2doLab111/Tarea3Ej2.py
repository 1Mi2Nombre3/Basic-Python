def part(L):
    p = L[0]
    men = []
    may = []
    for i in range(1, len(L)):
        if L[i] < p:
            men.append(L[i])
        else:
            may.append(L[i])
    return men, p, may


def quick(L):
    if len(L) < 2:
        return L
    men, p, may = part(L)
    return quick(men) + [p] + quick(may)


n = int(input("tamaño del vector: "))
L = [0] * n
print("Elementos")
for i in range(n):
    L[i] = int(input())
print(L)

print(quick(L))
