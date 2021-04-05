class PhoneNumber:
    number = ""
    area_code = ""
    def __init__(self, number):

        for digit in number:
            if digit.isdigit() == True:
                self.number += digit

        if self.number[0] == '1':
            self.number = self.number[1:]

        if int(self.number[0]) < 2 or int(self.number[3]) < 2 or len(self.number) != 10:
            raise ValueError("Number not valid")

        self.area_code = self.number[:3]

    def pretty(self):
        return "(" + self.area_code + ")-" + self.number[3:6] + "-" +self.number[6:10]
            

    