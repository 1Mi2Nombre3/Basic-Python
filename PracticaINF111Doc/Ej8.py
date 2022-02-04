#Determinar si un número es capicua.

import math
n=int(input("Num: "))
while n<=0:
    n = int(input("Num: "))

nd=int(math.log10(n))+1
n1=n
d=0
nc=0

for i in range(nd):
    d=n%10
    n=n//10
    nc=(nc*10)+d

if n1 == nc:
    print("Si capicua")
else:
    print("No capicua")