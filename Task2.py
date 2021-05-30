class ZeroDiv(Exception):
    def __init__(self, text):
        self.text = text


def division(a, b):
    if b == 0:
        raise ZeroDiv("!!!")

    return a / b


try:
    a = float(input('a: '))
    b = float(input('b: '))
    c = division(a, b)
    print(c)
except ZeroDiv as err:
    print(err)

