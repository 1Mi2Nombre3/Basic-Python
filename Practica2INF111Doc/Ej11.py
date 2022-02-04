n = int(input("tamaño de vector 1: "))
L = [0] * n
for i in range(len(L)):
    L[i] = input()
n1 = int(input("tamaño de vector 2: "))
L1 = [0] * n1
for j in range(len(L1)):
    L1[j] = input()
n2 = int(input("tamaño de vector 3: "))
L2 = [0] * n2
for k in range(len(L2)):
    L2[k] = input()

print(L)
print(L1)
print(L2)

nR = n + n1 + n2
LR = [0] * nR
cv = 1
cv1 = 1
a = 0
b = 0
c = 0
for i in range(nR):
    if cv == 1:
        if a < n:
            LR[i] = int(L[a])
            a = a + 1
            cv = 2
        else:
            if b < n1:
                LR[i] = int(L1[b])
                b = b + 1
                cv = 3
            elif c < n2:
                LR[i] = int(L2[c])
                c = c + 1
                cv = 1
    elif cv == 2:
        if b < n1:
            LR[i] = int(L1[b])
            b = b + 1
            cv = 3
        else:
            if c < n2:
                LR[i] = int(L2[c])
                c = c + 1
                cv = 1
            elif a < n:
                LR[i] = int(L[a])
                a = a + 1
                cv = 2
    elif cv == 3:
        if c < n2:
            LR[i] = int(L2[c])
            c = c + 1
            cv = 1
        elif a < n:
            LR[i] = int(L[a])
            a = a + 1
            cv = 2
        elif b < n1:
            LR[i] = int(L1[b])
            b = b + 1
            cv = 2
print()
print(LR)
