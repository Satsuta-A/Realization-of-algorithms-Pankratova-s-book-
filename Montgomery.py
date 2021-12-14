from common_func import *

def int_to_list_r(x):
    listi = list(str(x))
    listi.reverse()
    return list(map(int, listi))

def MR(x, b, k, m):
    if not gcd(m, 10) == 1 or not x < m * pow(b, k):
        raise BadNumberError('(m, 10) != 1')
    m1 = (- pow(m, -1, b)) % b

    y = x
    yl = int_to_list_r(y)

    for i in range(k):
        yl = int_to_list_r(y)
        u = yl[i] * m1 % b
        y = (y + u * m * pow(b, i)) // pow(b, k)
        if y >= m:
            y -= m

    return y

def MP(x, y, b, k, m):
    if not gcd(m, 10) == 1 or not x < m or not y < m:
        raise BadNumberError('(m, 10) != 1')
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

def MS(x, y, b, k, m):
    if not gcd(m, 10) == 1 or not x < m:
        raise BadNumberError('(m, 10) != 1')

    m1 = (- pow(m, -1, b)) % b
    y = binary_as_list(y)
    y.reverse()
    R2 = pow(b, 2 * k, m)
    x1 = MP(x, R2, b, k, m)
    z = x1

    for i in range(0, len(y) - 1):
        q = pow(z, 2)
        z = MR(q, b, k, m)
        if y[i] == 1:
            z = MP(z, x1, b, k, m)

    z = MR(z, b, k, m)
    return z


if __name__ == "__main__":
    print(MR(1234, 10, 2, 17))
    print(MP(12, 14, 10, 2, 17))
    print(MS(12, 14, 10, 2, 17))