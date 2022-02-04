n=int(input())
im=3
m4=4

for i in range(1,n+1):
    if i%3==0:
        print(m4,end=" ")
        m4=m4+4
    else:
        print(im,end=" ")
        im=im+2