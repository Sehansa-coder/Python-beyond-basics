# This example demonstrate how to change or modify the values 
# in a dictionary using a loop statement.
student={
    "name":"Maria",
    "age":25,
    "country":"Portugal"
}
print("Before updating:",student)

print("Updating values using loop:")
for key in student:
    if key=="age":
        student[key]=30

print(student)

# sample output:

# Before updating: {'name': 'Maria', 'age': 25, 'country': 'Portugal'}
# Updating values using loop:
# {'name': 'Maria', 'age': 30, 'country': 'Portugal'}