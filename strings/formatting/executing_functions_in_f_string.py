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
    # convert the letters in name to upper case
    print(f"Name in uppercase: {name.upper()}")
    # convert the letters in the fruit to lower case
    print(f"fruit in lowercase: {fruit.lower()}")
    # strip() function remove the unwanted spaces in the beginning and end of user input. Not in the middle of the spaces
    print(f"cleaned sentence: {sentence.strip()}")
    # print the length of the sentence after removing extra unwanted spaces by strip() function
    print(f"sentence length: {len(sentence.strip())}")


# get user input
name=input("Enter name:")
fruit=input("Enter favourite fruit: ")
sentence=input("Enter a sentence:")

# call the function
execute_functions_in_f_string(name,fruit,sentence)

# sample output:
# Enter name:Andrea
# Enter favourite fruit: ApplE
# Enter a sentence:    I love python
# Name in uppercase: ANDREA
# fruit in lowercase: apple
# cleaned sentence: I love python
# sentence length: 13


