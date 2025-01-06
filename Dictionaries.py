students = {
    "MOAG": "MOHAMMED AGOUMIL",
    "HAAG": "HAMZA AGOUMIL",
    "FAAG": "FATIMA EZZAHRA AGOUMIL",
}

# Accessing a value
print(students["MOAG"])

# Adding a new key-value pair
students["FAAN"] = "FATNA ANIBI"
print(students) 

# Removing a key-value pair using del
del students["MOAG"]
print(students)

for student, lastname in students.items():
    print(f"{student} last name is {lastname}")





# Common dictionarry methods:
# .keys(): Return all keys        
# .values(): return all values         
#.itemss(): Returns all key-values pairs as tuples.