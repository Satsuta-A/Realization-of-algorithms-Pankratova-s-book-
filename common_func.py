def binary(x): #Фунция перевода в двоичную СС
    y = ''
    while x > 0:
        y = str(x % 2) + y
        x = x // 2
    return y

def log2(x): #Логарифм основания 2(цел)
    i = 0
    while x != 1:
        x = x // 2
        i += 1
    return i

def factorial(x): #Факториал
    if x == 0:
        return 1
    return factorial(x - 1) * x

class BadNumberError(Exception): #Для исключений
    pass