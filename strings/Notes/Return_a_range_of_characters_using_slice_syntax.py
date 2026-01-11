# We can return a range of characters by using the slice syntax'
# Specify the start index an end index

# Following example shows the way of getting characters from position 2 to position 5(not included):

text="Hello world"
print(text[2:5])  # output : llo

# slice from the start
print(text[:4]) # output : Hell

# slice to the end
print(text[2:]) # output : llo world

# using negative index
print(text[-9:-1])   # output : llo worl