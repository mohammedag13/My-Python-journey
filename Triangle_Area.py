"""
This is a program that calculates the area of a triangle
"""
import math

def triangle_area():
    a = float(input("Enter the value of side a: "))
    b = float(input("Enter the value of side b: "))
    c = float(input("Enter the value of side c: "))

    s = (a + b + c) / 2
    A = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(f"The area of a triangle is {A:.2f}")

triangle_area()