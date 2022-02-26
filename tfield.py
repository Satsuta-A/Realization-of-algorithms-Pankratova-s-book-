from numpy.polynomial import Polynomial as P
from sympy import mod_inverse
import sympy as sp
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
            q_i = fs * mod_inverse(divisor[0], mod) % mod
        except Exception:
            return (q, number)
        tmp = [q_i * x for x in divisor] + [0]*(len(number) - len(divisor))
        q.append(q_i)
        for i in range(len(tmp)):
            number[i] = (number[i] - tmp[i]) % mod
        if len(number) > 0 and number[0] == 0:
            number.pop(0)
        if len(number) < len(divisor):
            return (q, number)
        else:
            return substolbik(number, divisor, mod)
    res = substolbik(number, divisor, mod)
    if q == []:
        return ([0], number)
    return res

class pol:
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
        if isinstance(elem, pol):
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
            while len(new_elem) != 1 and new_elem == 0:
                new_elem.pop(0)
            return pol(self.mod, *new_elem)

        elif isinstance(elem, int):
            new_elem = self.items[:]
            new_elem[-1] += elem % self.mod
            while len(new_elem) != 1 and self.items[0] == 0:
                new_elem.pop(0)
            return pol(self.mod, *new_elem)

        else:
            print("unsupported types!")
    def __radd__(self, elem):
        if isinstance(elem, int):
            new_elem = self.items[:]
            new_elem[-1] += elem % self.mod
            while len(new_elem) != 1 and self.items[0] == 0:
                new_elem.pop(0)
            return pol(self.mod, *new_elem)
        else:
            print("unsupported types!")
    def __neg__(self):
        new_elem = [-x % self.mod for x in self.items]
        return pol(self.mod, *new_elem)
    def __sub__(self, elem):
        if isinstance(elem, pol):
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
            return pol(self.mod, *new_elem)

        elif isinstance(elem, int):
            new_elem = self.items[:]
            new_elem[-1] -= elem % self.mod
            while len(new_elem) != 1 and self.items[0] == 0:
                new_elem.pop(0)
            return pol(self.mod, *new_elem)

        else:
            print("unsupported types!")
    def __rsub__(self, elem):
        if isinstance(elem, int):
            new_elem = -pol(self.mod, *self.items[:])
            new_elem.items[-1] = (new_elem.items[-1] + elem) % self.mod
            return new_elem
        else:
            print("unsupported types!")
    def __mul__(self, elem):
        if isinstance(elem, pol):
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
        return pol(self.mod, *new_elem)
    def __rmul__(self, elem):
        if isinstance(elem, int):
            new_elem = self.items[:]
            for i in range(len(new_elem)):
                new_elem[i] = new_elem[i] * elem % self.mod
            while len(new_elem) != 1 and self.items[0] == 0:
                new_elem.pop(0)
            return pol(self.mod, *new_elem)
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
        if isinstance(elem, pol):
            if self.mod != elem.mod:
                return "different mod!"

            elem1, elem2 = self.items[:], elem.items[:]
            new_elem = stolbik(elem1, elem2, self.mod)[0]

        elif isinstance(elem, int):
            new_elem = self.items[:]
            for i in range(len(new_elem)):
                new_elem[i] = new_elem[i] * mod_inverse(elem, self.mod) % self.mod
        else:
            print("unsupported types!")

        if new_elem == False:
            print("No division by 0!")
        else:
            while len(new_elem) != 1 and self.items[0] == 0:
                new_elem.pop(0)
            return pol(self.mod, *new_elem)
    def __rtruediv__(self, other):
        if isinstance(other, int):
            if self.items == [0]:
                print("No division by 0!")
            elif len(self.items) != 1:
                return 0
            elif len(self.items) == 1:
                d = self.items[0]
                return other * mod_inverse(d, self.mod) % self.mod
        else:
            print("unsupported types!")
    def __mod__(self, elem):
        if isinstance(elem, pol):
            if self.mod != elem.mod:
                return "different mod!"

            elem1, elem2 = self.items[:], elem.items[:]
            new_elem = stolbik(elem1, elem2, self.mod)[1]

        elif isinstance(elem, int):
            """new_elem = self.items[:]
            for i in range(len(new_elem)):
                new_elem[i] = new_elem[i] * mod_inverse(elem, self.mod) % self.mod"""
            return 0
        else:
            print("unsupported types!")

        if new_elem == False:
            print("No division by 0!")
        else:
            while len(new_elem) != 1 and self.items[0] == 0:
                new_elem.pop(0)
            return pol(self.mod, *new_elem)
    def __rmod__(self, elem):
        if isinstance(elem, int):
            if self.items == [0]:
                print("No division by 0!")
            elif len(self.items) != 1:
                return 0
            elif len(self.items) == 1:
                d = self.items[0]
                return elem * mod_inverse(d, self.mod) % self.mod
        else:
            print("unsupported types!")
    def __pow__(self, power, modulo=None):
        start = self
        shag = self
        for i in range(power - 1):
            start = start * shag
        return start


