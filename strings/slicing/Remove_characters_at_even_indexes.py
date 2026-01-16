# Problem :
# Write a function that removes all characters at even indexes
# and returns a string containing only characters at odd indexes

# input : a string of length>=1
# output : a string containing characters from odd positions only

def remove_even_index(word):

    # find the length of the input word
    length=len(word)
    return word[1:length:2]

# get user input
input_word=input("Enter word:")

# call the function and display output
print(remove_even_index(input_word))


# -----------sample output-------------
# Enter word:python
# yhn

# Enter word:abcdef
# bdf


