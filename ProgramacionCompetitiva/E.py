n = int(input())
while n < 1 or n > 10000:
    n = int(input())
aux = 0

while n > aux:
    aux = aux + 3
    if aux > n:
        aux = aux - 3
        break
print(aux)
