import math

n = int(input())
cd = int(math.log10(n)+1)
L = []
L1 = []
while n != 0:
    d = n // int(math.pow(10, cd - 1))
    n = n % int(math.pow(10, cd - 1))
    cd = cd - 1
    L.append(d)

cv = 0
cv1 = 0
cv2 = 0
for i in range(len(L)):
    if cv == 0:
        if cv1 == 0:
            if L[i] == 3:
                L1.append(L[i])
                cv = 1
                cv1 = 1
            else:
                L1.append(L[i])
        else:
            if cv2 == 0:
                if L[i] == 7:
                    L1.append(L[i])
                    cv = 1
                    cv2 = 1
                else:
                    if L[i] != 3:
                        L1.append(L[i])
            else:
                if L[i] != 7:
                    L1.append(L[i])
    else:
        cv = 0
x = ""
for i in L1:
    x = x + str(i)
print(x)
