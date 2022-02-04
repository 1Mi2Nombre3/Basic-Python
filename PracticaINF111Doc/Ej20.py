#Dado un x>100, hallar el inverso del número.
x=int(input("Valor de x: "))
while x<= 100:
    x = int(input("Valor de x: "))

while x!=0:
    d=x%10
    x=x//10
    print(d,end="")