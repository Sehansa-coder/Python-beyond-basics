
# Dictionary about a car

house={
    "floors":3,
    "colour":"white",
    "built_year":2021
}


keys_view=house.keys()         # Live view
keys_copy=list(house.keys())   # snapshot copy

# Modify dictionary
house["price"]=1200000

# Print after change
print("View after: ",keys_view)
print("Copy after: ",keys_copy)

# output:
# View after:  dict_keys(['floors', 'colour', 'built_year', 'price'])       
# Copy after:  ['floors', 'colour', 'built_year']


# why this happen?
# dict_keys(...) is a live view.
# If the dictionary changes, view also change
# In list(house.keys()) it is like a snapshot.It was taken once
# and never updates.