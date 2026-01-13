# Problem :
# Remove first and last character
# Return the string without the first and the last character using slicing method.

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