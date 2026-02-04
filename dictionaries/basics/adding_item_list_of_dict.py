# purpose:
# This program demonstrate hoe to add a new item to a list of dictionaries

# Example:
student=[
    {"name":"Alex","age":12,"country":"India"},
    {"name":"Noruko","age":14,"country":"Japan"}
]
# Adding a new student
student.append({"name":"Liam","age":16,"country":"Spain"})

# Printing with the new added student
print("Ater adding Liam:")
for i in student:
    print(i)

# sample output:

# Ater adding Liam:
# {'name': 'Alex', 'age': 12, 'country': 'India'}
# {'name': 'Noruko', 'age': 14, 'country': 'Japan'}
# {'name': 'Liam', 'age': 16, 'country': 'Spain'}