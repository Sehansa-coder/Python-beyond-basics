# Problem :
# You are given a list of integers. Write a Python program that joins 
# the numbers into a single string, separated by commas.
# example:
# input  : [10,20,30,40]
# output : 10,20,30,40


def numbers_to_strings(nums):
    new_list=[]
    for i in nums:
        # str(i)  => convert each number in the list into a string
        new_list.append(str(i))
    result =",".join(new_list)
    return result


# Getting user input
mylist=[]
for i in range(4):
    num=int(input(f"Enter number {i+1} : "))
    mylist.append(num)

# call the function and display the output
print(numbers_to_strings(mylist))

# sample output:

# Enter number 1 : 1
# # Enter number 2 : 2
# Enter number 3 : 3
# Enter number 4 : 4
# 1,2,3,4
