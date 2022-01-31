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

def gcd(a: int, b: int) -> int:
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

def pt_gladcost(n : int, factorbase: list):
    for i in factorbase:
        while not n % i == 0:
            n = n // i
    if n <= max(factorbase):
        return True
    else:
        return False

#Переписать
def TCRT(remains: list, modules: list) -> int:

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