class Queen:
    def __init__(self, row, column):

        if row < 0:
            raise ValueError("row not positive")
        elif row > 7:
            raise ValueError("row not on board")
        else:
            self.row = row

        if column < 0:
            raise ValueError("column not positive")
        elif column > 7:
            raise ValueError("column not on board")
        else:
            self.column = column

    def __eq__(self, other):
        return self.row == other.row and self.column == other.column
        


    def can_attack(self, another_queen):
        if another_queen == self:
            raise ValueError("Invalid queen position: both queens in the same square")

        return self.row == another_queen.row or self.column == another_queen.column or abs((self.row - another_queen.row)/(self.column - another_queen.column)) == 1

            
