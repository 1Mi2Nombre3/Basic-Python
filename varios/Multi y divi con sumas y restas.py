A=int(input())
B=int(input())
C=int(input())
a1=A
c1=C
R=0
c=0
for i in range(1,B+1):
    if i!=1:
        a=A
        for j in range(1,a1):
            A=A+a
for k in range(A):
    C=C+c1
    c=c+1
    if C==A:
        C=A
        break
    elif C>A:
        C=C-c1
        break

R=A-C
a1=str(a1)
B=str(B)
c1=str(c1)
print("Resultado: [("+a1+"^"+B+")/"+c1+")] = ",c)
print("Residuo: ",R)



