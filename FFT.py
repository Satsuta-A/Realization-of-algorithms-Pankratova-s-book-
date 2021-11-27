from scipy.fft import fft, fftfreq
from common_func import log2
from math import pi, e


def okr(comple):
    c = 0j
    num1 = round(comple.real, 1)
    num2 = round(comple.imag, 1)
    c = complex(int(num1 + (0.5 if num1 > 0 else -0.5)), int(num2 + (0.5 if num2 > 0 else -0.5)))
    return c

def comp(A, x):
    print(A)

    for i in range(len(A) // 2):
        A[i], A[d-i-1] = A[d-1-i], A[i]
    sA = 0
    for i in range(len(A)):
        sA += A[i]*pow(x, i)
    print('Сумма', sA)
    return sA

def FFT(A):
    global l, p2i
    p2i = 2 * pi * 1j
    l = pow(e, p2i)
    l = okr(l)
    n = pow(2, log2(len(A)) + 1)
    w = okr(pow(e, p2i / n))
    return FFTW(A, w)

def FFTW(A, w):
    d = len(A)
    for i in range(d // 2):
        A[i], A[d-i-1] = A[d-1-i], A[i]
    n = pow(2, log2(d) + 1)
    while d != n:
        A.append(0)
        d += 1

    for i in range(n // 2):
        A[i], A[n-i-1] = A[n-1-i], A[i]
    print('Вызов', A, w)
    if w == l:
        return comp(A, w)
    A0, A1 = [], []
    for i in range(len(A)):
        if i % 2 == 0:
            A0.append(A[i])
        else:
            A1.append(A[i])

    A0 = FFTW(A0, okr(pow(w, 2)))
    A1 = FFTW(A1, okr(pow(w, 2)))

    A_w = []
    for i in range(n):
        print(i)
        A_w[i] = comp(A0, okr(pow(w, 2*i))) + okr(pow(w, i)) * comp(A1, okr(pow(w, 2*i)))
    return A_w


if __name__ == "__main__":
    A = [1, 2]
    print(FFT(A))