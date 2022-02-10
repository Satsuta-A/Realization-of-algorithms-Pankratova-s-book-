from common_func import *
def generator_test(g, mod):
    if not isprime(mod):
        print('p - не простое число')
        return False
    phi = fi(mod)
    if pow(g, phi, mod) == 1 and gcd(g, mod) == 1 and pow(g, phi // 2, mod) - mod == -1 :
        factors = factorize(phi)
        for factor in factors:
            if pow(g, phi // factor, mod) == 1:
                print('g - не первовобразный корень')
                return False
    else:
        print('g - не первовобразный корень')
        return False
    return True

def rho_pol_log(alpha, beta, n):
    if generator_test(alpha, n):
        x, a, b = [0], [0], [0]
        i = 1
        while True:

    else:
        return False


if __name__ == "__main__":
    pass