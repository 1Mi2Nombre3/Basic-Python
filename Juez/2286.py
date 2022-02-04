a = input()
b = input()
lonA = len(a)
lonB = len(b)
c = 0
c1 = 0
L=[]
for i in range(lonB):
    if a[c] == b[i]:
        c = c + 1
        if c == lonA:
            c1 = i - (c-1)
            L.append(c1)
            c = 0
    else:
        c = 0

print(L)
