#inicio
a = input("Digite un número a: ")
b = input("Digite un número b: ")
c = input("Digite un número c: ")

if (a>c and c>b):
    print("Se ordena a,b,c: ",a,b,c)
else:
    if (a>c and c>b):
        print("Se ordena a,c,b: ",a,c,b)
    else:
        if (b>a and a>c):
            print("Se ordena b,a,c: ",b,a,c)
        else:
            if (b>c and c>a):
                print("Se ordena b,c,a",b,c,a)
            else:
                if (c>a and a>b):
                    print("se ordena c,a,b:", c,a,b)
                else:
                    print("se ordena c,b,a:", c,b,a)
#fin

