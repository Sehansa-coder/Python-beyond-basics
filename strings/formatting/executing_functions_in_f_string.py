# problem:
# Ask the user to enter the:
# full name
# favourite fruit
# a sentence of their choice

# using f-string, print:
# the name in upper case
# the fruit in lower case
# the sentence with leading and tralling spaces removed
# the length of the sentence

def execute_functions_in_f_string(name,fruit,sentence):
    print(f"Name in uppercase: {name.upper()}")
    print(f"fruit in lowercase: {fruit.lower()}")
    print(f"cleaned sentence: {sentence.strip()}")
    print(f"sentence length: {len(sentence.strip())}")


# get user input
name=input("Enter name:")
fruit=input("Enter favourite fruit: ")
sentence=input("Enter a sentence:")

# call the function
execute_functions_in_f_string(name,fruit,sentence)


