# problem 7 - creating a class Circle and creating 2 functions that compute the area and parameter (circumference)

import math
import random
class Circle:
    def __init__(self, r):
        self.r = r
        print("The radius of the circle is", self.r)
    def get_area(self):
        p = math.pi
        self.area = p * self.r * self.r
        print("The area of the circle is about", round(self.area, 3), "units square")
        
    def get_perimeter(self):
        p = math.pi
        self.cir = 2 * p * self.r
        print("The peremeter/circumference of the circle is about", round(self.cir, 3), "units")


radius = float(input("Enter a radius of a circle: "))
c1 = Circle(radius)
c1.get_area()
c1.get_perimeter()
