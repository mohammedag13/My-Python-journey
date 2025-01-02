"""
This a program that calculates the slope of a line that passes
through two points (x1, y1) and (x2, y2).
"""

#Asking the user for the coordinates
x1 = int(input("Enter the value of x1: "))
x2 = int(input("Enter the value of x2: "))
y1 = int(input("Enter the value of y1: "))
y2 = int(input("Enter the value of y2: "))

def calculate ():
    if x2 - x1 == 0:
        print("The slope if undefined(division by zero is not allowed)")
    elif x2 - x1 != 0:
        slope = (y2 - y1) / (x2 - x1)
        print(f"the calculatod slope is {slope}")

calculate()