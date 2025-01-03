"""
Now lets calculate the distance between two points
"""

import math

#Asking the user for the coordinates
x1 = float(input("Enter the value of x1: "))
x2 = float(input("Enter the value of x2: "))
y1 = float(input("Enter the value of y1: "))
y2 = float(input("Enter the value of y2: "))

def distance():
    value1 = (x2 - x1)**2
    value2 = (y2 - y1)**2
    distance = math.sqrt(value1 + value2)
    print(f"The distance between two points is: {distance:.2f}")

distance()