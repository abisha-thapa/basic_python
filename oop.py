from __future__ import print_function
import math

def circumference(radius):
    return math.pi*2*radius

"""
Simple OOP
"""
circleName1 = "First Circle"
circleRadius1 = 4.4

circleName2 = "Second Circle"
circleRadius2 = 3.7

circumference1 = circumference(circleRadius1)
circumference2 = circumference(circleRadius2)

print (circumference1,circleName1)
print (circumference2,circleName2)


"""
List Simple OOP
"""
circles = [["First Circle",4.4,0],["Second Circle",3.7,0]]
circles[0][2] = circumference(circles[0][1])
print (circles[0][2])