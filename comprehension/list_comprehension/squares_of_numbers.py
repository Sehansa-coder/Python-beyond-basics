# create a list of numbers from 1 to 10

numbers=list(range(1,11))

# use list comprehension to get squares of all numbers
squares=[n**2 for n in numbers]

print(squares)

# sample output
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]