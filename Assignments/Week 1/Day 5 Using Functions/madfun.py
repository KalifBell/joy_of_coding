# Using Functions Practice
# RaShiem KaLif Bell


# Write a program madfun.py that takes a decimal number as input from the user and prints out the following:
# The absolute value of the number 
# The number rounded to 0 decimal places
# The square root of the rounded number’s absolute value


# Example runs of this program might be:
# > Please enter a number: 8.88
# > 8.88
# > 9.0
# > 3.0

# > Please enter a number: -24.75
# > 24.75
# > -25.0
# > 5.0

import math

user_input = float(input("Please enter decimal number: "))

print("absolute value: ", (abs(user_input)))
print("rounded: ",       round(user_input))
print("square root: ",   math.sqrt(abs(round(user_input))))