import math
while (True):
    try:
        n,k = map(int,input().split())
        suma = 0
        numero = 0
        for i in range(n):
            suma += ((i+k)/(i+2+k))
        suma =  math.ceil(suma)
        print(suma)
    except EOFError:
        break;