from common_func import gcd
from sympy import isprime
def p_method(n):
    a, b = 2, 2
    while True:
        a = (pow(a, 2) + 1) % n
        b = (pow(b, 2) + 1) % n
        b = (pow(b, 2) + 1) % n

        d = gcd(a - b, n)

        if 1 < d and d < n:
            return d
        if d == n:
            return 'FAIL'

if __name__ == "__main__":
    print(p_method(75361))
    """fails = 0
    succ = 0
    for x in range(1, 1000000):
        if not isprime(x):
            #print(f'{x} divide by', p_method(x))
            if p_method(x) == 'FAIL':
                fails += 1
            else:
                succ += 1

    print(f'Fails: {fails};\nSuccsess: {succ};\nTotal: {fails+succ};\nChance of succsess: {succ/(fails+succ)};')"""