#Dada una cadena desde teclado, remplazar los espacios por guiones
c1 = input()
c2 = ""
n = len(c1)
for i in range(n):
    if(c1[i] != " "):
        c2 = c2 + c1[i]
    else:
        c2 = c2+"-"
print(c2)
