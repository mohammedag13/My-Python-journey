"""
Program: calculates the cost per square inch of a circular pizza,
given its diameter and price. The formula for area is A = pi * r**2

"""


import math

# Input: get the diameter and price of the pizza

diameter = float(input("Enter the diameter of the pizza(in inches): "))
price = float(input("Enter the price of the pizza (in dollars): "))

#Calculate the radius (r = diameter / 2)

radius = diameter / 2

#Calculate the area of the pizza (A = pi * r**2)

area = math.pi * (radius **2)

#Calculate the cosr per square inch (cost_per_inch = price / area)
cost_per_inch = price / area

#Output the Result

print(f"The cost per square inch of the pizza is {cost_per_inch:.2f}")
