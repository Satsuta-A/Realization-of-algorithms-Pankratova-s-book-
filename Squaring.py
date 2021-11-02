def Squaring(x):
    number_str = str(x)
    n = len(number_str)
    list_of_digits, answer = list(map(int, list(number_str))), [0 for i in range(2 * n)] # Шаг 1
    list_of_digits.reverse()

    for i in range(n): # Шаг 2
        doub = answer[2 * i] + pow(list_of_digits[i], 2) # Шаг 2.1
        answer[2 * i], c = doub % 10, 0

        for j in range(i + 1, n): # Шаг 2.2
            trip = answer[i + j] + 2 * list_of_digits[i] * list_of_digits[j] + doub // 10
            answer[i + j] = trip % 10
            doub = trip

        answer[i + j + 1] += doub // 10 # Шаг 2.3

    return int(''.join(map(str, answer))[::-1]) # Шаг 3

def test():
    for i in range(10, 1000):
        x = Squaring(i)
        if x == i * i:
            print('Successfully! - ', x)
        else:
            print(i * i, ' <> ', x,'\nError! i = ', i)
            exit

print(Squaring(12345676543241233467))
