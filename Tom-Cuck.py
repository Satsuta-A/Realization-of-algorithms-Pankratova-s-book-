from common_func import BadNumberError
def poly(list, x):
    y = 0
    for i in range(len(list)):
        y += list[i][0] * (x ** list[i][1])
    return y

def repr(x):
    A = []
    lent =len(str(x))
    for i in range(lent):
        A.append([x % 10, i])
        x = x // 10
    return A

def Toom_Cook(u, v):
    if len(str(u)) != len(str(v)):
        raise BadNumberError('Одинаковой длины!')
    r, W = len(str(u)), []
    for i in range(2 * r - 1):
        W.append(poly(repr(u), i) * poly(repr(v), i)) #Находим значения в стандартных точках

    delta_ij, lenW = [], len(W)
    for i in range(lenW):
        delta_ij.append([W[i]])

    max, k = lenW, 1
    for j in range(lenW):#Находим коэфиценты для интерполяционной формулы Ньютона
        i = 0
        while i < max - 1:
            delta_ij[i].append((delta_ij[i+1][j]-delta_ij[i][j]) // k)
            i += 1
        k, max = k + 1, max - 1

    c_k, result = delta_ij[0], 0
    c_k.reverse()
    for i in range(len(c_k)):#Сразу считаем значение в x = 10 для получения числа
        k = len(c_k) - i - 2
        q = c_k[i]
        while k >= 0:
            q *= 10 - k
            k -= 1
        result += q
    return result

if __name__ == "__main__":
    print('Введите два числа одинковой длины.')
    u = int(input('Введите число 1: '))
    v = int(input('Введите число 2: '))

    result, check = Toom_Cook(u, v), v * u
    if check == result:
        print(f'Верно! ответ: {result}, должно быть: {check}')
