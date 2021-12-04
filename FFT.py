from scipy.fft import fft, fftfreq
from common_func import *

def binary_as_list_const_len(x, k):
    y = []
    while x > 0:
        y.append(x % 2)
        x = x // 2
    while len(y) < k:
        y.append(0)
    y.reverse()
    return y
"""
def module(x, mod):
    if x >= 0:
        while x >= mod:
            x -= mod
    else:
        while x < 0:
            x += mod
    return x"""

def rev(x, k):
    number = binary_as_list_const_len(x, k)
    number.reverse()
    return inverse_binary_as_list(number)

def FFT(a, w):
    k = log2(len(a)) + 1
    n = pow(2, k)
    if n > len(a):
        n = n >> 1
        k -= 1
    mod = pow(w, n // 2) + 1
    if pow(w, n, mod) != 1:
        raise BadNumberError('W должен быть примитивным корнем!')

    S, R = [], []
    for i in a:
        R.append(i)
        S.append(i)
    for l in range(k-1, -1, -1):
        for i in range(n):
            S[i] = R[i]
        for i in range(n):
            index = binary_as_list_const_len(i, k)
            index_paste0 = [x for x in index]
            index_paste1 = [x for x in index]

            index_paste0[l-1] = 0
            index_paste1[l-1] = 1

            index_paste0 = inverse_binary_as_list(index_paste0)
            index_paste1 = inverse_binary_as_list(index_paste1)

            w_deg = pow(w, rev((i // pow(2, l)), k))

            R[i] = (S[index_paste0] + w_deg * S[index_paste1]) % mod

    b = []
    for i in range(n):
        b.append(R[rev(i, k)])

    return b

if __name__ == "__main__":
    #4321 2
    a = list(map(int, list(input('Введите коэффиценты: '))))
    w = int(input('Введите примитивный корень: '))

    print(f'Результат FFT: {FFT(a, w)}')