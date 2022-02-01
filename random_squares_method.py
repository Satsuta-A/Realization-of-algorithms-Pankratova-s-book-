
from common_func import *
from random import randint

def rsm(n: int, factorbase: list):
    if isprime(n):
        raise BadNumberError('n - простое')
    factorbase_check(factorbase)

    while True:
        pars = []
        a = randint(1, n)
        while len(pars) <= len(factorbase):
            b = pow(a, 2, n)
            if razl_bool(b, factorbase):
                pars.append((a, b))
            a = (a+1) % n

        proda, prodb = 1, 1
        for par in pars:
            proda *= par[0]
            prodb *= par[1]
        prodb = int(pow(prodb, 0.5) % n)
        proda = proda % n

        if proda != prodb and proda != -prodb % n and proda ** 2 % n == prodb ** 2 % n:
            d = gcd(abs(proda - prodb), n)
            if 1 < d and d < n:
                return d

if __name__ == "__main__":
    n = 24961
    #n = 143
    factorbase = [3, 5]
    #factorbase = [2, 3, 5]
    d = rsm(n, factorbase)
    print(f'{d}; {n} / {d} = {n / d}')