# purpose:
# Demonstrate how to use a list of dictionaries in Python
# You can store multiple records (like students) an access, modify, add, or
# remove them.

# Example: List of students

students=[
    {"name":"Alex","age":20,"country":"America"},
    {"name":"Sera","age":23,"country":"Africa"},
    {"name":"Tony","age":25,"country":"Canada"}
]

# -------------------------------Accessing all students------------------------------
print("All students:")
for i in students:
    print(f"{i['name']} is {i['age']} years old who lives in {i['country']}")

# sample output:
# All students:
# Alex is 20 years old who lives in America
# Sera is 23 years old who lives in Africa
# Tony is 25 years old who lives in Canada