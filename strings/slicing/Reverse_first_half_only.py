# problem : 
# Write a function that reverse only the first half of the string
# while keeping the second half unchanged

# Asssume the string ength is even

# Input : A string with an even number of characters
# Output : A string where only the first half is reversed

def first_half_reversed(word):

    # find the length of the user input
    length=len(word)
    
    # equation to check odd or even status
    check=length%2

    half=length//2

    if check==0:
        result=word[half-1::-1]+word[half:length]
        return result
    else:
        # if the number of characters in the string is odd
        return "Error"
    
# get user input
userInput=input("Enter the word : ")

# call the function and display output
print(first_half_reversed(userInput))



# ----------- sample output-------------
# Enter the word : butter     
#tubter

# Enter the word : bye   -> 3 characters (odd)
# Error

# Enter the word : abcdef
# cbadef