class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        return Matrix([[m + n for m, n in zip(x, y)] for x, y in zip(self.matrix, other.matrix)])

    def __str__(self):
        my_str = ""
        for el in self.matrix:
            my_str += "\t".join(list(map(str, el))) + "\n"
        return my_str


matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
print(matrix1 + matrix2)
