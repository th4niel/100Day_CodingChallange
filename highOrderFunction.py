def add(n1, n2):
    return n1 + n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1/n2

def substract(n1, n2):
    return n1 - n2

def calculator(n1, n2, calc):
    return calc(n1, n2)


result = calculator(10, 5, multiply)

print(result)