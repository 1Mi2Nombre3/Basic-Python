x=int(input())
cd=0
while x != 0:
    d=x%10
    x=int(x/10)
    cd=cd+1
print("Cant. dig: ",cd)