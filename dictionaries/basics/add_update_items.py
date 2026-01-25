# This explains how to add items and update items(dictionary items)

# Declare dictionary
student={
    "name":"Alice",
    "age":20
} 

# Add a new key
student["country"]="Sri Lanka"

# Update an existing key
student["age"]=25

# update using update() method
student.update({"grade":"A"})

print(student)

# sample output:
# {'name': 'Alice', 'age': 25, 'country': 'Sri Lanka', 'grade': 'A'}