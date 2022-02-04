C = input()
c = 0
for i in range(len(C)):
    if C[i] == "!":
        c += 1
print(c)