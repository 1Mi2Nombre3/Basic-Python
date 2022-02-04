#Dada una frase con caracteres del alfabeto ingles de minusculas y espacios. De cada palabra mostrar las vocales que no se usan, en el mismo orden.
T=int(input())
for i in range(T):
    cad1=input()
    n=len(cad1)
    L=["a","e","i","o","u"]
    L1=[]
    for i in range(n):
        if cad1[i]=="a" or cad1[i]=="e" or cad1[i]=="i" or cad1[i]=="o" or cad1[i]=="u":
            L1.append(cad1[i])
        elif cad1[i]==" ":
            print(L1)
            L1=[]
    print(L1)








