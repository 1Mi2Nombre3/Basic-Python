y=0
x=int(input())
while x>100:
    d=x%10
    y=(y*10)+d
    x = int(input())
print(y)