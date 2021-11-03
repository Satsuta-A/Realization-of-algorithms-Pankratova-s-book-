def binary(x): #Фунция перевода в двоичную СС
    y = ''
    while x > 0:
        y = str(x % 2) + y
        x = x // 2

    return y

class BadNumberError(Exception): #Для исключений
    pass
