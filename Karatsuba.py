from common_func import BadNumberError
def decimical_full(x):
    l = []
    l.append(len(str(x)))
    l.append(x // (10**(l[0] // 2)))
    l.append(x % (10**(l[0] // 2)))
    return l

def karatsuba(u, v):

    if len(str(u)) != len(str(v)) or len(str(u)) % 2 != 0:
        raise BadNumberError('Одинаковых по длине числа, чётной длины!')

    U, V = decimical_full(u), decimical_full(v)
    A, B = U[1] * V[1], U[2] * V[2]
    C = (U[1]+U[2])*(V[1]+V[2])

    return A * (10 ** (U[0])) + (C - A - B) * (10 ** (U[0] // 2)) + B


if __name__ == "__main__":
    print('Введите два одинаковых по длине числа, чётной длины')
    u = int(input('Введите первое число: '))
    v = int(input('Введите второе число: '))

    print(f'Результат быстрого умножения: {karatsuba(u, v)}')
    print(f'Результат простого умножения: {u * v}')