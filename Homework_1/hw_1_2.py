# problem 2 - finding the area of a circle given by the user's radius

import math
r = float(input("Enter the radius to compute the circle's area: "))
pi = math.pi
area = pi * r * r

print("The area of a circle with radius", r, "is about", round(area, 3), "units square.")
