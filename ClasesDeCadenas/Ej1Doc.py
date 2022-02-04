#Dada 1 cadena generar una segunda cadena intercalando las palabras entre mayusculas y minusculas.
c1=input()
c2=""
c=0
for i in c1:
    if i == " ":
        c=c+1
    if c % 2 != 0:
        a=i.lower()
    else:
        a=i.upper()
    c2=c2+a
print(c2)