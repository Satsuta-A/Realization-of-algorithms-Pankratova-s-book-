from common_func import BadNumberError as BNE
def Square_root_extraction(a):
    if a < 0:
        raise BNE('Больше нуля!')
    x = a    
    
    x0 = x
    
    while x < x0:
        x = (a // x + x) // 2
    return int(x0 ** (0.5))

def test():
    for x in range(6391):
            if int(x ** (0.5)) != Square_root_extraction(x):
                print(f'Error! x = {x}')
                exit
    print('Success!')

if __name__ == "__main__":
    x = int(input('Введите a: '))
    print(f'{Square_root_extraction(x)}, а если проверить: {int(x**(0.5))}')
    test()
