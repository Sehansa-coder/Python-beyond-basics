# Formatting numbers in Python


salary=1000000
price=12345.6789
percentage=0.875
 
print(f"Salary: {salary:,}")
print(f"Price: {price:,.2f}")
print(f"Progress: {percentage:.1%}")

# Explanations:
# ,     -> adds thousand seperator
# .2f   -> formats float to 2 decimal places
# .1%   -> converts decimal to percentage
