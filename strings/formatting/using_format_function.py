# String formatting using str.format()
# This file demonstrate string formatting using the str.format() method.
# It uses curly braces {} as placeholders and replaces them with values passed inside
# the format() method.
#
# The format() method was introduced as a more readable alternative to 
# old-style (%) string formatting.
# Although, f-strings are preferred in modern Python, understanding .format() is
# useful when reading older codebases.

name="Daniel"
age=20

print("My name is {} and I am {} years old".format(name,age))
print("Next year I will be {}".format(age+1))

# expected output:
# My name is Daniel and I am 20 years old
# Next year I will be 21
#-------------------------------------------------------------

# use positional placeholders
print("{0} loves {1} and {0} practise codes daily.".format("Gabriela","Python"))
# {0} -> will be name and {1} -> will be age always
# {)} refers to the first value, {!} refers to the second value.

# expected output:
# Gabriela loves Python and Gabriela practise codes daily.
#---------------------------------------------------------------------

# Using Named placeholders

print("Name:{name}, Age:{age}".format(name="Tony",age=18))
# output:  Name:Tony, Age:18

#---------------------------------------------------------------------

# Formatting numbers

score=89.4567
print("Score = {:.2f}".format(score))
# :.2f formats the float value to 2 decimal places
# output : Score = 89.46

#------------------------------------------------------------------------

# Alignments formatting

print("{:<10}|{:>5}".format("Apple",50))
# output : 
# Apple     |   50

# <  : left-align text
# >  : right-aligned text
# {:<10} -> left-align, width 10
# {:>5} -> right-align, width 5
