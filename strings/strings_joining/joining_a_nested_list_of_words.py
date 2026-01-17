# problem :
# Write a python program that joins words from a nested list
# into a single sentence seperated by spaces

def join_nested_list(mylist):
    # create the new list 
    flatten_list=[]
    for sublist in mylist:
        for word in sublist:
            flatten_list.append(word)
    
    sentence=" ".join(flatten_list)

    # display the new flatten list
    print(flatten_list)

    # return the final sentence
    return sentence

# declare the nested list
word_list=[["I","am"],["interested"],["in","languages"]]

# call the function and display the output
print(join_nested_list(word_list))

# sample output:

# ['I', 'am', 'interested', 'in', 'languages']
# I am interested in languages