# In this example it shows the usage of .keys() function.
# It does not make a copy. It creates a view object
# So when the dictionary changes, x changes automatically.

car={
    "brand":"Volvo",
    "model":"Mustang",
    "year":1978
}
x=car.keys()
print(x)
# output:
# dict_keys(['brand', 'model', 'year'])

car["colour"]="white"
print(x)
# output:
# dict_keys(['brand', 'model', 'year', 'colour'])