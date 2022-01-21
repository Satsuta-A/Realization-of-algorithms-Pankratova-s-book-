#сть не малое количество фэйлов при тест ~20%

import math
from common_func import gcd

def p_method(n):
    a, b = 2, 2
    while True:
        a = (pow(a, 2, n) + 1) % n
        b = (pow(b, 2, n) + 1) % n
        b = (pow(b, 2, n) + 1) % n

        d = gcd(a * b, n)

        if 1 < d and d < n:
            return d
        if d == n or d == 1:
            return 'FAIL'

if __name__ == "__main__":
    fails = 0
    succ = 0
    for x in range(1, 122):
        print(f'{x} divide by', p_method(x))
        if p_method(x) == 'FAIL':
            fails += 1
        else:
            succ += 1

    print(f'fails = {fails}, succsess = {succ}')