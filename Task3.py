class Cell:
    def __init__(self, count: int):
        self.__count = count

    def __add__(self, other):
        return Cell(self.__count + other.__count)

    def __sub__(self, other):
        res = self.__count - other.__count
        if res <= 0:
            raise ValueError

        return Cell(res)

    def __mul__(self, other):
        return Cell(self.__count * other.__count)

    def __truediv__(self, other):
        return Cell(self.__count // other.__count)

    @staticmethod
    def make_order(cell, n):
        res = str()
        counter = cell.__count
        while counter > 0:
            res += '*' * (counter if counter < n else n) + '\n'
            counter -= n

        # Просто скопировал:)
        def remove_suffix(input_string, suffix):
            if suffix and input_string.endswith(suffix):
                return input_string[:-len(suffix)]
            return input_string

        res = remove_suffix(res, '\n')

        return res


c1 = Cell(4)
c2 = Cell(3)
c3 = Cell(5)
c4 = Cell(7)

c5 = c1 - c2

print(Cell.make_order(c4, 2))
