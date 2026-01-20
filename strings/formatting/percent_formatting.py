# Old-style string formatting using %

# This file demonstrates old-stype (%) string formatting and compares it with 
# modern f-string formatting.

name = "Lily"
age = 20
score = 87.567

print("Name: %s"% name)     # %s -> string
print("Age: %d"% age)       # %d -> integer
print("Score: %f"% score)   # %f -> float
print("Score rounded off to 2 decimal places: %.2f"% score) 
# output= 87.57

print("My name is %s and I am %d years old."%(name,age)) 
# output - My name is Lily and I am 20 years old.

# same output using f-strings (modern approach)

print(f"My name is {name} and I am {age} years old.") 
# output -My name is Lily and I am 20 years old.

print(f"Score: {score:.2f}")   
# output= 87.57


# Final output:
# Name: Lily
# Age: 20
# Score: 87.567000
# Score rounded off to 2 decimal places: 87.57
# My name is Lily and I am 20 years old. 
# My name is Lily and I am 20 years old. 
# score: 87.57
