# Find the area of Circle given that radius of a circle. (Use pi value from Math module as mathematical constant)

import math


def circle_area(radius):
    return math.pi * radius * radius


r = 5
print('Area of circle with radius {} is {}'.format(r, circle_area(r)))
