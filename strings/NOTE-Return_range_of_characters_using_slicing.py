
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

# Using step parameter
#   [start:end:step]  # step = how many jumps it takes

name="sehansa dewlini"
print(name[1:7:2])   # output :  eas

print(name[::2])     # output : shnadwii
print(name[1::2])    # output : eas eln

# Reverse a string
print(name[::-1])    # output : inilwed asnahes

print(name[8:2:-1])  # output : d asna

# slice the entire thing
print(name[:])      # output : sehansa dewlini


#------------------------------------------------------------------

# slicing works in lists,tuple,ranges

nums=[1,2,3,4,5,6]
print(nums[1:5:2])   # first index of range is 1  ->step=2  -> 1+2=3 = index 3 which means 2
                                # then index 3 + 2 = index 5 but not included

# output : [2, 4]

