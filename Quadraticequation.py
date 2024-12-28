"""
This Program solves all kinds of quadratic equations
"""
#Importing the math library
import math

def main():
    print("This program find the real solutions to a quadratic")
    print()

    a = float(input("Enter the value of coefficient a: "))
    b = float(input("Enter the value of coefficient b: "))
    c = float(input("Enter the value of coefficient c: "))

    square_root = math.sqrt(b * b - 4 * a * c)
    
    root1 = (-b + square_root) / (2 * a)
    root2 = (-b - square_root) / (2 * a)

    print()
    print("The solutions are: ", root1, root2)

main()