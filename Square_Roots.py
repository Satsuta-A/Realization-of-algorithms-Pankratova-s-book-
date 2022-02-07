from common_func import *
from random import randint
def sr_a_mod_p_odd(a, p):
    if not p % 2 == 1:
        print(f'p = {p} Должно быть нечётным')
        return False
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

def sr_a_mod_3_4(a, p):
    if not p % 4 == 3 or myLegendre(a, p) == -1:
        return False
    r = pow(a, (p+1) // 4, p)
    return (r, -r)

def sr_a_mod_3_8(a, p):
    if not p % 8 == 5 or myLegendre(a, p) == -1:
        return False
    d = pow(a, (p - 1) // 4, p)
    if d == 1:
        r = pow(a, (p + 3) // 8, p)
    elif d == p - 1:
        r = 2 * a * pow(4 * a, (p - 5) // 8, p) % p
    return (r, -r)

def sr_aQ_mod_p(a, p):
    pass

def sr_a_mod_pq(a, p):
    pass

if __name__ ==  "__main__":
    p = 29
    for a in range(1, p):
        print(sr_a_mod_p_odd(a, p), sr_a_mod_3_4(a, p), sr_a_mod_3_8(a, p), 'Проверка a:', a)