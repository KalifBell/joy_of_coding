# Using Functions Writing 
# Rashiem Kalif Bell

# Write a program maths.py that takes a number as input from the user 
# and prints out the following information:
# The absolute value of the number.
# The floor of the number using the math module (e.g., floor(3.75) is 3).
# The number rounded to 2 decimal places.

import math

user_input = (input("Please enter a number. "))
user_input = float(user_input)

print("absoulute value is:", abs(user_input))
print("floor value is", math.floor(user_input))
print("rounded value is", round(user_input, 2))