"""
A program that determines the length of a ladder
-The algorithm:
Get input:

The height of the ladder.
The angle of the ladder.

calculation: 

* converting from degrees to radians using this formulae: radians = (pi / 180) * angle
* calculating length: length = height / sin(angle)

Get output:

print the length of the ladder required to reach a given height

"""
import math

ladder_height = float(input("Enter the height of the ladder: "))
ladder_angle = float(input("Enter the angle of the ladder: "))

#The angle must be in radians in order to calculate the length of the ladder
angle_in_radians = (math.pi / 180) * ladder_angle

#Calculating the height

length = ladder_height / math.sin(angle_in_radians)

#Printing the length of the ladder
print(f"The length of the ladder is: {length: .2f}")
