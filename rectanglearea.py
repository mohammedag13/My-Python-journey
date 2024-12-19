"""
This program take width and length as input and calculates the area of a rectangle
it prints the area at the end after doing this calculation
area = length * width
"""

def rectangle_area(length, width):
    area = length * width
    return area

#Asking the user for length and width values respectively:
length = int(input("Type the length value: "))
width = int(input("Type the width value: "))

#Give the user of the program the result (printing area value in the screen):

print(f"The area of the rectangle with length {length} and width {width} is: {rectangle_area(length, width)}")
