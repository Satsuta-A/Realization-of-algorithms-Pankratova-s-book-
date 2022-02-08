import math

from common_func import *
import numpy as np
from sympy import nextprime

def qs(n: int, k: int):
    factorbase = []
    factorbase.append(-1)
    factorbase.append(2)

    m = int(pow(n, 0.5))

    pred = 2
    while len(factorbase) < k:
        now = nextprime(pred)
        if myLegendre(n, now) == 1:
            factorbase.append(now)
        pred = now

    t = k + 1
    h = 0
    while True:
        pars = []
        V, E = [], []
        while len(pars) != t:
            a = h + m
            b = pow(h + m, 2) - n
            if razl_bool(b, factorbase):
                pars.append([a, b])
                e = []
                for item in razl(b, factorbase):
                    e.append(item[1])
                E.append(e)
                V.append(list(map(lambda x: x % 2, e)))
            if h <= 0:
                h = abs(h) + 1
            else:
                h = -h
        decisions = search_c(V)
        for c in decisions:
            cd = c[:]
            I = []
            for item in c:
                if item == 1:
                    I.append(c.index(item) + 1)
                    c[c.index(item)] = 0
            c = cd
            b = 1
            for j in range(k):
                sum = 0
                for i in range(t):
                    sum += c[i] * E[i][j]
                b *= pow(factorbase[j], sum)

            x, y = 1, np.sqrt(b)
            for i in I:
                x *= pars[i-1][0] % n
            x, y = int(x), int(y)
            if x % n != y % n and x % n != (-y) % n and x ** 2 % n == y ** 2 % n:
                d = gcd(abs(int(x + y)), n)
                if 1 < d and d < n:
                    return d
        t += 1

if __name__ == "__main__":
    n = 24961
    k = 12
    res = qs(n, k)
    print(f'Результат: {res}\nПроверка: {n} / {res} = {n / res}')
    n = 214536
    k = 12
    #k = 6
    res = qs(n, k)
    print(f'Результат: {res}\nПроверка: {n} / {res} = {n / res}')
    n = 91
    k = 12
    res = qs(n, k)
    print(f'Результат: {res}\nПроверка: {n} / {res} = {n / res}')