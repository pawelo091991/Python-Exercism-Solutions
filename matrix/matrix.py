class Matrix:
    
    matrix = list()
    
    def __init__(self, matrix_string):   
        self.matrix = [[int(num) for num in row.split(' ')] for row in matrix_string.splitlines()]

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        return [row[index-1] for row in self.matrix]
