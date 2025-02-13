# Description: This file is used to learn python programming language
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_name(self):
        print("My name is " + self.name)
        print("My age is " + str(self.age))
        print("My grade is " + self.grade)
    

mohammed = Student("Mohammed", 25, "sixth grade")
asmaa = Student("Asmaa", 23, "fifth grade")
omar = Student("Omar", 20, "third grade")

mohammed.get_name()
print("------------------------------------------------------")
asmaa.get_name()
print("------------------------------------------------------")
omar.get_name()