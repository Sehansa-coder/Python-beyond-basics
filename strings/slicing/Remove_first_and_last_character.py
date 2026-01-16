# Problem :
# Remove first and last character
# Write a functionthat removes the first and last character from a string and 
# returns the remaining part.

# input : a string with at least two characters
# output : a string without first and last character

def remove_first_last(word):
    # find the length of the input 
    l=len(word)
    return word[1:l-1]

# get the user input
input_word=input("Enter the word : ")

# call the function and display output
print(remove_first_last(input_word))

# sample output :
# Enter the word : sehansa
# ehans

# Enter the word : hello
# ell

# Enter the word : hello children
# ello childre
