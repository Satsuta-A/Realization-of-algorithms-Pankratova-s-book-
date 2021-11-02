from Squaring import  Squaring
def binary(x):
    y = ''

    while x > 0:
        y = str(x % 2) + y
        x = x // 2

    return  y

"""def Exponentiation(x,power):
    number_str = str(x)
    number_power = str(power)
    n = len(number_str)

    q = x
    if power01[n] = 1

    return int(''.join(map(str, answer))[::-1])"""

print(binary(10))