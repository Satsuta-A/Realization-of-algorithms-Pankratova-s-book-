##########ЧЕРНОВИК###########

#число - список, деление с остатком
number = [1, 3, 1]
divisor = [2, 3, 1]
mod = 6
r = []
q = []
from sympy import mod_inverse
import sys
import sympy as sp
from sympy.abc import x
def stolbik(number, divisor, mod):
    number = [x % mod for x in number]
    divisor = [x % mod for x in divisor]
    while number != [] and number[0] == 0:
        number.pop(0)
    while divisor != [] and divisor[0] == 0:
        divisor.pop(0)
    if len(number) < len(divisor):
        return (0, number)
    elif divisor == []:
        return False
    q = []
    def substolbik(number, divisor, mod):
        fs = number[0]
        try:
            print(mod_inverse(divisor[0], mod))
            q_i = fs * mod_inverse(divisor[0], mod) % mod
        except Exception:
            return (q, number)
        tmp = [q_i * x for x in divisor] + [0]*(len(number) - len(divisor))
        q.append(q_i)
        for i in range(len(tmp)):
            number[i] = (number[i] - tmp[i]) % mod
        print(q, number)
        if len(number) > 0 and number[0] == 0:
            number.pop(0)
        print(q, number)
        if len(number) < len(divisor):
            return (q, number)
        else:
            return substolbik(number, divisor, mod)
    res = substolbik(number, divisor, mod)
    if q == []:
        return (0, number)
    return res

print(stolbik(number, divisor, mod))