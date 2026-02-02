# This program shows different ways to loop through 
# a dictionary in Python.

student={
    "name":"Rose",
    "age":25,
    "grade":"A"

}

print("Looping through keys:")
for key in student:
    print(key)
# sample output:
# Looping through keys:
# name
# age
# grade

print("Looping through values:")
for value in student.values():
    print(value)
# sample output:
# Looping through values:
# Rose
# 25
# A

print("Looping through keys and values:")
for key,value in student.items():
    print(key,":",value)
# sample output:
# Looping through keys and values:
# name : Rose
# age : 25
# grade : A

# use it in a meaningful way
for key,value in student.items():
    print(f"{key} -> {value}")
# sample output:
# name -> Rose
# age -> 25
# grade -> A