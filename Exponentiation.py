from Squaring import Squaring
def binary(x): #Фунция перевода в двоичную СС
    y = ''
    while x > 0:
        y = str(x % 2) + y
        x = x // 2

    return y

def Exponentiation(x,power): #Сама функция возведения в степень
    number_power_str = str(binary(power))
    n = len(number_power_str)
    power01 = list(map(int, list(number_power_str))) #Обработка входа
    power01.reverse()

    q = x #Шаг 1
    answer = x if power01[0] == 1 else 1

    for i in range(1, n):#Шаг 2
        q = Squaring(q) #Шаг 2.1
        if power01[i] == 1: #Шаг 2.2
            answer = answer * q

    return answer #Шаг 3/Ответ

def test(): #Функция проверки для случаев x^x
    for i in range(1, 1000):
        x = Exponentiation(i, i)
        if x == pow(i, i):
            print('Successfully! - ', x)
        else:
            print('Error! ', pow(i, i), ' <> ', x, 'i = ', i)
            exit

x = int(input('Введите x: '))
y = int(input('Введите y: '))
print(Exponentiation(x, y))