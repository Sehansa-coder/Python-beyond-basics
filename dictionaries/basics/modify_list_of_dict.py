# purpose:
# This program demonstrate how to modify values in a list of dictionaries

# Example:
animals=[
    {"name":"dog","legs":4,"type":"Husky"},
    {"name":"cat","legs":4,"type":"Persian"},
    {"name":"bird","legs":2,"type":"parrot"}
]

# Modify if the name is dog, we capitalize it
for ani in animals:
    if ani["name"]=="dog":
        ani["name"]="DOG"

print("After update:")
for ani in animals:
    print(ani)

# sample output:

# After update:
# {'name': 'DOG', 'legs': 4, 'type': 'Husky'}
# {'name': 'cat', 'legs': 4, 'type': 'Persian'}
# {'name': 'bird', 'legs': 2, 'type': 'parrot'}