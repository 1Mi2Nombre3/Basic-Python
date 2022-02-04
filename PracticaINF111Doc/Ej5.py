#Dado 2 números enteros positivos, determinar si uno es múltplo de otro.

a=int(input("Num1: "))
while a <= 0:
    a = int(input())
b=int(input("Num2: "))
while b <= 0:
    b = int(input())

if a % b == 0:
    print("Si es múltiplo")
elif b % a == 0:
    print("Si es múltiplo")
else:
    print("No es múltiplo")
