# problem : 
# The user input a list of numbers.
# Write a python program that:
#   filters only the even numbers
#   joins them into a string seperated by hyphens

def join_even_numbers(num_list):
    even_list=[]
    for i in num_list:

        # chheck even or odd
        if i%2==0:
            even_list.append(str(i))
    
    result="-".join(even_list)
    return result


# get user input
number_list=[]
for i in range(10):
    numbers=int(input(f"Enter number {i+1} : "))
    number_list.append(numbers)

# call the function and display output
print(join_even_numbers(number_list))

# sample output :

# Enter number 1 : 1
# Enter number 2 : 2
# Enter number 3 : 3
# Enter number 4 : 4
# Enter number 5 : 5
# Enter number 6 : 6
# Enter number 7 : 7
# Enter number 8 : 8
# Enter number 9 : 9
# Enter number 10 : 10
# 2-4-6-8-10