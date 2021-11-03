from Squaring import Squaring
from common_func import binary

def Exponentiation(x,power): #Сама функция возведения в степень
    if power == 0:
        return 1
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
    print('Тесты')
    for i in range(12345690824735728342104, 12345690824735728342121):
        x = Exponentiation(i, i)
        if x == pow(i, i):
            print('Successfully! - ', x)
        else:
            print('Error! ', pow(i, i), ' <> ', x, 'i = ', i)
            exit

if __name__ == "__main__":
    x = int(input('Введите x: '))
    y = int(input('Введите y: '))
    print(Exponentiation(x, y))
    test()