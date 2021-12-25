from common_func import *

def int_to_list_r(x):
    listi = list(str(x))
    listi.reverse()
    return list(map(int, listi))
"""
MR(x, R, m) = x * R^(-1) mod m, где НОД(R, m) = 1 или же  НОД(b, m) = 1, где R = b^k
"""
def MR(x, m, b = 10):
    k = len(str(m))
    if not gcd(m, 10) == 1 or not x < m * pow(b, k):
        raise BadNumberError('(m, 10) != 1 and x < m * b^k')
    m1 = (- pow(m, -1, b)) % b
    y = x
    print(k)
    yl = int_to_list_r(y)
    for i in range(k):
        yl = int_to_list_r(y)
        u = yl[i] * m1 % b
        y = (y + u * m * pow(b, i))
    y = y // pow(b, k)
    if y >= m:
        y -= m
    return y
"""
MP(x, y, b, k, m) =  x * y * b^(-k) mod m, (m,b) = 1 and x,y < m
"""
def MP(x, y, m, b = 10):
    if not gcd(m, b) == 1 or not x < m or not y < m:
        raise BadNumberError('(m, 10) != 1 and x,y < m')
    k = len(str(m))
    m1 = (- pow(m, -1, b)) % b
    z = 0
    yl, xl = int_to_list_r(y), int_to_list_r(x)
    for i in range(k):
        zl = int_to_list_r(z)
        u = (zl[0] + xl[i] * yl[0]) * m1 % b
        z = (z + xl[i] * y + u * m) // b
    if z >= m:
        z -= m

    return z

def MS(x, y, m, b=10):
    if not gcd(m, 10) == 1 or not x < m:
        raise BadNumberError('(m, 10) != 1 and x < m')

    k = len(str(m))
    m1 = (- pow(m, -1, b)) % b
    y = binary_as_list(y)
    y.reverse()
    R2 = pow(b, 2 * k, m)
    x1 = MP(x, R2, m)
    z = x1

    for i in range(0, len(y) - 1):
        q = pow(z, 2)
        z = MR(q, m)
        if y[i] == 1:
            z = MP(z, x1, m)

    z = MR(z, m)
    return z


if __name__ == "__main__":
    #12 14 2 17
    x = int(input('x:'))
    m = int(input('m:'))
    print('MR = ', MR(x, m))
    print('Входные данные для MP')
    x = int(input('Введите x: '))
    y = int(input('Введите y: '))
    m = int(input('Введите m: '))
    print(MP(x, y, m), ',должно быть =', MR(x * y % m, m))
    print(MS(10, 2, 17), pow(10, 2, 17))