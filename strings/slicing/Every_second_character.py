# Problem : 

# You are given a string as input
# Write function that returns a new string containing every second 
# character from the original string, starting
# from the first character (index 0)

# You must solve this problem using python slicing.

def one_hop(word):

    # find the length of the input word
    length=len(word)
    return word[:length:2]

# get user input
input_word=input("Enter the word : ")

# call the function and display the output
print(one_hop(input_word))


# sample output : 
# Enter the word : hello
# hlo

# Enter the word : abcdef
# ace