from common_func import *
from random import randint
def square_roots_a_mod_p_odd(a, p):
    if not p % 2 == 1:
        print(f'p = {p} Должно быть нечётным')
    if a < 1 or a > p - 1:
        a = a % p

    if myLegendre(a, p) == -1:
        return False
    b = randint(1, p - 1)
    while myLegendre(b, p) != -1:
        b = randint(1, p - 1)

    t = p - 1
    s = 0
    while t % 2 == 0:
        t = t // 2
        s += 1

    gcd, x, y = gcdExtended(a, p)
    a_rev = x % p

    c = pow(b, t, p)
    r = pow(a, (t+1)//2, p)

    for i in range(1, s):
        d = pow(pow(r, 2) * a_rev, pow(2, s - i - 1), p)
        if d % p == p - 1:
            r = r * c % p
        c = pow(c, 2, p)

    return (r, -r)

if __name__ ==  "__main__":
    p = 11
    for a in range(1, p):
        if square_roots_a_mod_p_odd(a, p) != False:
            print(square_roots_a_mod_p_odd(a, p), 'Проверка a, test_a:', a, pow(square_roots_a_mod_p_odd(a, p)[0], 2, p))