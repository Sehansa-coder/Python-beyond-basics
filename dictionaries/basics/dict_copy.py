# Demonstration of copy()

student={
    "name":"Alex",
    "age":21
}

# create a copy and it doesn't change
student_copy=student.copy()

# add a new item to the dictionary
student["city"]="Colombo"

print("original:",student)
print("copy:",student_copy)

# sample output

# original: {'name': 'Alex', 'age': 21, 'city': 'Colombo'}
# copy: {'name': 'Alex', 'age': 21}