# Purpose:
# This program demonstrates nested dictionaries in Python.
# Nested dictionaries are dictionaries within dictionaries, often used to store
# structured data.
# You will see how to access, update, and literate over nested dictionaries.

# Example: Students with their age and grade
students={
    "Sera":{"age":17,"grade":"A"},
    "Alex":{"age":13,"grade":"B"},
    "Bengin":{"age":16,"grade":"F"}
}

print(students)
# output:
# {'Sera': {'age': 17, 'grade': 'A'}, 'Alex': {'age': 13, 'grade': 'B'}, 'Bengin': {'age': 16, 'grade': 'F'}}

# Accessing nested dictionary
print("Sera's age:",students["Sera"]["age"])
print("Alex's grade:",students["Alex"]["grade"])
# output:
# Sera's age: 17
# Alex's grade: B


# Update necessary dictionary
students["Bengin"]["grade"]="C"
print("After updating Bengin's grade:",students["Bengin"])
# output:
# After updating Bengin's grade: {'age': 16, 'grade': 'C'}

# Adding a new studnet
students["Liam"]={"age":20,"grade":"A"}
print("After adding Liam details:",students)
# output:
# After adding Liam details: {'Sera': {'age': 17, 'grade': 'A'}, 'Alex': {'age': 13, 'grade': 'B'}, 'Bengin': {'age': 16, 'grade': 'C'}, 'Liam': {'age': 20, 'grade': 'A'}}



