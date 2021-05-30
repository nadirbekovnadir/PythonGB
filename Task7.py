class Complex2:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"{self.a}" + (f" + j{self.b}" if self.b > 0 else f" - j{-self.b}")

    def __add__(self, other):
        return Complex2(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return Complex2(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)


c1 = Complex2(2, 3)
c2 = Complex2(3, -1)
print(c1)
print(c2)

c3 = c1 + c2
print(c3)

c4 = c1 * c2
print(c4)
