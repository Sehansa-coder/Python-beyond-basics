# This program shows how to convert celsius temperatures to fahrenheit

celcius=[0,10,20,30,40]

# formula:  (C*9/5)+32

farenheit=[]
for temp in celcius:
    farenheit.append((temp*9/5)+32)

print(farenheit)

# sample output:
# [32.0, 50.0, 68.0, 86.0, 104.0]