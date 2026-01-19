
name="Daniel"
age=20

print("My name is {} and I am {} years old".format(name,age))
print("Next year I will be {}".format(age+1))

# output:
# My name is Daniel and I am 20 years old
# Next year I will be 21
#-------------------------------------------------------------

# use positions
print("{0} loves {1} and {0} practise codes daily.".format("Gabriela","Python"))
# {0} -> will be name and {1} -> will be age always

# output:
# Gabriela loves Python and Gabriela practise codes daily.
#---------------------------------------------------------------------

# Named placeholders

print("Name:{name}, Age:{age}".format(name="Tony",age=18))
# output:  Name:Tony, Age:18

#---------------------------------------------------------------------

# Formatting numbers

score=89.4567
print("Score = {:.2f}".format(score))
# output : Score = 89.46

#------------------------------------------------------------------------

# Alignments

print("{:<10}|{:>5}".format("Apple",50))
# output : Apple     |   50

# {:<10} -> left-align, width 10
# {:>5} -> right-align, width 5
