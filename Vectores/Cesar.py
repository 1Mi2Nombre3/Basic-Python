def Cesar(cad1):
    cad2 = ""
    alp = "abcdefghijklmnopqrstuvwxyz"
    read = 0
    for i in cad1:
        read = alp.find(i)
        read = (read + 1) % 26
        if i != " ":
            cad2 = cad2 + alp[read]
        else:
            cad2 = cad2 + " "
    print(cad2)


cad = input()
Cesar(cad)