def converting(polinom: list, nepr: list, mod: int):
    polinom = pol(mod, *polinom)
    nepr = pol(mod, *nepr)
    deg = len(nepr)
    #print('conv fun', nepr, id(nepr))
    nepr.items = nepr.items[1:]
    #print(nepr)
    while nepr.items[0] == 0:
        nepr.items.pop(0)
    if len(polinom) >= deg:
        i = 0
        hel = pol(nepr.mod, 0)
        while len(polinom.items) >= deg:
            koef = polinom.items[i]
            polinom.items.pop(i)
            hel = hel + nepr * koef
        return polinom + hel
    else:
        return polinom

class TF:
    def __init__(self, mod: int, nepr: pol, polinom: pol):
        self.mod = mod
        if self.mod != nepr.mod != polinom.mod:
            raise Exception
        self.nepr = nepr
        self.polinom = polinom

    def __len__(self):
        return len(self.polinom)
    def __str__(self):
        return str(self.polinom.items)
    def __repr__(self):
        return str(self.polinom.items)
    def __getitem__(self, i):
        return self.polinom.items[len(self) - i - 1]
    def __setitem__(self, key, value):
        self.polinom.items[len(self.polinom) - key - 1] = int(value)
    def __abs__(self):
        integer = 0
        for i in range(len(self.polinom)):
            integer += self.polinom.items[i] * pow(10, i)
    def __add__(self, elem):
        if isinstance(elem, TF):
            if self.mod != elem.mod or self.nepr != elem.nepr:
                print("different mod or nepr!")
            else:
                return TF(self.mod, self.nepr, self.polinom + elem.polinom)
        else:
            print("unsupported types!")
    def __neg__(self):
        return TF(self.mod, self.nepr, -self.polinom)
    def __sub__(self, elem):
        if isinstance(elem, TF):
            if self.mod != elem.mod or self.nepr != elem.nepr:
                print("different mod or nepr!")
            else:
                return TF(self.mod, self.nepr, self.polinom - elem.polinom)
        else:
            print("unsupported types!")
    def __mul__(self, elem):
        if isinstance(elem, TF):
            if self.mod != elem.mod or self.nepr != elem.nepr:
                print("different mod or nepr!")
            else:
                new = TF(self.mod, self.nepr, self.polinom * elem.polinom)
                #print('mul', new.nepr, id(new.nepr))
                new.polinom = converting(new.polinom.items[:], new.nepr.items[:], self.mod)
                return new
        else:
            print("unsupported types!")
    def __truediv__(self, elem):
        if isinstance(elem, TF):
            if self.mod != elem.mod or self.nepr != elem.nepr:
                print("different mod or nepr!")
            else:
                new = TF(self.mod, self.nepr, self.polinom / elem.polinom)
                new.polinom = converting(new.polinom.items[:], new.nepr.items[:], self.mod)
                return new
        else:
            print("unsupported types!")
    def __mod__(self, elem):
        if isinstance(elem, pol):
            if self.mod != elem.mod:
                return "different mod!"

            elem1, elem2 = self.items[:], elem.items[:]
            new_elem = stolbik(elem1, elem2, self.mod)[1]

        elif isinstance(elem, int):
            """new_elem = self.items[:]
            for i in range(len(new_elem)):
                new_elem[i] = new_elem[i] * mod_inverse(elem, self.mod) % self.mod"""
            return 0
        else:
            print("unsupported types!")

        if new_elem == False:
            print("No division by 0!")
        else:
            while len(new_elem) != 1 and self.items[0] == 0:
                new_elem.pop(0)
            return pol(self.mod, *new_elem)
    def __rmod__(self, elem):
        if isinstance(elem, int):
            if self.items == [0]:
                print("No division by 0!")
            elif len(self.items) != 1:
                return 0
            elif len(self.items) == 1:
                d = self.items[0]
                return elem * mod_inverse(d, self.mod) % self.mod
        else:
            print("unsupported types!")
    def __pow__(self, power, modulo=None):
        start = self
        shag = self
        if power == 0:
            return TF(self.mod, self.nepr, pol(self.mod, 0))
        for i in range(power - 1):
            start = start * shag
        start = converting(start.polinom.items[:], self.nepr.items[:], self.mod)
        return start

"""x = pol(11, 1, 4, 1)
y = pol(11, 1, 1)
print(x * y)
print(x * 2)
print(2 * y)
print(x / y)
print(x % y)
print(pol(11, 2, 2, 2) / 2)
print(2 / pol(11, 2, 2, 2))
print(2 / pol(11, 2))
print(pow(pol(10, 1, 0), 10))"""

nepr = pol(2, 1, 0, 0, 1, 1)
alpha = pol(2, 1, 0)
element_of_field = TF(2, nepr, alpha)
for i in range(16):
    print(pow(element_of_field, i))
