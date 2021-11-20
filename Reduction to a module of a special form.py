from Exponentiation import Exponentiation as pov
def Spec_form(x, m, b = 10):
    bN,i = 1, 1
    while bN*b <= m:
        bN *= b
        i += 1
    bN = pov(b, i)
    c = bN - m

    r = x % bN
    q = (x - r) // bN

    while q > 0:
        qc = q * c
        rN = qc % bN
        qN = (qc - rN) // bN
        r, q = r + rN, qN
    while r >= m:
        r -= m
    return r

def test():
    for i in range(11, 10000):
        for j in range(i-10, i):
            if not Spec_form(i, j) == i % j:
                print(f'Error! x = {i}, m = {j}')
                exit
    print('Тесты успешно пройден!')

if __name__ == "__main__":
    x = int(input('Введите число x: '))
    m = int(input('Введите число m: '))
    #b = int(input('Введите число b: '))

    print('Ответ: ', Spec_form(x, m))
    print('Должно быть: ', x % m)
    #test()
