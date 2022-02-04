n = int(input())
a = 0
b = ""

num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
rom = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

while n != 0:
    for i in range(n // num[a]):
        b = b + rom[a]
        n = n - num[a]
    a = a + 1
print(b)
