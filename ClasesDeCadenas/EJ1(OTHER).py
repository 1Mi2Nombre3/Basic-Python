cad1 = input()
cad2 = ""
cad3 = ""
read= len(cad1)
for i in range(read):
    if cad1[i] == cad1[0]:
        cad3=cad1[i]
        cad2=cad2+cad3
        print(cad2)
    elif cad1[i] == " ":
        cad3=""