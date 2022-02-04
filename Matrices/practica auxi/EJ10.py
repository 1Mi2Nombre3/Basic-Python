### MODULO ###

def EliRep(l1, l):
    find = False
    for i in range(len(l1)):
        if x == l1[i]:
            find = True
    return find

### MAIN ###

n = int(input())
while n > 10 ** 5:
    n = int(input())
a = list(map(str, input().split()))
x = ""
for i in a:
    x = x + i
print(x)

a = ""
for j in x:
    cv = 0
    for k in x:
        if j == k:
            cv = cv + 1
    if cv >= 2:
        a = a + j
L = []
for i in a:
    L.append(i)
print(L)