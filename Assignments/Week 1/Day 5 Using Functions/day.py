# Quiz Using Functions
# RaShiem KaLif Bell

# Write a program day.py that asks the user for their favorite month
# and day of the month as input and outputs the following:

# a. The month & day followed by “ , 2020” with proper
# capitalization and spacing (i.e., no space before the comma,
# one space after).
# b. Whether or not the month is alphanumeric
# c. The number of 2’s in the number
# d. The factorial of the number
# e. The log base 2 of the absolute value of the number
# An example run of this program might be:

# > Please enter your favorite month: APRIL
# > Enter your favorite day of the month: 23
# > April 23, 2020
# > Is the month alphanumeric? True
# > How many 2’s? 1
# > Factorial: 25852016738884976640000
# > Log base 2: 4.523561956057013
import math

month = input("Please enter your favorite month:")
day   = input("Enter your favorite day of the month: ")
day_int = int(day) # changed to interger for factorial

print(month.capitalize(), day + ", ")
print("Is it alphanumeric?", month.isalnum())
print("How many 2's? ", day.count("2"))
print("Factorial of the day:", math.factorial(day_int))