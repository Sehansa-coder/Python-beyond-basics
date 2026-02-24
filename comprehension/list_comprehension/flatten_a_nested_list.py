# this example shows how to flatten a nested list
# converting a 2D liat (list of lists) into 1D list

nested_list=[[1,2,3],[4,5,6],[7,8]]

# list comprehension to flatten the list

flattened=[]
for sublist in nested_list:
    for num in sublist:
        flattened.append(num)

print(flattened)

# sample output:
# [1, 2, 3, 4, 5, 6, 7, 8]