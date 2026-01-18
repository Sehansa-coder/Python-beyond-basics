# problem:
# Ask the user to enter:
#  their name, age,favourite programming language, current score
# using f-string, print the output in the format:

# Hello <name>!
# You are <age> years old.
# Your favourite programming language is <language>.
# Your score rounded to 2 decimal places is <score>.
# Next year, you will be <age+1> years old.

# Rules:
# You must use f-string
# round the score to 2 decimal places usinf formatting is=nside the f-string
# do the age calculation inside f-string.

def person_details(name,age,language,score):

    # display the output using f-string formatting
    print(f"Hello {name}!")
    print(f"You are {age} years old.")
    print(f"Your favourite programming language is {language}.")
    print(f"Your score rounded to 2 decimal places is {score:.2f}.")
    print(f"Next year, you will be {age+1} years old.")


# get user input
name=input("Enter your name:")
age=int(input("Enter your age : "))
language=input("Enter your favourite programming language:")
score=float(input("Enter your score :"))

# call the function 
person_details(name,age,language,score)

# sample output:
# 