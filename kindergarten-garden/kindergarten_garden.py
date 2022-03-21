class Garden:
    
    def __init__(self, diagram, students=None):
        self.diagram = diagram.split("\n")
        self.plant = {'G': 'Grass', 'C': 'Clover', 'R': 'Radishes', 'V': 'Violets'}
        if students is None:
            self.students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']
        else:
            self.students = students
            self.students.sort()

    def plants(self, student):
        return [self.plant[self.diagram[0][self.students.index(student) * 2]],
                self.plant[self.diagram[0][self.students.index(student) * 2 + 1]],
                self.plant[self.diagram[1][self.students.index(student) * 2]],
                self.plant[self.diagram[1][self.students.index(student) * 2 + 1]]
                ]