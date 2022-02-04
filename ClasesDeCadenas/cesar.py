# Cifrar con cesar 1 una cadena.
cad1 = input()
cad2 = ""
alp = "abcdefghijklmnopqrstuvwxyz"  # 26
read = 0
for i in cad1:
    read = alp.find(i)
    read = (read + 1) % 26
    if i != " ":
        cad2 = cad2 + alp[read]
    else:
        cad2 = cad2 + " "
print(cad2)
