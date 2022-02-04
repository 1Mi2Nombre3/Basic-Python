#dec = int(input())
#bin(dec)
#print(int(bin(dec)[2:]))

#A base 3
n = int(input("Numero: "))
L=[]
while (n>=1):
    L.append(n%3)
    n = n//3
S=d[::-1]
for i in S:
    print(i, end="")