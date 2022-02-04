n=int(input())
while n<2 or n>100:
    n = int(input())
a=0
c=0
for i in range(n):
   n1=int(input())
   if n1%7==0:
       c=c+1
       a=a+n1
       if c>=2:
           print(a)
           a=n1

