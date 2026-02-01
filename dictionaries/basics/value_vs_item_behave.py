# Demonstrating that values() and items() are live views
# values() --> live view of all values
# items() --> live view of key-value pairs

product={
    "name":"Laptop",
    "price":1200,
    "stock":10
}

# get views
value_view=product.values()
item_view=product.items()

print("Before change:")
print("values:",value_view)
print("items:",item_view)

# modify the directory
product["price"]=1500
product["brand"]="Lenovo"

print("After change:")
print("Values:",value_view)
print("Items:",item_view)

# sample output:

# Before change:
# values: dict_values(['Laptop', 1200, 10])
# items: dict_items([('name', 'Laptop'), ('price', 1200), ('stock', 10)])
# After change:
# Values: dict_values(['Laptop', 1500, 10, 'Lenovo'])
# Items: dict_items([('name', 'Laptop'), ('price', 1500), ('stock', 10), ('brand', 'Lenovo')])