# get() method in Python

# sample dictionary
student={
    "name":"Bella",
    "age":13,
    "city":"Las Vegas"
}

# Accessing an existing key
name=student.get("name")
print("Name: ",name)  # output: Name: Bella

# Accessing a non-esisting key without crashing
grade=student.get("grade")
print("Grade: ",grade)  # output : Grade: None

# Accessing a non-existing key with a default value
grade=student.get("grade","not assigned")
print("Grade: ",grade)   # output: Grade:  not assigned

# 