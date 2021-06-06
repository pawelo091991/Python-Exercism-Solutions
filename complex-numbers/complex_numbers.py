import math

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        if self.real == other.real and self.imaginary == other.imaginary:
            return True
        else:
            return False

    def __add__(self, other):
        return(
            ComplexNumber(
                self.real + other.real, 
                self.imaginary + other.imaginary
            )
        )

    def __mul__(self, other):
        return(
            ComplexNumber(
                self.real * other.real + self.imaginary * other.imaginary * (-1),
                self.real * other.imaginary + self.imaginary * other.real
            )
        )

    def __sub__(self, other):
        return(
            ComplexNumber(
                self.real - other.real, 
                self.imaginary - other.imaginary
            )
        )

    def __truediv__(self, other):
        top = ComplexNumber(self.real, self.imaginary) * ComplexNumber(other.real, -other.imaginary)
        bot = ComplexNumber(other.real, other.imaginary) * ComplexNumber(other.real, -other.imaginary)

        return(
            ComplexNumber(
                top.real/bot.real, 
                top.imaginary/bot.real
            )
        )

    def __abs__(self):
        return(math.sqrt(pow(self.real,2) + pow(self.imaginary,2)))

    def conjugate(self):
        return(
            ComplexNumber(
                self.real,
                -self.imaginary
            )
        )

    def exp(self):
        return(
            ComplexNumber(
                math.exp(self.real) * math.cos(self.imaginary),
                math.exp(self.real) * math.sin(self.imaginary) 
            )
        )
