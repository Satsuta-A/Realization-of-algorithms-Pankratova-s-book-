from sympy import isprime

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

def primRoots(modulo):
    roots = []
    required_set = set(num for num in range(1, modulo) if gcd(num, modulo) == 1)

    for g in range(1, modulo):
        actual_set = set(pow(g, powers) % modulo for powers in range(1, modulo))
        if required_set == actual_set:
            roots.append(g)
    return roots

def fi(n):
    f = n;
    if n%2 == 0:
        while n%2 == 0:
            n = n // 2;
        f = f // 2;
    i = 3
    while i*i <= n:
        if n%i == 0:
            while n%i == 0:
                n = n // i;
            f = f // i;
            f = f * (i-1);
        i = i + 2;
    if n > 1:
        f = f // n;
        f = f * (n-1);
    return f;

def factorize(n):
    factors = []

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

def razl_bool(n: int,factorbase: list):
    for p in factorbase:
        if n < 0:
            continue
        while not n % p == 0:
            n = n // p
    if n == 0:
        return True
    else:
        return False

def razl_bool_spec(n: int,factorbase: list):
    factorbase.remove(-1)
    for p in factorbase:
        while not n % p == 0:
            n = n // p
    if n == 0:
        return True
    else:
        return False

def razl(n: int,factorbase: list):
    factorbase_new = []
    if razl_bool(n, factorbase):
        for i in range(len(factorbase)):
            factorbase_new.append([factorbase[i], 0])

        for i in range(len(factorbase)):
            while not n % factorbase_new[i][0] == 0:
                n = n // factorbase_new[i][0]
                factorbase_new[i][1] += 1
        return factorbase_new


#Переписать
def TCRT(remains: list, modules: list):

    def Check() -> bool:
        for i in range(len(modules) - 1):
            for j in range(i + 1, len(modules)):
                if gcd(modules[i], modules[j]) != 1:
                    print("The modules are not mutually prime")
                    return False

        if len(remains) == 0 or len(modules) == 0:
            print("No input data")
            return False

        if len(remains) != len(modules):
            print("Not enough input data")
            return False
        return True

    if not Check(): return -1

    r = len(modules)

    N = 1
    for n in modules:
        N *= n

    M = list(N // modules[i] for i in range(r))
    Z = list(map(lambda x, y: pow(x, -1, y), M, modules))

    x = 0
    for i in range(r):
        x += (remains[i] * M[i] * Z[i]) % N

    return x % N