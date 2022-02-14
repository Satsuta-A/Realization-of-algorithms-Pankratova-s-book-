from common_func import *
from random import randint
import galois as gl
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

    return  (r, (-r) % p)

def sr_a_mod_3_4(a, p):
    if a < 1 or a > p - 1:
        a = a % p
    if not p % 4 == 3 or myLegendre(a, p) == -1:
        return False
    r = pow(a, (p+1) // 4, p)
    return  (r, (-r) % p)

def sr_a_mod_3_8(a, p):
    if a < 1 or a > p - 1:
        a = a % p
    if not p % 8 == 5 or myLegendre(a, p) == -1:
        return False
    d = pow(a, (p - 1) // 4, p)
    if d == 1:
        r = pow(a, (p + 3) // 8, p)
    elif d == p - 1:
        r = 2 * a * pow(4 * a, (p - 5) // 8, p) % p
    return  (r, (-r) % p)

def sr_aQ_mod_p(a, p):
    if a < 1 or a > p - 1:
        a = a % p
    if p % 2 == 0 or myLegendre(a, p) == -1:
        return False
    b = randint(1, p)
    while myLegendre((pow(b, 2, p) - 4 * a) % p, p) != -1:
        b = randint(1, p)

    GF = gl.GF(p)
    b = (-b) % p
    f, r = gl.Poly([1, b, a], field=GF), gl.Poly([1, 0], field=GF)
    deg = (p + 1) // 2
    print(r**deg % f)
    r = ((r ** deg) % f).integer % p

    return (r, (-r) % p)

def sr_a_mod_pq(a, n):
    primes = factorize(n)
    if len(primes) == 1:
        for prime in primes:
            if prime % 8 == 5:
                return sr_a_mod_3_8(a, prime)
            elif prime % 4 == 3:
                return sr_a_mod_3_4(a, prime)
            else:
                return sr_a_mod_p_odd(a, prime)
    p, q = primes[0], primes[1]
    if a < 1 or a > p - 1:
        a = a % p
    if p % 2 == 0 or myLegendre(a, p) == -1 or q % 2 == 0 or myLegendre(a, q) == -1:
        return False
    rs = []
    for prime in primes:
        if prime % 8 == 5:
            rs.append(sr_a_mod_3_8(a, prime))
        elif prime % 4 == 3:
            rs.append(sr_a_mod_3_4(a, prime))
        else:
            rs.append(sr_a_mod_p_odd(a, prime))

    gcd, c, d = gcdExtended(p, q)
    r, s = rs[0][0], rs[1][0]
    x = (r * d * q + s * c * p) % n
    y = (r * d * q - s * c * p) % n
    x, y = x % n, y % n
    return (x, (-x) % n, y, (-y) % n)

if __name__ ==  "__main__":
    #while True:
    """        a = input('Число a: ')
    if a == '-':
    break
    a = int(a)
    p = int(input('Модуль: '))"""
    a = 245643
    p = 1567981
    print(f'Ответ: {sr_aQ_mod_p(a, p)} {sp.sqrt_mod(a, p)}')
    a = 2
    p = 7
    print(f'Ответ: {sr_aQ_mod_p(a, p)} {sp.sqrt_mod(a, p)}')
    a = 6
    p = 7
    print(f'Ответ: {sr_aQ_mod_p(a, p)} {sp.sqrt_mod(a, p)}')
    a = 4
    p = 7
    print(f'Ответ: {sr_aQ_mod_p(a, p)} {sp.sqrt_mod(a, p)}')
    a = 40000
    p = 104161
    print(f'{sp.sqrt_mod(a, p)}')
    print(f'Ответ: {sr_aQ_mod_p(a, p)} ')