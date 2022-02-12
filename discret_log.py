from common_func import *
from collections import OrderedDict

def BSGS(alpha: int, betta: int, n: int):

    def serch_j_in_list_of_pairs(betta, lst: list):
        for pair in lst:
            if pair[1] == betta:
                return pair[0]

    alpha, betta = alpha % n, betta % n
    m = int(np.sqrt(n)) + 1
    lst = []
    for j in range(m):
        lst.append([j, pow(alpha, j, n)])
    lst.sort(key=lambda tup: tup[1])
    alphar = pow(alpha, -m, n)
    list_of_second_components = [pair[1] for pair in lst]
    for i in range(m):
        if betta in list_of_second_components:
            return i * m + serch_j_in_list_of_pairs(betta, lst)
        else:
            betta = betta * alphar % n

    return 'Log не существует!'


def rho_pol_log(alpha, beta, n):
    if generator_test(alpha, n):
        x, a, b = [0], [0], [0]
        i = 1
        while True:
            pass
    else:
        return False

def call_BSGC():
    while True:
        n = int(input('n: '))
        if type_of_module(n) == -1:
            print('Неподходящий модуль: ')
            continue

        betta = int(input('betta: '))
        roots = myPrimRoot(n)
        if len(roots) < 25:
            for root in roots:
                print(f'Результат: {BSGS(root, betta, n)};')
                print(f'Проверка: {sp.discrete_log(n, betta, root)}')
        else:
            true, false = 0, 0
            for root in roots:
                if BSGS(root, betta, n) == sp.discrete_log(n, betta, root):
                    true += 1
                else:
                    false += 1
            print(f'Успехи, неудачи: {true}, {false};')
        if input() == '-':
            break
        else:
            continue

if __name__ == "__main__":
    """n = 11
    print(myPrimRoot(n))
    alpha, betta = 2, 10
    print('Результат:', BSGS(alpha, betta, n))
    print('Проверка: ', sp.discrete_log(n, betta, alpha))"""
#########################################################################################################
    call_BSGC()
