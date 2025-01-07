# This is a program that manages a simple gradebook

# Initialize the dictionary to store student names and grades
students = {}

# Ask the user how many students to add to the gradebook
students_number = int(input("Enter the number of students you want to add to the gradebook: "))

# Loop to gather names and grades
for i in range(students_number):
    name = input(f"Enter the name of student {i + 1}: ")
    grade = float(input(f"Enter {name}'s grade: "))  # Convert grade to a number
    students[name] = grade  # Add the student and their grade to the dictionary

# Display the gradebook
print("\nGradebook:")
for name, grade in students.items():
    print(f"{name}: {grade}")

# Calculate the average grade
average_grade = sum(students.values()) / len(students)

# Find students with grades equal to the average
students_with_average = [name for name, grade in students.items() if grade == average_grade]

# Display the average grade
print(f"\nThe average grade of the class is: {average_grade:.2f}")

# Display students with the average grade
if students_with_average:
    print("Students with the average grade:")
    for name in students_with_average:
        print(name)
else:
    print("No students have the average grade.")
