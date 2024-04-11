import numpy

class poly:
    def __init__(self, coefficients):
        self.coefficients = coefficients
        
    def val(self, x):
        return numpy.polyval(self.coefficients, x)
    
    def deriv(self, x):
        return numpy.polyval(numpy.polyder(self.coefficients), x)
        pass