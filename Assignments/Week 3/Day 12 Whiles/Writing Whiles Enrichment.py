# Writing Whiles Enrichment
# Rashiem Kalif Bell 

# 1. (WW1) Using a while loop, write a program that prints out the even numbers from 2 to 20.abs
i = 2
while i <= 20:
    # print(i)
    i += 2

# 2. (WW2) Write a program that gets a string as input from the user, and finds the index of the 
# first occurrence of the letter ‘e’ (upper or lower case). Your program should define a function
# that takes a string as a parameter and returns the e index. If the string does not contain an e,
# the function should return -1.

def find_e(user_input): # Get input from user
    user_input_upper = user_input.upper() # convert to uppercase so it's case insensitive 
    count = user_input_upper.count("E")
    return count

find_e(hello)
# user_input = input("Please enter a word: ")
# e_count = find_e(user_input)
# print(find_e)

# def count_e(user_input):
#     user_input_lower = user_input.lower()
#     count = user_input_lower.count('e')

#     return count 

# user_input = input("Please enter a word: ")
# e_count = count_e(user_input)

# print(f"The letter 'e' (case-insensitive) appears {e_count} times in the input string.")
