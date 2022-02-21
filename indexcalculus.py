from common_func import *
import sympy as sp
import numpy as np
from scipy.linalg import lstsq

def ic_log(a, g, n):
    t = log2(n) - 3
    factorbase = [2]
    for i in range(t):
        factorbase.append(sp.nextprime(factorbase[-1]))
    m = n - 1
    while True:
        while True:
            left_part_i = []
            right_part_i = []
            k_list = []
            k = randint(1, m)
            while len(left_part_i) <= t:
                while k in k_list:
                    k = randint(1, m)
                k_list.append(k)
                b = pow(g, k, n)
                factors = factorize(b)
                if sublist(list(set(factors)), factorbase):
                    dict = {}
                    for item in factors:
                        if dict.get(item) == None:
                            dict[item] = 1
                        else:
                            dict[item] += 1
                else:
                    continue

                left_part = []
                for item in factorbase:
                    if item in dict:
                        left_part.append(dict[item])
                    else:
                        left_part.append(0)

                left_part_i.append(left_part)
                right_part_i.append(k)

            lp = np.array(left_part_i)
            rp = np.array(right_part_i)
            try:
                log = lstsq(lp, rp)[0]
                break
            except Exception:
                continue

        log = list(map(int, log))
        log = list(map(lambda x: x % m, log))
        x = []
        while True:
            k_list = []
            k = randint(1, m)
            while k in k_list:
                k = randint(1, m)
            k_list.append(k)
            b = a * pow(g, k, n) % n
            factors = factorize(b)
            if sublist(list(set(factors)), factorbase):
                dict = {}
                for item in factors:
                    if dict.get(item) == None:
                        dict[item] = 1
                    else:
                        dict[item] += 1
            else:
                continue

            summ = 0
            for item in dict:
                summ = summ + dict[item] * log[factorbase.index(item)]
            x = (summ - k) % m
            if pow(g, x, n) == a:
                return x

if __name__ == "__main__":

    print('res', ic_log(13, 2, 37))
    print(sp.discrete_log(37, 13, 2))

    print('res', ic_log(17, 10, 47))
    print(sp.discrete_log(47, 17, 10))

    print('res', ic_log(94, 3, 101))
    print(sp.discrete_log(101, 94, 3))

    print('res', ic_log(1058, 2, 1117))
    print(sp.discrete_log(1117, 1058, 2))
