class Matrix:

    matrix = list()
    
    def __init__(self, matrix_string):   
        self.matrix = [[int(num) for num in row.split(' ')] for row in matrix_string.splitlines()]

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        return [row[index-1] for row in self.matrix]


dupa = Matrix("1 2 3 4\n5 6 7 9\n1 2 3 4")
dupa.column(2)

