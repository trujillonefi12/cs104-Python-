# PROGRAM BY NEFI TRUJILLO
# CS104 ENSIGN COLLEGE MAY THE 5TH

import math


cRad = int(input("What is the radius of the circle? "))


diameter = 2 * cRad


circumference = 2 * math.pi * cRad

area = math.pi * cRad**2


print(
    "A circle with a radius of",
    cRad,
    "units will have a diameter of",
    diameter,
    "square units, and a circumference of",
    "{:.2f}".format(circumference),
    "units, an area of",
    "{:.2f}".format(area),
    "units.",
)
