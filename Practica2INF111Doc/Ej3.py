cad = input()
cad2 = ""
for i in range(len(cad)):
    if cad[i] != " ":
        cad2 = cad2 + cad[i]
    else:
        cad2 = cad2 + "$"
print(cad2)