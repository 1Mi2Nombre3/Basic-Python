x=int(input())
while x<=0:
    x=int(input())
y=0
while x!=0:
    d=x%10
    x=x//10
    y=(y*10)+d
print("Invertido: ",y)