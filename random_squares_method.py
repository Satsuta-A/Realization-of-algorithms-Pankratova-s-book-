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
            if pt_gladcost(b, factorbase):
                pars.append((a, b))
            a = (a+1) % n

        x, y = 1, 1
        for par in pars:
            x *= par[0]
            y *= par[1]
        y = int(pow(y, 0.5) % n)
        x = x % n

        if pow(x, 2, n) == pow(y, 2, n) and x != y and x != -y % n:
            res = gcd(abs(x - y), n)
            if 1 < res and res < n:
                return res


if __name__ == "__main__":

    n = 214536
    factorbase = [7, 11]
    res = rsm(n, factorbase)
    if res:
        print(f'Результат: {res}\nПроверка: {n} / {res} = {n / res}')