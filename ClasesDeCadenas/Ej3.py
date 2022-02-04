cad1=input()
read= len(cad1)
L=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
cad2=""
L2=[]

for i in range(read):
    cad2=cad1[i]
    for j in L:
        if cad2 == j:
            L.remove(j)
if L==L2:
    print("NO SE IGNORO A NINGUN CARACTER")
else:
    for k in L:
        print(k,end="")