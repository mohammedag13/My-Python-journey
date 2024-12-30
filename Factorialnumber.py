"""
A program that will compute the factorial of a number entered by the user

"""


"""
Algorithm
Input number to take factorial of, n
Compute factorial of n, fact
Output fact

"""

def main():
    n = int(input("n!: "))
    fact = 1 #Accumulator starts at 1
    for number in range(1, n + 1):
        factorial = fact * number
    print(factorial)

main()