#Dado 2 números intercambiar sus valores sin utilizar estructuras condicionales.
Num1 = int(input("Num1: "))
Num2 = int(input("Num2: "))

Num1 = Num1+Num2
Num2 = Num1-Num2
Num1 = Num1-Num2

print(Num1,Num2)
