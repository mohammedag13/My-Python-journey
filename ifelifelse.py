""" This a program that checks if a number is:
* Positive
* Negative
* Zero
* and if it is positive, it checks if it is even ir idd.
"""

#Le'ts create a function 
def checking ():
    number = int(input("Enter a number: ")) #Asking the user to Enter the number we want to check
    if number > 0:
        print(f"The number {number} is positive")
        
    elif number < 0:
        print(f"The Number {number} is positive")
    elif number == 0:
        print(f"The number {number} equal zero")
checking()    