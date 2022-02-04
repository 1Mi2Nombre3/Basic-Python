def sumA(a, b):
    return a + b


def restA(a, b):
    return a - b


def calculadora(a, b, f):
    return f(a, b)


a = 3
b = 4
print(sumA(a, b))
print(restA(a, b))
print(calculadora(a, b, sumA))
print(calculadora(a, b, restA))
