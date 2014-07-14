import fractions
import math

class Rational:
    "Simple Rational Number Arithmetic"
        
    def __init__(self, number):
        "Number in Rational form (p/q)"
        conversion = fractions.Fraction.from_float(number)
        limited = conversion.limit_denominator(2)
        print ("Some math was done, the number is ", limited)
        self.numerator = limited.numerator #member variable to be used in other funcs
        self.denominator = limited.denominator #member variable to be used in other funcs
    
    #Member Functions

    def addition (self, num, denom):
        result = (self.numerator/self.denominator) + (num/denom)
        return result;

    def subtraction (self, num, denom):
        result = (self.numerator/self.denominator) - (num/denom)
        return result;

    def multiplication (self, num, denom):
        result = (self.numerator/self.denominator) * (num/denom)                 
        return result;

    def division (self, num, denom):
        result = (self.numerator/self.denominator) / (num/denom) 
        return result;
