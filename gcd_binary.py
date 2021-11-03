from  Exponentiation import Exponentiation as pov
from numpy import gcd
from common_func import BadNumberError

def gcd_binary(a,b):
    if a <= 0 or b <= 0:
        raise BadNumberError('a или b <= нуля!')

    i, a1 = 0, a
    while a1 % 2 != 1:
        a1 = a1 // 2
        i += 1

    j, b1 = 0, b
    while b1 % 2 != 1:
        b1 = b1 // 2
        j += 1

    a, b = a1, b1
    k = i if i < j else j

    while a != b:
        if a < b:
            a, b = b, a
        c = a - b

        s, c1 = 0, c
        while c1 % 2 != 1:
            c1 = c1 // 2
            s += 1

        a = c1

    return pov(2, k) * a

def test():
    for i in range(600, 639):
        for j in range(i-1, i+3):
            if gcd(i, j) != gcd_binary(i ,j):
                print(f'Error! a = {i}, b = {j}')
                exit
            else:
                print(f'Success! - gsd = {gcd_binary(i, j)}')

if __name__ == "__main__":
    x = int(input('Введите a: '))
    y = int(input('Введите b: '))
    print(gcd_binary(x, y))
    #test()