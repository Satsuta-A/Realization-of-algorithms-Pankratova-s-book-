from sympy import isprime
import numpy as np
from random import randint
import sympy as sp

class BadNumberError(Exception): #Для исключений
    pass

def binary_as_list(x): #Фунция перевода в двоичную СС
    y = []
    while x > 0:
        y.append(x % 2)
        x = x >> 1
    y.reverse()
    return y

def inverse_binary_as_list(list):
    list.reverse()
    k, result = 1, 0
    for i in list:
        result += i * (1 << k)
        k += 1
    return result >> 1

def log2(x): #Логарифм основания 2(цел)
    i = 0
    while x != 1:
        x = x // 2
        i += 1
    return i

def factorial(x): #Факториал
    if x == 0:
        return 1
    return factorial(x - 1) * x

def factorbase_check(factorbase: list):
    for i in factorbase:
        if not isprime(i):
            raise BadNumberError(f'В базе есть простое число!({i})')

def type_of_module(n: int):
    factors = factorize_dict(n)
    keys = list(factors.keys())
    if len(factors) == 0:
        return 1
    if len(keys) == 1:
        key, value = list(factors.items())[0]
        if key == 2:
            if value == 1:
                return 1
            elif value == 2:
                return 0
            else:
                return -1
        else:
            if value == 1:
                return 1
            else:
                return 0
    elif len(keys) == 2:
        lst = list(factors.items())
        key1, value1 = lst[0]
        if key1 == 2 and value1 == 1:
            return 0
        else:
            return -1
    else:
        return -1


def primRoots(mod: int):
    roots = []
    elements = set(num for num in range(1, mod) if gcd(num, mod) == 1)
    for g in range(1, mod):
        actual_set = set(pow(g, powers, mod) for powers in range(1, mod))
        if elements == actual_set:
            roots.append(g)
    if len(roots) == fi(fi(mod)):
        return roots
    else:
        print('len[roots] != fi(fi(mod))')

def fi(n):
    f = n
    if n % 2 == 0:
        while n % 2 == 0:
            n = n // 2
        f = f // 2
    i = 3
    while i*i <= n:
        if n % i == 0:
            while n % i == 0:
                n = n // i
            f = f // i
            f = f * (i-1)
        i = i + 2
    if n > 1:
        f = f // n
        f = f * (n-1)
    return f

def ord(a, mod):
    if a == 0:
        return False
    if a == 1:
        return [1, [1]]
    i = 1
    list = []
    list.append(a)
    while True:
        list.append(list[i - 1] * a % mod)
        i += 1
        if list[i - 1] == 1:
            #print('ord list:', a, list)
            return [i, list]

def generator_test(g, mod):
    if not isprime(mod):
        print('p - не простое число')
        return False
    phi = fi(mod)
    if pow(g, phi, mod) == 1 and gcd(g, mod) == 1 and pow(g, phi // 2, mod) - mod == -1 :
        factors = factorize(phi)
        for factor in factors:
            if pow(g, phi // factor, mod) == 1:
                print('g - не первовобразный корень')
                return False
    else:
        print('g - не первовобразный корень')
        return False
    return True

def factorize(n):
    factors = []
    if n < 0:
        factors.append(-1)
        n = -n
    p = 2
    while True:
        while n % p == 0 and n > 0:
            factors.append(p)
            n = n / p
        p += 1
        if p > n / p:
            break
    if n > 1:
        factors.append(int(n))
    return factors

def gcdExtended(a, b):
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = gcdExtended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y

def lcm(a, b):
    return a * b // gcd(a, b)

def myLegendre(a, p):
    ls = pow(a, (p - 1) // 2, p)
    return -1 if ls == p - 1 else ls

def myJacobi(a, n):
    n = factorize(n)
    res = 1
    for prime in n:
        res *= myLegendre(a, prime)
    return res

def gcd(a: int, b: int):
    k = 1
    while a != 0 and b != 0:
        while a & 1 == 0 and b & 1 == 0:
            a >>= 1
            b >>= 1
            k <<= 1
        while a & 1 == 0:
            a >>= 1
        while b & 1 == 0:
            b >>= 1
        if a >= b:
            a -= b
        else:
            b -= a
    return b * k

def sublist(lst1, lst2):
    for item in lst1:
        if not item in lst2:
            return False
    return True

def razl_bool(n: int, factorbase: list):
    if sublist(factorize(n), factorbase):
        return True
    else:
        return False

def razl(n: int, factorbase: list):
    factors = list(set(factorize(n)))
    factorbase_new = []
    for item in factorbase:
        column = [item, 0]
        factorbase_new.append(column)
    if n < 0:
        factors.remove(-1)
        factorbase_new[0][1] = 1
    else:
        factorbase_new[0][1] = 2


    for factor in factors:
        if not factor in factorbase:
            raise BadNumberError('В разложении есть число не из факторной базы')
        while n % factor == 0:
            n = n // factor
            i = factorbase.index(factor)
            factorbase_new[i][1] += 1
    return factorbase_new

def factorize_dict(n: int):
    lst = factorize(n)
    dict = {}
    for item in lst:
        if dict.get(item) == None:
            dict[item] = 1
        else:
            dict[item] += 1
    return dict

def divisors(n):
    from itertools import chain
    divs = lambda n: chain(*((d, n // d) for d in range(1, int(n ** 0.5) + 1) if n % d == 0))
    lst = list(set(divs(n)))
    lst.sort()
    lst.pop(0)
    return lst

def myPrimRoot(n: int):
    if type_of_module(n) == -1:
        return False

    phi = fi(n)
    factors = factorize(phi)
    g_list = []

    for g in range(2, n):
        if gcd(g, n) != 1:
            continue
        bol = True
        for factor in factors:
            if pow(g, phi // factor, n) == 1:
                bol = False
                break
        if bol:
            g_list.append(g)
    if fi(fi(n)) == len(g_list):
        return g_list
    else:
        print('Что-то пошло не так')

if __name__ == "__main__":
    for i in range(3, 18):
        if myPrimRoot(i):
            print(myPrimRoot(i))
            for all in myPrimRoot(i):
                print(sp.is_primitive_root(all, i))
