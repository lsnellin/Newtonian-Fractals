class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
     
    def __repr__(self):
        return "{}{:+}i".format(self.real, self.imag)
     
    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real,imag)
     
    def __truediv__(self, other):
        denom = other.real**2 + other.imag**2
        real = (self.real * other.real + self.imag * other.imag) / denom
        imag = (self.imag * other.real - self.real * other.imag) / denom
        return ComplexNumber(real, imag)
    
    def __add__(self, other):
        real = self.real + other.real
        imag = self.imag + other.imag
        return ComplexNumber(real, imag)
    
    def __sub__(self, other):
        real = self.real - other.real
        imag = self.imag - other.imag
        return ComplexNumber(real, imag)
    def mult(self, other):
        real = self.real * other
        imag = self.imag * other
        return ComplexNumber(real, imag)
        