# create a list of numbers from 1 to 20
numbers=list(range(1,21))

# use list comprehension to filter only even numbers
even_numbers=[n for n in numbers if n%2==0]

print(even_numbers)

# output:
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]