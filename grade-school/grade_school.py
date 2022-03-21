import bisect

class School:
    def __init__(self):
        self.grades = {1:[],2:[],3:[],4:[],5:[],6:[],7:[]}
        self.names = []
        self.added_history = []

    def add_student(self, name, grade):
        if name in self.names:
            self.added_history.append(False)
        else:
            bisect.insort(self.grades[grade], name)
            self.added_history.append(True)

        self.names.append(name)

    def roster(self):
        roster = []
        for i in range(1,8):
            roster.extend(self.grades[i])

        return roster


    def grade(self, grade_number):
        return self.grades[grade_number]

    def added(self):
        return self.added_history
