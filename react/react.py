class Cell:
    formula_cells = []

    def __init__(self, value = None, inputs = None, function = None):
        if value != None:
            self.__value = value
        else:
            self.__inputs = inputs
            self.__function = function
            self.__value = function(self.__inputs)
            self.__callbacks = []
            Cell.formula_cells.append(self)
            
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value
        for cell in Cell.formula_cells:
            cell.update()

    def update(self):
        value = self.__function(self.__inputs)
        if self.__value != self.__function(self.__inputs):
            self.__value = value
            for callback in self.__callbacks:
                callback(self.__value)

    def add_callback(self, callback):
        self.__callbacks.append(callback)

    def remove_callback(self, callback):
        if callback in self.__callbacks:
            self.__callbacks.remove(callback)

    def __add__(self, value):
        return self.__value + value

    def __radd__(self, value):
        return self.__value + value

    def __sub__(self, value):
        return self.__value - value

    def __rsub__(self, value):
        return value - self.__value

    def __mul__(self, value):
        return self.__value * value

    def __rmul__(self, value):
        return self.__value * value

    def __lt__(self, value):
        return True if self.__value < value else False


class InputCell:
    def __new__(cls, value):
        return Cell(value=value)


class ComputeCell:
    def __new__(self, inputs, compute_function):
        return Cell(inputs=inputs, function=compute_function)
