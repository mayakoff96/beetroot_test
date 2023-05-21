class Fraction:

    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be 0.")
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        if isinstance(other, Fraction):
            numerator = self.numerator * other.denominator + other.numerator * self.denominator
            denominator = self.denominator * other.denominator
            return Fraction(numerator, denominator)
        else:
            raise TypeError("Unsupported operation type for +: 'Fraction' and '{}'".format(type(other).__name__))

    def __sub__(self, other):
        if isinstance(other, Fraction):
            numerator = self.numerator * other.denominator - other.numerator * self.denominator
            denominator = self.denominator * other.denominator
            return Fraction(numerator, denominator)
        else:
            raise TypeError("Unsupported operation type for -: 'Fraction' and '{}'".format(type(other).__name__))

    def __mul__(self, other):
        if isinstance(other, Fraction):
            if other.numerator == 0:
                raise ZeroDivisionError("Division by 0!")
            numerator = self.numerator * other.denominator
            denominator = self.denominator * other.numerator
            return Fraction(numerator, denominator)
        else:
            raise TypeError("Unsupported operation type for /: 'Fraction' and '{}'".format(type(other).__name__))

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return (self.numerator * other.denominator) == (self.denominator * other.numerator)
        else:
            return False

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"


if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    result = x + y
    print(result)
    print(result == Fraction(3, 4))