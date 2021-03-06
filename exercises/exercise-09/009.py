"""
Project Euler Problem 9
=======================

A Pythagorean triplet is a set of three natural numbers, a < b < c, for
which,
                             a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


# The class


class Pythagorean:

    """
    Since pythagorean triples occur as m^2 - n^2, 2mn, m^2 + n^2

    Therefore their sum is 2m^2 + 2mn=100

    m^2 + mn =500

    m(m+n)=500

    sqrt500=22.~~~

    therefore try m=20 , m+n=25
    n = 5
    a = 400-25=375
    b = 2*20*5=200
    c = 400+25=425

    """

    def __init__(self, m=20, n=5):
        self.m = m
        self.n = n
        self.a = ((self.m**2) - (self.n**2))
        self.b = (self.m * self.n) * 2
        self.c = ((self.m**2) + (self.n**2))

    def ABCProduct(self):
        return (self.a * self.b * self.c)

pythagorean = Pythagorean()
print pythagorean.ABCProduct()

"""
The function

def pythagorean(result=1000):
    a = ((m**2) - (n**2))
    b = 2 * m * n
    c = ((m**2) + (n**2))
    return (a * b * c)
"""
