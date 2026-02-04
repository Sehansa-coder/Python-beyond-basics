# purpose:
# This program demonstrate how to remove an item from a list of dictionaries based
# on a condition (age)

# Example: List of students

students=[
    {"name":"David","age":18,"country":"Norway"},
    {"name":"Rebecca","age":19,"country":"Africa"},
    {"name":"Thomas","age":18,"country":"America"}
]

# Remove student of age 18
new_list=[]
for stu in students:
    if stu["age"]!=18:
        new_list.append(stu)

students=new_list

print("After removing:")
for i in students:
    print(i)

# sample output:

# After removing:
# {'name': 'Rebecca', 'age': 19, 'country': 'Africa'}

# Since both of the other students are 18 years old, they are removed.

