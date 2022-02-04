n = int(input())

while n < 1 or n >= 1000:
    n = int(input())

if n % 4 == 0:
    print("YES, multiplo de 4")
elif n % 7 == 0:
    print("YES, multiplo de 7")
elif n==444 or n==447 or n==474 or n==744:
    print("YES")
    print("HOLA")
elif n==777 or n==774 or n==747 or n==477:
    print("YES")
    print("ADIOS")
elif n==47 or n==74:
    print("YES")
else:
    print("NO")