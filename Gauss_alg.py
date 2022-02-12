from common_func import *
def cringe(n: int, t: int, s: int):
    dict = factorize_dict(n)
    e, d = 1, 1
    for item in dict.keys():
        if s % e * pow(item, dict[item]):
            e *= pow(item, dict[item])
        else:
            d *= pow(item, dict[item])
    return e, d

def Gauss_alg(mod: int):
    alpha_next = randint(2, mod-1)
    #t_next = ord(alpha_next, mod)[0]
    while True:
        print('Cycle start')
        alpha_pred = alpha_next
        #t_pred = t_next
        o = ord(alpha_pred, mod)
        t_pred, order = o[0], o[1]
        if t_pred == mod - 1:
            return alpha_pred
        betta = randint(2, mod-1)
        while betta in order:
            betta = randint(2, mod-1)
        s = ord(betta, mod)[0]
        if s == mod - 1:
            alpha_next = betta
        else:
            e, d = cringe(lcm(t_pred, s), t_pred, s)
            alpha_next = pow(alpha_pred, t_pred // d, mod) * pow(betta, s // e, mod)

if __name__ == "__main__":
    #до ~10000000 1000000007
    p = 104149
    print(sp.primitive_root(p))
    print(sp.isprime(p))
    '''
    104149, 104161, 104173, 104179, 104183, 104207, 104231, 104233, 104239, 104243, 104281, 104287, 104297, 104309, 104311, 104323, 104327, 104347, 104369, 104381, 104383, 104393, 104399, 104417, 104459, 104471, 104473, 104479, 104491, 104513, 104527, 104537, 104543, 104549, 104551, 104561, 104579, 104593, 104597, 104623, 104639, 104651, 104659, 104677, 104681, 104683, 104693, 104701, 104707, 104711, 104717, 104723, 104729
    '''
    #print('Confirmed roots', primRoots(p))
    g = Gauss_alg(p)
    print(g, sp.is_primitive_root(g, p))
    """primes = '107	2	251	6	409	21	577	5	743	5	929	3 109	6	257	3	419	2	587	2	751	3	937	5 7	3	113	2	263	5	421	2	593	3	757	2	941	2 11	2	127	3	269	2	431	7	599	7	761	6	947	2 13	2	131	2	271	6	433	5	601	7	769	11	953	3 17	3	137	3	277	5	439	15	607	3	773	2	967	5 19	2	139	2	281	3	443	2	613	2	787	2	971	2 23	5	149	2	283	3	449	3	617	3	797	2	977	3 29	2	151	6	293	2	457	13	619	2	809	3	983	5 31	3	157	5	307	5	461	2	631	3	811	3	991	6 37	2	163	2	31 1	17	463	3	641	3	821	2	997	7'
    test_list = list(map(int, primes.split()))
    prime_roots = []
    for i in range(0, len(test_list)-1, 2):
        prime_roots.append([test_list[i], test_list[i+1]])
    l = len(prime_roots)
    for i in range(l - l):
        prime_roots.pop()
    t = 0
    f = 0
    for item in prime_roots:
        g = Gauss_alg(item[0])
        if Gauss_alg(item[0]) in primRoots(item[0]):
            print(g, 'p:', item[0])
            #item[1]:
            t += 1
        else:
            f += 1
    print(f'true: {t}\nfalse: {f}')"""