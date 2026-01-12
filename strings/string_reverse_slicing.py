# problem by---------------------Codewars--------------------------------
# source : https://www.codewars.com/kata/586efc2dcf7be0f217000619

# explanation :
# You'll be given a string of characters as an input. Complete the function that returns a list of strings: (a) in the reverse order of the original string, and (b) with each successive string starting one character further in from the end of the original string.
# Assume the original string is at least 3 characters long. Try to do this using slices and avoid converting the string to a list.

# Examples
# '123'   ==>  ['321', '21', '1']
# 'abcde' ==>  ['edcba', 'dcba', 'cba', 'ba', 'a']


def reverse_slicing(name):
    answer=[]

    for i in range(len(name),0,-1):   #  => counts backwards: 5,4,3,2,1
        answer.append(name[:i][::-1])   # [:i] => shortens the string from the end    #  [::-1] => reverse the string
    
    return answer

# get user input
input_name=input("Enter your input:")

# display output
print(reverse_slicing(input_name))

# sample output:

# Enter your input:123
# ['321', '21', '1']

# Enter your input:123456
# ['654321', '54321', '4321', '321', '21', '1']

# Enter your input:seha
# ['ahes', 'hes', 'es', 's']

# Enter your input:abcde
# ['edcba', 'dcba', 'cba', 'ba', 'a']