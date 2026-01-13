# Question:

# Write a function that returns the first and last character of a string.


def first_last(inputWord):
    # get the length of the input word
    l=len(inputWord)
    result=inputWord[:1]+inputWord[l-1:l]  # or use [-1:]
    return result

# get user input
word=input("enter the word : ")

# call the function and display output
print(first_last(word))

# sample output:
# enter the word : hello
# ho

# enter the word : python
# pn