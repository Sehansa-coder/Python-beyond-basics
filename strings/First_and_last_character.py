# Question:

# Write a function that returns a new string containing only the first 
# and last character of the given string
# Input : Astring with at leaat one character
# output : a string made of the first and last character

# exampe:
# Input : "a"
# output : "aa"
# Input : "hello"
# output : "ho"


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

# enter the word : a
# aa
