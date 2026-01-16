# problem :
# Write a program to return the first half of the string
# For that the length of the string shoul be even.

def first_half(input_word):

    # find the length of the string
    length=len(input_word)

    # check whether the length of the string is even or odd
    check=length%2
   
    # get the range to display the half of string
    size=length//2

    if check==0:
        return input_word[:size]
    else:
        # if the length is odd, cannot return half of the string
        return "Error"
    
# get user input
word=input("Enter the word : ")

# call the function and display output
print(first_half(word))


# sample output : 
# Enter the word : abcdef
# abc

# Enter the word : ade
# Error

