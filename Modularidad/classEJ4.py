# dado un N desde teclado, si N es par mostrar la serie fibonaci de lo contrario mostrar los multiplos de 5
def ParImpar(N):
    if N % 2 == 0:
        a = 1
        b = 0
        for i in range(N):
            a = a + b
            b = a - b
            print(b, end=" ")
    else:
        for j in range(1,N+1):
            if j % 5 == 0:
                print(j, end=" ")

                
N = 0
while N >= 0:
    N = int(input())
    ParImpar(N)
