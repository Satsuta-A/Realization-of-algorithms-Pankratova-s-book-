#сть не малое количество фэйлов при тест ~20%
import math

from common_func import gcd
from random import randint
from math import log
from sympy import isprime
def help_B(n):
    i = -1
    while n > 0:
        n //= 10
        i += 1
    return i

def p_1_pollard(n):
    #B = int(input(f'n ~ {help_B(n)}\n'))
    B = 20

    a = randint(2, n-1)
    d = gcd(a, n)
    if d == 2:
        return d

    for q in range(B+1):
        if isprime(q):
            l = math.floor(math.log(110) // math.log(11))
            a = pow(a, pow(q, l), n)

    d = gcd(a - 1, n)

    if d == 1 or d == n:
        return 'FAIL'
    else:
        return d





if __name__ == "__main__":
    for x in range(100000, 200000):
        print(p_1_pollard(x))