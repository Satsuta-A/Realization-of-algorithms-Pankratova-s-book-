def binary(x): #Фунция перевода в двоичную СС
    y = ''
    while x > 0:
        y = str(x % 2) + y
        x = x // 2
    return y

def log2(x):
    i = 0
    while x != 1:
        x = x // 2
        i += 1
    return i

class BadNumberError(Exception): #Для исключений
    pass