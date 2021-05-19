class Matrix:
    def __init__(self, elements: list):
        self.__mat = elements

    # Лишние табы и переносы строк
    # можно было бы исключить делая join
    def __str__(self):
        res = str()
        for row in self.__mat:
            for el in row:
                res += str(el) + '\t'
            res += '\n'
        return res

    def __add__(self, other):
        res = Matrix(self.__mat)
        for i, row in enumerate(other.__mat):
            for j, el in enumerate(row):
                res.__mat[i][j] += el
        return res


mat1 = Matrix([[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]])

mat2 = Matrix([[3, 2, 1],
               [6, 5, 4],
               [9, 8, 7]])

print(mat1)
print(mat2)

mat3 = mat1 + mat2

print(mat3)
