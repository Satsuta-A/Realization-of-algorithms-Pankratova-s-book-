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
    print(factorbase)

    left_part_i = []
    right_part_i = []
    k1 = [1,13,25]
    c = 0
    print('t + c', t + c)
    while len(left_part_i) < t + c:
        print('l', len(left_part_i))
        #k = randint(1, n - 1)
        k = k1[c]
        print(k)
        c += 1
        b = pow(g, k, n)
        factors = factorize(b)

        if sublist(list(set(factors)), factorbase):
            dict = {}
            for item in factors:
                if dict.get(item) == None:
                    dict[item] = 1
                else:
                    dict[item] += 1
            print(dict)
        else:
            continue

        left_part = []
        for item in set(factors):
            if item in dict:
                left_part.append(dict[item])
            else:
                left_part.append(0)

        left_part_i.append(left_part)
        right_part_i.append(k)

    lp = np.array(left_part_i)
    rp = np.array(right_part_i)
    print(left_part_i, right_part_i)
    x = np.linalg.solve(lp, rp)
    log = list(map(int, x))
    log = list(map(x % n for x in log))
    x = []
    for a in args:
        while True:
            k = randint(0, n - 1)
            b = a * pow(g, k, n) % n
            factors = factorize(b)
            if sublist(list(set(factors)), factorbase):
                dict = {}
                for item in factors:
                    if dict.get(item) == None:
                        dict[item] = 1
                    else:
                        dict[item] += 1
                print(dict)
            else:
                continue

            summ = 0
            for item in dict:
                summ = summ + dict[item] * log[factors.index(item)]
            x.append((summ - k) % n)
    return x

if __name__ == "__main__":
    print(ic_log([13, 2, 37]))
    print(sp.discrete_log(37, 2, 13))