from Exponentiation import Exponentiation as pov
def Barretts_modulo(x, m, b = 10):
    x_str, m_str = str(x), str(m) #Обработка входа
    x_list, m_list = list(map(int, list(x_str))), list(map(int, list(m_str)))
    x_list.reverse()
    m_list.reverse()
    n = len(m_str)
    z = int(pov(b, 2 * n) / m)

    q = int(int(x / pov(b, n - 1)) * z / pov(b, n + 1)) #Шаг 1
    r1, r2 = x % pov(b, n + 1), (q * m) % pov(b, n + 1)#Шаг 2

    if r1 > r2: #Шаг 3
        r = r1 - r2
    else:
        r = pov(b, n + 1) + r1 - r2
    while r > m: #Шаг 4
        r -= m

    return r #Шаг 5

def test():
    for i in range(11, 10000):
        for j in range(i-10, i):
            if Barretts_modulo(i, j) == i % j:
                pass
            else:
                print(f'Error! x = {i}, m = {j}')
                exit

if __name__ == "__main__":
    x = int(input('Введите число x: '))
    m = int(input('Введите число m: '))
    #b = int(input('Введите число b: '))

    print('Ответ: ', Barretts_modulo(x, m))
    print('Должно быть: ', x % m)
    test()