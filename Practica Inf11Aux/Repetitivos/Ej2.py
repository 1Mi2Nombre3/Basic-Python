x = int(input())
D = 0
while x<=0 or x>=1001:
    x = int(input())
for i in range(1,x+1):
    R = x%i
    if R == 0:
        R = 1
        D = R+D
print(D)