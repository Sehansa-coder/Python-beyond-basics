# Escape characters in Python strings

# Escape characters allow to include special characters like newlines,
# tabs, backslashes, quotes, etc., in strings.


# \n  -> new line
print("Hello!\nWelcome to python programming.")
# output:
# Hello!
# Welcome to python programming.


# \t  -> tab
print("Name:\tDaniel\nAge:\t20")
# output:
# Name:   Daniel
# Age:    20


# \\  -> backslash
print("This is a backslash:\\")
# output:
# This is a backslash:\


# \' -> single quote, \" -> double quote
print('It\'s Python')
print("He said \"Hello\" to me")

# output:
# It's Python
# He said "Hello" to me


# combining f-strings and escape characters
name="Sera"
score=23.789
print(f"Student:\t{name}\nScore:\t{score:.2f}")
# output:
# Student:    Sera
# Score:  23.79

