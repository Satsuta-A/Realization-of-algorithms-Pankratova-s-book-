def ss_convect(num: int, base: int):
    if not (2 <= base <= 9):
        quit()
    newNum = ''
    while num > 0:
        newNum = str(num % base) + newNum
        num //= base
    return newNum

mod = 3
base = 5
for i in range(36):
    if i % mod == 0:
        print(i % mod, 'Accept Число:',  ss_convect(i, base))
    else:
        print(i % mod, 'Reject Число:', ss_convect(i, base))