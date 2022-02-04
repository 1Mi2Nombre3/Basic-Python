#Ej18
n=int(input("Valor de N elementos: "))
while n<=0:
    n=int(input("Valor de N elementos: "))
a=2
S=0
for i in range(1,n+1):
    S=S+((a*i)/i)
print(S)