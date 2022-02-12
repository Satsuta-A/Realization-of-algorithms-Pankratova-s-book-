from common_func import BadNumberError as BNE
def Square_root_extraction(a):
    if a < 0:
        raise BNE('Больше нуля!')
    x = a
    while True:
        x0 = x
        x = (a // x + x) // 2

        if x >= x0:
            return x0

def test():
    for x in range(6391):
            if int(x ** (0.5)) != Square_root_extraction(x):
                print(f'Error! x = {x}')
                exit
    print('Success!')

if __name__ == "__main__":
    x = int(input('Введите a: '))
    print(f'{Square_root_extraction(x)}, а если проверить: {int(x**(0.5))}')
    #test()