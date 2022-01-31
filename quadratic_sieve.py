from common_func import *
def qs(n: int, factorbase: list):
    factorbase_check(factorbase)
    factorbase.insert(0, -1)

    m = int(pow(n, 0.5))

    x = 0
    pars = []
    while True:
        for i in range(len(factorbase)+1):
            b = pow(x+m, 2)
            if not pt_gladcost(b, factorbase):
                break
            else:
                vi = []
                ei = []
                for j in factorbase:
                    vk = 0
                    while not n % j == 0:
                        n = n // j
                        vk += 1
                    ei.append((vk, factorbase.index(j)))
                    vi.append((vk % 2, factorbase.index(j)))
                pars.append((x+m, b))
        if x <= 0:
            x = abs(x) + 1
        else:
            x = -x

"""    T = []
    for v in vi:
        if v[0] == 0:
            T.append(v[1])
    x = 1
    for i in T:
        x *= pars[i][0]

    l = []
    for i in range(len(factorbase)):
        tmp = 0
        for j in T:
            tmp +="""

