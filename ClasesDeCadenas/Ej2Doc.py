#Cifrar con cesar 1 una cadena.
cad1 = input()
cad2=""
alp="abcdefghijklmnopqrstuvwxyz" #26
read = 0

for i in cad1:
    read = 0
    if i == " ":
        cad2 = cad2+" "
    for j in alp:
        read = read+1
        if read >= 26:
            read=0
        if i==j:
            cad2 = cad2 + alp[read]
print(cad2)
