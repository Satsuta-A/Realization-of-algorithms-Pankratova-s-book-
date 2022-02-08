from sympy import isprime
import numpy as np

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
    if n < 0:
        factors.append(-1)
        n = -n
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

def sublist(lst1, lst2):
    for item in lst1:
        if not item in lst2:
            return False
    return True

def razl_bool(n: int, factorbase: list):
    if sublist(factorize(n), factorbase):
        return True
    else:
        return False

def razl(n: int, factorbase: list):
    factors = list(set(factorize(n)))
    factorbase_new = []
    for item in factorbase:
        column = [item, 0]
        factorbase_new.append(column)
    if n < 0:
        factors.remove(-1)
        factorbase_new[0][1] = 1
    else:
        factorbase_new[0][1] = 2


    for factor in factors:
        if not factor in factorbase:
            raise BadNumberError('В разложении есть число не из факторной базы')
        while n % factor == 0:
            n = n // factor
            i = factorbase.index(factor)
            factorbase_new[i][1] += 1
    return factorbase_new

def cV(c: list, V: list):
    """for i in range(len(V)-1):
        cs = 0
        for j in range(len(c)):
            cs += c[j] * V[j][i]
        if cs % 2 != 0:
            return False
    return True"""

    O = list(np.dot(c, V) % 2)
    if O == [0] * (len(V) - 1):
        return True
    else:
        return False

def search_c(V: list):
    decisions = []
    c = 2 ** (len(V) - 1)
    while c < 2 ** len(V):
        for i in range(len(V)):
            lst = binary_as_list(c)
            if cV(lst, V):
                if i == len(V) - 1:
                    decisions.append(binary_as_list(c))
                continue
            else:
                break
        c += 1
    c = 2 ** (len(V) - 2)
    while c < 2 ** (len(V) - 1):
        for i in range(len(V)):
            lst = [0] + binary_as_list(c)
            if cV(lst, V):
                if i == len(V) - 1:
                    decisions.append([0] + binary_as_list(c))
                continue
            else:
                break
        c += 1
    if decisions != []:
        return decisions


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