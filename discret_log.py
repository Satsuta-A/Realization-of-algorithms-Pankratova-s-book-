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

def rho_log_pankratova(alpha, betta, n, p):
    global S1, S2, S3
    S1, S2, S3 = [], [], []
    for i in range(0, p):
        if i % 3 == 1:
            S1.append(i)
        elif i % 3 == 2:
            S2.append(i)
        elif i % 3 == 0:
            S3.append(i)

    def x_next(x: int):
        #print('x', x)
        if x in S1:
            #print('xS1')
            return betta * x % p
        elif x in S2:
            #print('xS2')
            return x * x % p
        elif x in S3:
            #print('xS3')
            return alpha * x % p

    def a_next(a: int, x: int):
        #print('a', a)
        if x in S1:
            #print('aS1')
            return a
        elif x in S2:
            #print('aS2')
            return 2 * a % n
        elif x in S3:
            #print('aS3')
            return (a + 1) % n

    def b_next(b: int, x: int):
        #print('b',b)
        if x in S1:
            #print('bS1')
            return (b + 1) % n
        elif x in S2:
            #print('bS2')
            return 2 * b % n
        elif x in S3:
            #print('bS3')
            return b

    def xab_next(x, a, b):
        xab = [x_next(x), a_next(a, x), b_next(b, x)]
        return xab

    xab1 = [1, 0, 0]
    xab2 = [1, 0, 0]
    while True:
        xab1 = xab_next(xab1[0], xab1[1], xab1[2])
        h = xab_next(xab2[0], xab2[1], xab2[2])
        xab2 = xab_next(h[0], h[1], h[2])
        #print(xab1, xab2)
        if xab1[0] == xab2[0]:
            break
    r = (xab1[2] - xab2[2]) % n
    if r == 0:
        return False
    d = gcd(r, n)
    x = (xab2[1] - xab1[1])//d * pow(r // d, -1, n // d) % (n // d)
    z = [x]
    while len(z) != d:
        z.append(z[-1] + n // d)
    for i in z:
        if pow(alpha, i, p) == betta:
            return i

def rho_log(alpha, betta, n, p, a0=0, b0=0):
    #if generator_test(alpha, p):
    global S1, S2, S3
    S1, S2, S3 = [], [], []
    for i in range(0, n):
        if i % 3 == 1:
            S1.append(i)
        elif i % 3 == 0:
            S2.append(i)
        elif i % 3 == 2:
            S3.append(i)

    def x_next(x: int):
        #print('x', x)
        if x in S1:
            #print('xS1')
            return betta * x % n
        elif x in S2:
            #print('xS2')
            return x * x % n
        elif x in S3:
            #print('xS3')
            return alpha * x % n

    def a_next(a: int, x: int):
        #print('a', a)
        if x in S1:
            #print('aS1')
            return a
        elif x in S2:
            #print('aS2')
            return 2 * a % p
        elif x in S3:
            #print('aS3')
            return (a + 1) % p

    def b_next(b: int, x: int):
        #print('b',b)
        if x in S1:
            #print('bS1')
            return (b + 1) % p
        elif x in S2:
            #print('bS2')
            return 2 * b % p
        elif x in S3:
            #print('bS3')
            return b

    def xab_next(x, a, b):
        xab = [x_next(x), a_next(a, x), b_next(b, x)]
        return xab

    if not (a0 == 0 and b0 == 0):
        x = pow(alpha, a0) * pow(betta, b0)
    else:
        x = 1

    xab = [[x, a0, b0]]
    xup_put = xab_next(xab[0][0], xab[0][1], xab[0][2])
    xab.append(xup_put)
    for i in range(2, n):
        xup_put = xab_next(xab[i-1][0], xab[i-1][1], xab[i-1][2])
        xab.append(xup_put)
    #print(xab)
    for i in range(1, n):
        if xab[i][0] == xab[2 * i][0]:
            r = (xab[i][2] - xab[2 * i][2]) % p
            if r == 0:
                #return False
                return rho_log(alpha, betta, p, n, randint(1, p - 1), randint(1, p - 1))
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
    """p = 191
    n = 383
    a = 2
    b = 228"""
    """a = 89
    b = 799
    p = 101
    n = 809"""
    """a = 2
    b = 5
    n = 29
    p = 28
    print(rho_log(a, b, n, p))
    print(sp.discrete_log(n, b, a), BSGS(a, b, n))"""
######################################################
    """n = 191
    p = 383
    a = 2
    b = 228"""
    """a = 89
    b = 799
    n = 101
    p = 809"""
    """a = 3
    b = 17525607
    p = 23661857
    n = 739433"""
    a = 5
    b = 2943
    p = 23663
    n = 11831
    #print(sp.discrete_log(p, b, a), BSGS(a, b, p))
    print(rho_log_pankratova(a, b, n, p))