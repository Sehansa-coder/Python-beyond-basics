# Debug formatting in python uisng f-string

# This file demonstrate the use of debug formatting in python.
# Instead of printing just the value, you can print the variable name
# and its value together using = sign
# It's specially useful when debugging code or checking variables

x=20
name="Sera"
score=88.678

# Basic debug formatting
print(f"{x=}")
print(f"{name=}")
print(f"{score=:.2f}")  # formatting float while debugging

# Output:
# x=20
# name='Sera'
# score=88.68