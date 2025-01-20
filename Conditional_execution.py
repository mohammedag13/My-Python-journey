x = int(input("Enter a number: "))
y = int(input("Enter a number:"))

#This is a compound statement
#the placeholder pass is used to avoid syntax error

if x > 0:
    pass #This is a placeholder that does nothing
elif x < 0:
        print("x is negative")
else:
    print("x is zero")

#Alternative execution
if x % 2 == 0:
    print("x is even")
else:
     print("x is odd") #This is called a branche

#chained conditionals
if x < y:
     print("x is less than y") #This is called a branche
elif x > y:
     print("x is greater than y") # This is called a branche
else:
     print("x and y are equal")


#Nested conditionals
#Make sure to avoid nested conditions as much as possible cause it makes the code difficult to read

#Combining logical operators with nested conditionals
if 0 < x and x < 10:
     print("x is a positive single-digit number.")
     