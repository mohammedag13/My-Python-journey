"""
A program that calculates the volume and surface
area of a sphere from its radius, given as input.

"""

r = int(input("Enter the radius: ")) #Asking the user to enter the radius

import math

def calculate():
    volume = (4 / 3) * math.pi * r**3
    area = 4 * math.pi * r**2
    volume = round(volume, 2)
    area = round(area, 2)
    print(f"The volume of the sphere is {volume}.")
    print(f"The area of the sphere is {area}.")
    
calculate()