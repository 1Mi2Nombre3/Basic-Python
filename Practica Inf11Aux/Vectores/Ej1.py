N = int(input())
S1 = 0
S = []
SL = []
SL2 = []
C = 0
aux = 0
for i in range(N):
    V = int(input())
    S1 += V
    S.append(S1)

lon = len(S)

if S1 % 2 == 0:
    for i in range(lon):
        if i+1 == lon:
            SL2.append(S[i])
    for j in range(0,lon-1):
        SL2.append(S[j])
    for k in SL2:
        print(k, end=" ")
else:
    for i in range(1, lon):
        if C == 0:
            aux = S[0]
        SL.append(S[i])
        C = 1
    SL.append(aux)
    for i in SL:
        print(i, end=" ")
