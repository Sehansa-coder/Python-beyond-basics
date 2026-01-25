# This example demonstrate different ways to remove items from a dictionary.
# the methods are:
# .pop()
# del
# .clear()

student={
    "name":"Alfred",
    "age":20,
    "country":"America",
    "grade":"A"
}

# Remove an item using pop()
removed_age=student.pop("age")
print("Removed age:",removed_age)
print("After pop:",student)
# sample output:
# Removed age: 20
# After pop: {'name': 'Alfred', 'country': 'America', 'grade': 'A'}

# Remove an item using del
del student["grade"]
print("After del:",student)
# sample output:
# After del: {'name': 'Alfred', 'country': 'America'}

# If the key doesn't exist, use the following safe version
student.pop("marks","Key not found")

student.clear()
print("After clear:",student)
# Sample output:
# After clear: {}