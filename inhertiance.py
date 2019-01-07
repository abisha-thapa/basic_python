"""
                  Shape
                  Polygon
    Quadrilateral       Triangle
Rec. Trape. Square  Iso. Equi. Scalene
"""

from __future__ import print_function

class Shape():
    def __init__(self):
        self.color = "red"
        self.sides = 0

class Square(Shape):
    def __init__(self,w):
        Shape.__init__(self)
        self.width = w

sq1 = Square(5)
sq2 = Square(9)

print("Square Size",sq1.width,"X",sq1.sides,sq1.color,",",sq2.width,"X",sq2.sides,sq2.color)