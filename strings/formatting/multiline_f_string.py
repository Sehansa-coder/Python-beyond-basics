# multiline f-string in Python

# This file demonstrates how to use multiline f-strings
# to print clean and formatted output without multiple print() calls.

name="Daniel"
age=20
language="English"
score=78.345

# Basic multiline f-string
print(f"""
Name: {name}
Age: {age}
Favouritr language: {language}
Score: {score:.2f}
Next year age: {age+1}
""")

# sample output:

# Name: Daniel
# Age: 20
# Favouritr language: English
# Score: 78.34
# Next year age: 21
