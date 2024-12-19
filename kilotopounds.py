"""
Building a program to convert weight from kilograms
to pounds because in europe we use kilograms and in America
people use pounds so it is a bit confusing.
"""
def kilograms_to_pounds (kilograms):
    pound = kilograms * 2.20462
    return pound

#Asking the user to put weight in kilograms:

kilograms = float(input("Enter the weight in kilograms: "))

#converting kilograms to pounds
pounds = kilograms_to_pounds(kilograms)

#printing the result of the conversion
print(f"{kilograms} is equal to {pounds:.2f} pounds")
