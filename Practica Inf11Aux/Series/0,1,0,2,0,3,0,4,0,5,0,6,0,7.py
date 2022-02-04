# 1 0 1 2 0 3 0 4 0 5 0 6 0 7

n = int(input())

Nat=1
Ceros=0

res = 0

for i in range(0,n+1):
    if i % 2 == 0:
        res = Nat
        Nat = Nat + 1
    else:
        res = Ceros

    print(res,end=" ")

