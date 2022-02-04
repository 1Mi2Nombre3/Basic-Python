a,b = map(int,input("Enter 2 numbers integers: ").split())
x = 0
print("their numbers are ",a," y ", b, ",enter the module or a multiplication")
#m is the module or the multipliacation

m = str(input("Enter a symbol: "))

while m != "*" and m != "%":
    print("Please enter a valid symbol")
    m = str(input(" "))

if m == "*":
    x = a * b
    print("the result of your multiplication is: ",x)
else:
    x = a % b
    print("the result of your module is: ",x)