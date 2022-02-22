class tfield:
    def __init__(self, mod, *args):
        self.mod = mod
        self.items = [int(x) % self.mod for x in args]
        self.tflen = len(args)
    def __len__(self):
        return self.tflen
    def __str__(self):
        return str(self.items)
    def __getitem__(self, i):
        return self.items[i]
    def __setitem__(self, key, value):
        self.items[key] = int(value)

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
            return tfield(self.mod, *new_elem)

        elif isinstance(elem, int):
            new_elem = self.items[:]
            new_elem[-1] += elem % self.mod
            return tfield(self.mod, *new_elem)

        else:
            print("unsupported types!")

    def __radd__(self, elem):
        if isinstance(elem, int):
            new_elem = self.items[:]
            new_elem[-1] += elem % self.mod
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
            return tfield(self.mod, *new_elem)

        elif isinstance(elem, int):
            new_elem = self.items[:]
            new_elem[-1] -= elem % self.mod
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

    def __mul__(self, number):
        pass
    def __rmul__(self, number):
        pass
    def __del__(self):
        pass

print('default')
elem1 = tfield(3, 3, 0, 3, 0, 3)
elem2 = tfield(3, 1, 1, 0, 1, 0, 1)
print(elem1)
print(elem2)

print('vec1 - vec2')
elem3 = elem1 - elem2
print(elem3)

print('vec1 + vec2')
elem3 = elem1 + elem2
print(elem3)

print('vec + number')
elem4 = elem3 + 1
print(elem4)
print('number + vec')
elem4 = 1 + elem3
print(elem4)

print('vec - number')
elem4 = elem3 - 1
print(elem4)

print('number - vec')
elem4 = 1 - elem3
print(elem4)


print('check')
print(elem1)
print(elem2)
