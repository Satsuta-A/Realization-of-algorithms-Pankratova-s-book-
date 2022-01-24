from math import log, floor
from common_func import gcd
from random import randint
from sympy import isprime
def p_1_pollard(n):
    if not isprime(n):
        B = 20
        a = randint(2, n-1)
        d = gcd(a, n)
        if d == 2:
            return d

        for q in range(B+1):
            if isprime(q):
                l = floor(log(n) // log(q))
                a = pow(a, pow(q, l), n)

        d = gcd(a - 1, n)

        if d == 1 or d == n:
            return 'FAIL'
        else:
            return d

if __name__ == "__main__":
    fails = 0
    succ = 0
    for x in range(100000, 1000000):
        if p_1_pollard(x) == 'FAIL':
            fails += 1
            #print(x, p_1_pollard(x))
        else:
            succ += 1
    print(f'Fails: {fails};\nSuccsess: {succ};\nTotal: {fails + succ};\nChance of succsess: {succ / (fails + succ)};')