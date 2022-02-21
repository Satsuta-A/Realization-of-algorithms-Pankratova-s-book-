from common_func import *
import sympy as sp
import numpy as np

def ic_log(*args):
    c = 0
    args = list(args[0])
    n = args[-1]
    args.pop()
    g = args[-1]
    args.pop()
    t = log2(n) - 3
    factorbase = [2]
    for i in range(t):
        factorbase.append(sp.nextprime(factorbase[-1]))
    #print(factorbase)
    m = n - 1
    while True:
        left_part_i = []
        right_part_i = []
        k_list = []
        k = randint(1, m)
        while len(left_part_i) <= t + c:
            while k in k_list:
                k = randint(1, m)
            k_list.append(k)
            #print('step 1', k)
            b = pow(g, k, n)
            factors = factorize(b)
            #print(b, factors)
            if sublist(list(set(factors)), factorbase):
                dict = {}
                for item in factors:
                    if dict.get(item) == None:
                        dict[item] = 1
                    else:
                        dict[item] += 1
                #print(dict)
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
        #print(lp, rp)
        try:
            log = np.linalg.solve(lp, rp)
            #print('Suuccccc')
            break
        except Exception:
            continue

    log = list(map(int, log))
    #print(log)
    log = list(map(lambda x: x % m, log))
    """print(lp, rp)
    print(log)"""
    x = []
    for a in args:
        while True:
            k_list = []
            k = randint(1, m)
            while k in k_list:
                k = randint(1, m)
            k_list.append(k)
            #k = randint(1, m)
            #print('step 2', k)
            b = a * pow(g, k, n) % n
            factors = factorize(b)
            if sublist(list(set(factors)), factorbase):
                dict = {}
                for item in factors:
                    if dict.get(item) == None:
                        dict[item] = 1
                    else:
                        dict[item] += 1
                #print(dict)
            else:
                continue

            summ = 0
            for item in dict:
                summ = summ + dict[item] * log[factorbase.index(item)]
            x.append((summ - k) % m)
            break
    return x

if __name__ == "__main__":
    print(ic_log([17, 10, 47]))
    print(sp.discrete_log(47, 17, 10))

    print(ic_log([13, 2, 37]))
    print(sp.discrete_log(37, 13, 2))