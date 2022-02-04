cad = input()
voc = "aeiou"
cad2 = ""
cv = 0

for i in range(len(cad)):
    cv = 0
    for j in range(len(voc)):
        if cad[i] == voc[j]:
            cad2 = cad2 + voc[(j - 1)]
            cv = 1
    if cv == 0:
        cad2 = cad2 + cad[i]
print(cad2)
