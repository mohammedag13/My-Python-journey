# Modifying lists
# Adding Elements using .append()
names = ["mohammed", "fatima ezzahra", "Riad", "majed"]
names.append("salah")
print(names)

# Removing elements using remove()
# Using .pop() - to move the element at the desired index
numbers = [0, 1, 2, 3, 4, 5]
numbers.remove(1)
numbers.pop(0)
print(numbers)

# list of numbers
# Get the number of elements in the list

length1 = len(numbers)
length2 = len(names)

print(f"The lists lengths respectively are: {length1}, {length2}")