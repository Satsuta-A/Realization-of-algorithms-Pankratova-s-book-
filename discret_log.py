from common_func import *

def BSGS(alpha: int, betta: int, n: int):

    def search_j_in_list_of_pairs(betta, lst: list):
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
            return i * m + search_j_in_list_of_pairs(betta, lst)
        else:
            betta = betta * alphar % n

    return 'Log не существует!'


def rho_log(alpha, betta, p, n, a0=0, b0=0):
    #if generator_test(alpha, p):
    global S1, S2, S3
    S1, S2, S3 = [], [], []
    for i in range(1, p):
        if i % 3 == 1:
            S1.append(i)
        elif i % 3 == 0:
            S2.append(i)
        elif i % 3 == 2:
            S3.append(i)

    def x_next(x: int):
        if x in S1:
            return betta * x % n
        elif x in S2:
            return x * x % n
        elif x in S3:
            return alpha * x % n

    def a_next(a: int, x: int):
        if x in S1:
            return a
        elif x in S2:
            return 2 * a % p
        elif x in S3:
            return (a + 1) % p

    def b_next(b: int, x: int):
        if x in S1:
            return (b + 1) % p
        elif x in S2:
            return 2 * b % p
        elif x in S3:
            return b

    def xab_next(x, a, b):
        return [x_next(x), a_next(a, x), b_next(b, x)]

    if not (a0 == 0 and b0 == 0):
        x = pow(alpha, a0) * pow(betta, b0)
    else:
        x = 1

    xab = [[x, a0, b0]]
    xab.append(xab_next(*xab[0]))
    print(xab)
    print(xab_next(xab[1][0], xab[1][1], xab[1][2]))
    for i in range(1, p):
        xab.append(xab_next(xab[i-1][0], xab[i-1][1], xab[i-1][2]))
    #print(xab)
    for i in range(1, p):
        #h = xab[-1]
        #xab.append(xab_next(*h))
        #print(xab)
        #for j in range(i+1, 2 * i):
            #h = xab[j]
            #print(h)
            #xab.append(xab_next(*h))
        #xab[2 * i][0], xab[2 * i][1], xab[2 * i][2] = xab[2 * i][0] % p, xab[2 * i][1] % p, xab[2 * i][2] % p
        #print(xab[i], xab[2 * i])
        if xab[i][0] == xab[2 * i][0]:
            """for item in xab:
                print(item)"""
            print('yey')
            r = (xab[i][2] - xab[2 * i][2]) % p
            if r == 0:
                return False
                #return rho_log(alpha, betta, p, n, randint(1, p - 1), randint(1, p - 1))
            else:
                return pow(r, -1, p) * (xab[2 * i][1] - xab[i][1]) % p
    #else:
        #return False

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
    #call_BSGC()
    n = 383
    p = 191
    a = 2
    b = 228
    print(sp.primitive_root(p))
    print(sp.primitive_root(n))
    print(sp.is_primitive_root(2, 383))
    #print(myPrimRoot(n))
    print(rho_log(a, b, p, n), sp.discrete_log(n, b, a), BSGS(a, b, n))
