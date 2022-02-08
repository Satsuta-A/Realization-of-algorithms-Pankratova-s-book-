from common_func import *
from random import randint
from sympy import nextprime

def ruzl(n: int,factorbase: list):
    factorbase.remove(-1)
    for p in factorbase:
        while not n % p == 0:
            n = n // p
    if n == 1:
        return True
    else:
        return False

def qs(n: int, k: int):
    factorbase = []
    factorbase.append(-1)
    factorbase.append(2)
    k += 2

    m = int(pow(n, 0.5))
    while True:
        pred = 2
        while len(factorbase) < k:
            now = nextprime(pred)
            if myLegendre(n, now) == 1:
                factorbase.append(now)
            pred = now

        t, x = k + 1, 0
        e, v, pars = [], [], []
        while len(pars) <= t:
            a = x + m
            b = pow(x + m, 2) - n
            if razl_bool(b, factorbase):
                e_i = []
                for item in razl(b, factorbase):
                    e_i.append(item[1])
                v_i = [i % 2 for i in e_i]
                e.append(e_i)
                v.append(v_i)
                pars.append([a, b])
            if x <= 0:
                x = abs(x) + 1
            else:
                x = -x

        T = []
        for i in range(t):
            if sum(v[i]) % 2 == 0:
                T.append(i)

        I = []
        for i in range(len(factorbase)):
            c = 0
            if i in T:
                for j in range(len(factorbase)):
                    c += e[i][j]
            c = c // 2
            I.append(c)

        y = 1
        for j in range(len(factorbase)):
            y *= pow(factorbase[j], I[j], n) % n

        x = 1
        for par in pars:
            x *= par[0] % n

        if gcd(x - y, n) != 1:
            return gcd(x - y, n)

if __name__ == "__main__":
    n = 214536
    k = 3
    res = qs(n, k)
    print(f'Результат: {res}\nПроверка: {n} / {res} = {n / res}')