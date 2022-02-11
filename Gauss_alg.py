from common_func import *
from random import randint
def Gauss_alg(mod: int):
    alpha = [randint(1, mod)]
    t = [ord(alpha[0], mod)[0]]
    i = 0
    counter = 0
    while counter <= 100:
        if t[i] == mod - 1:
            return alpha[i]
        betta = randint(1, mod)
        while betta in ord(alpha[i], mod)[1]:
            betta = randint(1, mod)
        s = ord(alpha[betta], mod)[0]
        if s == mod - 1:
            alpha.append(betta)
        else:
            e, d = cringe(lcm(t[i], s))
            print(gcd(e, d))
            alpha.append(pow(alpha[i], t[i]//d) * pow(betta, s // e))
            t.append(lcm(t[i], s))
            i += 1
        counter += 1

if __name__ == "__main__":
    #print(Gauss_alg(37))
    primes = '3	2	107	2	251	6	409	21	577	5	743	5	929	3 109	6	257	3	419	2	587	2	751	3	937	5 7	3	113	2	263	5	421	2	593	3	757	2	941	2 11	2	127	3	269	2	431	7	599	7	761	6	947	2 13	2	131	2	271	6	433	5	601	7	769	11	953	3 17	3	137	3	277	5	439	15	607	3	773	2	967	5 19	2	139	2	281	3	443	2	613	2	787	2	971	2 23	5	149	2	283	3	449	3	617	3	797	2	977	3 29	2	151	6	293	2	457	13	619	2	809	3	983	5 31	3	157	5	307	5	461	2	631	3	811	3	991	6 37	2	163	2	31 1	17	463	3	641	3	821	2	997	7'
    test_list = list(map(int, primes.split()))
    prime_roots = []
    for i in range(0, len(test_list)-1, 2):
        prime_roots.append([test_list[i], test_list[i+1]])
    for i in range(len(prime_roots)//10):
    for item in prime_roots:
        t = 0
        f = 0
        if Gauss_alg(item[0]) == item[1]:
            t += 1
        else:
            f += 1
    print(f'true: {t}\nfalse: {f}')




"""    prime_roots = [[3	2]	[107	2]	[251	6]	[409	21]	[577	5]	[743	5]	[929	3]
[109	6]	[257	3]	[419	2]	[587	2]	[751	3]	[937	5]
[7	3]	[113	2]	[263	5]	[421	2]	[593	3]	[757	2]	[941	2]
[11	2]	[127	3]	[269	2]	[431	7]	599	7	761	6	947	2
13	2	131	2	271	6	433	5	601	7	769	11	953	3
17	3	137	3	277	5	439	15	607	3	773	2	967	5
19	2	139	2	281	3	443	2	613	2	787	2	971	2
23	5	149	2	283	3	449	3	617	3	797	2	977	3
29	2	151	6	293	2	457	13	619	2	809	3	983	5
31	3	157	5	307	5	461	2	631	3	811	3	991	6
37	2	163	2	31 1	17	463	3	641	3	821	2	997	7]"""