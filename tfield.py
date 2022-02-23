from numpy.polynomial import Polynomial as P
from sympy import mod_inverse
def stolbik(number, divisor, mod):
    number = [x % mod for x in number]
    divisor = [x % mod for x in divisor]
    while number != [] and number[0] == 0:
        number.pop(0)
    while divisor != [] and divisor[0] == 0:
        divisor.pop(0)
    if len(number) < len(divisor):
        return ([0], number)
    elif divisor == []:
        return False
    q = []
    def substolbik(number, divisor, mod):
        fs = number[0]
        try:
            print(mod_inverse(divisor[0], mod))
            q_i = fs * mod_inverse(divisor[0], mod) % mod
        except Exception:
            return (q, number)
        tmp = [q_i * x for x in divisor] + [0]*(len(number) - len(divisor))
        q.append(q_i)
        for i in range(len(tmp)):
            number[i] = (number[i] - tmp[i]) % mod
        while number[0] == 0:
            number.pop(0)
        if len(number) < len(divisor):
            return (q, number)
        else:
            return substolbik(number, divisor, mod)
    res = substolbik(number, divisor, mod)
    if q == []:
        return ([0], number)
    return res

class tfield:
    ##Подумать как обощить равенство mod и удаление нулевых в начале до не пустого списка
    def __init__(self, mod, *args):
        self.mod = mod
        self.items = [int(x) % self.mod for x in args]
        self.tflen = len(args)
        while len(self.items) != 1 and self.items[0] == 0:
            self.items.pop(0)
    def __len__(self):
        return self.tflen
    def __str__(self):
        return str(self.items)
    def __repr__(self):
        return str(self.items)
    def __getitem__(self, i):
        return self.items[self.tflen - i - 1]
    def __setitem__(self, key, value):
        self.items[self.tflen - key - 1] = int(value)
    def __abs__(self):
        integer = 0
        for i in range(self.tflen):
            integer += self.items[i] * pow(10, i)
    def __add__(self, elem):
        if isinstance(elem, tfield):
            if self.mod != elem.mod:
                return "different mod!"

            elem1 = self.items[:]
            elem2 = elem.items[:]

            if len(elem1) > len(elem2):
                for _ in range(len(elem1) - len(elem2)):
                    elem2.insert(0, 0)
            elif len(elem1) < len(elem2):
                for _ in range(len(elem2) - len(elem1)):
                    elem1.insert(0, 0)

            new_elem = elem1
            for i in range(len(new_elem)):
                new_elem[i] += elem2[i] % self.mod

            while len(new_elem) != 1 and self.items[0] == 0:
                new_elem.pop(0)
            return tfield(self.mod, *new_elem)

        elif isinstance(elem, int):
            new_elem = self.items[:]
            new_elem[-1] += elem % self.mod
            while len(new_elem) != 1 and self.items[0] == 0:
                new_elem.pop(0)
            return tfield(self.mod, *new_elem)

        else:
            print("unsupported types!")
    def __radd__(self, elem):
        if isinstance(elem, int):
            new_elem = self.items[:]
            new_elem[-1] += elem % self.mod
            while len(new_elem) != 1 and self.items[0] == 0:
                new_elem.pop(0)
            return tfield(self.mod, *new_elem)
        else:
            print("unsupported types!")
    def __neg__(self):
        new_elem = [-x % self.mod for x in self.items]
        return tfield(self.mod, *new_elem)
    def __sub__(self, elem):
        if isinstance(elem, tfield):
            if self.mod != elem.mod:
                return "different mod!"

            elem1 = self.items[:]
            elem2 = elem.items[:]

            if len(elem1) > len(elem2):
                for _ in range(len(elem1) - len(elem2)):
                    elem2.insert(0, 0)
            elif len(elem1) < len(elem2):
                for _ in range(len(elem2) - len(elem1)):
                    elem1.insert(0, 0)

            new_elem = elem1
            for i in range(len(new_elem)):
                new_elem[i] -= elem2[i] % self.mod
            while len(new_elem) != 1 and self.items[0] == 0:
                new_elem.pop(0)
            return tfield(self.mod, *new_elem)

        elif isinstance(elem, int):
            new_elem = self.items[:]
            new_elem[-1] -= elem % self.mod
            while len(new_elem) != 1 and self.items[0] == 0:
                new_elem.pop(0)
            return tfield(self.mod, *new_elem)

        else:
            print("unsupported types!")
    def __rsub__(self, elem):
        if isinstance(elem, int):
            new_elem = -tfield(self.mod, *self.items[:])
            new_elem.items[-1] = (new_elem.items[-1] + elem) % self.mod
            return new_elem
        else:
            print("unsupported types!")
    def __mul__(self, elem):
        if isinstance(elem, tfield):
            if self.mod != elem.mod:
                return "different mod!"

            elem1, elem2 = self.items[:], elem.items[:]
            elem1.reverse()
            elem2.reverse()
            elem1, elem2 = P(elem1), P(elem2)
            new_elem = list((elem1*elem2).coef)
            new_elem.reverse()
            for i in range(len(new_elem)):
                new_elem[i] %= self.mod

        elif isinstance(elem, int):
            new_elem = self.items[:]
            for i in range(len(new_elem)):
                new_elem[i] = new_elem[i] * elem % self.mod
        else:
            print("unsupported types!")

        while len(new_elem) != 1 and self.items[0] == 0:
            new_elem.pop(0)
        return tfield(self.mod, *new_elem)
    def __rmul__(self, elem):
        if isinstance(elem, int):
            new_elem = self.items[:]
            for i in range(len(new_elem)):
                new_elem[i] = new_elem[i] * elem % self.mod
            while len(new_elem) != 1 and self.items[0] == 0:
                new_elem.pop(0)
            return tfield(self.mod, *new_elem)
        else:
            print("unsupported types!")
    """def __truediv__(self, elem):
        if isinstance(elem, tfield):
            if self.mod != elem.mod:
                return "different mod!"

            elem1, elem2 = self.items[:], elem.items[:]
            elem1.reverse()
            elem2.reverse()
            elem1, elem2 = P(elem1), P(elem2)
            new_elem = list((elem1 // elem2).coef)
            new_elem.reverse()
            for i in range(len(new_elem)):
                new_elem[i] %= self.mod

        elif isinstance(elem, int):
            new_elem = self.items[:]
            for i in range(len(new_elem)):
                new_elem[i] = new_elem[i] * elem % self.mod
        else:
            print("unsupported types!")

        while new_elem[0] == 0:
            new_elem.pop(0)
        return tfield(self.mod, *new_elem)"""
    def __truediv__(self, elem):
        if isinstance(elem, tfield):
            if self.mod != elem.mod:
                return "different mod!"

            elem1, elem2 = self.items[:], elem.items[:]
            new_elem = stolbik(elem1, elem2, self.mod)

        elif isinstance(elem, int):
            new_elem = self.items[:]
            for i in range(len(new_elem)):
                new_elem[i] = new_elem[i] * elem % self.mod
        else:
            print("unsupported types!")

        if new_elem == False:
            print("No division by 0!")
        else:
            while len(new_elem) != 1 and self.items[0] == 0:
                new_elem.pop(0)
            return tfield(self.mod, *new_elem)

x = tfield(3, 5, 3)
y = tfield(3, 2, 7)
print(x * y)
print(x * 2)
print(2 * y)
print(x / y)