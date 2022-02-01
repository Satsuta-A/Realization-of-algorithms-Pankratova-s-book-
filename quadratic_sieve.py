from common_func import *
from random import randint
from sympy import nextprime

def razl(n: int,factorbase: list):
    factorbase.remove(-1)
    for p in factorbase:
        while not n % p == 0:
            n = n // p
    if n == 0:
        return True
    else:
        return False

def qs(n: int, k: int):
    factorbase = []
    factorbase.append(-1)
    factorbase.append(2)
    k += 2

    pred = 2
    while len(factorbase) < k:
        now = nextprime(pred)
        if myLegendre(n, now) == 1:
            factorbase.append(now)
        pred = now

    m = int(pow(n, 0.5))

    pars = []
    x = 0
    while len(pars) <= len(factorbase):
        a = x + m
        b = pow(x + m, 2) - n
        if razl(b, factorbase):
            pars.append((a, b))
        if x <= 0:
            x = abs(x) + 1
        else:
            x = -x

    x, y = 1, 1
    for par in pars:
        x *= par[0]
        y *= par[1]
    y = int(pow(y, 0.5) % n)
    x = x % n

    if x != y and x != -y % n and x ** 2 % n == y ** 2 % n:
        res = gcd(abs(x - y), n)
        if 1 < res and res < n:
            return res

if __name__ == "__main__":
    n = 214536
    #n = 143
    k = 3
    #k = 4
    res = qs(n, k)
    if res:
        print(f'Результат: {res}\nПроверка: {n} / {res} = {n / res}')