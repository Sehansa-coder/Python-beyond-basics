# Problem :
# Write a python program that:
# 1. takes three words as user input
# 2. Stores them in a list
# 3. Joins them into a sentence seperated by spaces
# 4. Prints the final sentence


def join_words(words_list):
    sentence=" ".join(words_list)
    return sentence

# Get user input
mylist=[]
for i in range(3):
    word=input(f"Enter word {i+1} : ")
    mylist.append(word)

# Call the function and display the final sentence
print(join_words(mylist))


# sample output :
# Enter word 1 : Good 
# Enter word 2 : morning
# Enter word 3 : guys
# Good morning guys
