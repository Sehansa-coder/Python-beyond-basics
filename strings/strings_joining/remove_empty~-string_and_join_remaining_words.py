# problem:
# write a python program that removes empty strings from a list
# and joins the remaining words into a single sentence


def remove_empty(word_list):
    # declare new list
    new_list=[]
    for item in word_list:

        # only add the items in the list with no empty elements
        if item!="":
            new_list.append(item)

    sentence=" ".join(new_list)
    return sentence

# declare the list
mylist=["Python", "","is", "","very","powerful",""]

# call the function and display the output
print(remove_empty(mylist))

# sample output:

# Python is very powerful