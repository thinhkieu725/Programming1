"""
COMP.CS.100 Programming 1.
11.3.ComparisonsOfFractions.py
Creator: Thinh Kieu
Student id number: 152167613
"""


class Fraction:
    """
    This class represents one single fraction that consists of
    numerator (osoittaja) and denominator (nimittäjä).
    """

    def __init__(self, numerator, denominator):
        """
        Constructor. Checks that the numerator and denominator are of
        correct type and initializes them.

        :param numerator: int, fraction's numerator
        :param denominator: int, fraction's denominator
        """

        # isinstance is a standard function which can be used to check if
        # a value is an object of a certain class.  Remember, in Python
        # all the data types are implemented as classes.
        # ``isinstance(a, b´´) means more or less the same as ``type(a) is b´´
        # So, the following test checks that both parameters are ints as
        # they should be in a valid fraction.
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError

        # Denominator can't be zero, not in mathematics, and not here either.
        elif denominator == 0:
            raise ValueError

        self.__numerator = numerator
        self.__denominator = denominator

    def return_string(self):
        """
        :returns: str, a string-presentation of the fraction in the format
                       numerator/denominator.
        """

        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""

        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"

    def simplify(self):
        """
        Simplify the fraction by dividing numerator and denominator by their greatest common divisor.
        """
        gcd = greatest_common_divisor(self.__numerator, self.__denominator)
        self.__numerator //= gcd
        self.__denominator //= gcd

    def complement(self):
        """
        Return the complement of a fraction
        :return: fraction, the complement fraction
        """
        return Fraction((-1) * self.__numerator, self.__denominator)

    def reciprocal(self):
        """
        Return the reciprocal of a fraction
        :return: fraction, the reciprocal fraction
        """
        return Fraction(self.__denominator, self.__numerator)

    def multiply(self, frac2):
        """
        Return the product of the fraction and another fraction.
        :param frac2: fraction, the fraction to multiply
        :return: fraction, the product of two fractions
        """
        nume = self.__numerator * frac2.__numerator
        deno = self.__denominator * frac2.__denominator
        return Fraction(nume, deno)

    def divide(self, frac2):
        """
        Return the quotient of the fraction and another fraction.
        :param frac2: fraction, the fraction to divide
        :return: fraction, the quotient of two fractions
        """
        nume = self.__numerator * frac2.__denominator
        deno = self.__denominator * frac2.__numerator
        return Fraction(nume, deno)

    def add(self, frac2):
        """
        Return the sum of the fraction and another fraction.
        :param frac2: fraction, the fraction to add
        :return: fraction, the sum of two fractions
        """
        nume = self.__numerator * frac2.__denominator + frac2.__numerator * self.__denominator
        deno = self.__denominator * frac2.__denominator
        return Fraction(nume, deno)

    def deduct(self, frac2):
        """
        Return the difference of the fraction and another fraction.
        :param frac2: fraction, the fraction to deduct
        :return: fraction, the difference of two fractions
        """
        nume = self.__numerator * frac2.__denominator - frac2.__numerator * self.__denominator
        deno = self.__denominator * frac2.__denominator
        return Fraction(nume, deno)

    def __lt__(self, frac2):
        """
        Check whether the fraction is smaller than another fraction
        :param frac2: the fraction to be compared
        :return: bool, True if the fraction is smaller than frac2
        """
        if self.__numerator * frac2.__denominator - frac2.__numerator * self.__denominator < 0:
            return True
        else:
            return False

    def __gt__(self, frac2):
        """
        Check whether the fraction is greater than another fraction
        :param frac2: the fraction to be compared
        :return: bool, True if the fraction is greater than frac2
        """
        if self.__numerator * frac2.__denominator - frac2.__numerator * self.__denominator > 0:
            return True
        else:
            return False

    def __str__(self):
        """
        :returns: str, a string-presentation of the fraction in the format
                       numerator/denominator.
        """

        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""

        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"


def greatest_common_divisor(a, b):
    """
    Euclidean algorithm. Returns the greatest common
    divisor (suurin yhteinen tekijä).  When both the numerator
    and the denominator is divided by their greatest common divisor,
    the result will be the most reduced version of the fraction in question.
    """

    while b != 0:
        a, b = b, a % b

    return a


def main():
    frac = Fraction(-2, -4)
    print(frac)

    frac.simplify()
    print(frac)

    a = Fraction(2, 3)
    b = Fraction(3, 4)

    print(a.deduct(b))

    print(a < b)


if __name__ == "__main__":
    main()
