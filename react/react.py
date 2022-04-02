class InputCell:
    def __init__(self, initial_value):
        self.__value = initial_value
        self.__compute_cells = []

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value
        for compute_cell in self.__compute_cells:
            compute_cell.update()

    def __add__(self, val):
        return self.__value + val

    def __mul__(self, val):
        return self.__value * val

    def assign(self, compute_cell):
        self.__compute_cells.append(compute_cell)



class ComputeCell:
    def __init__(self, inputs, compute_function):
        self.__inputs = inputs
        self.__function = compute_function
        self.__value = compute_function(self.__inputs)

        for input in self.__inputs:
            input.assign(self)
            
        

    @property
    def value(self):
        return self.__value

    def add_callback(self, callback):
        pass

    def remove_callback(self, callback):
        pass

    def __add__(self, val):
        return self.__value + val.value

    def update(self):
        self.__value = self.__function(self.__inputs)
