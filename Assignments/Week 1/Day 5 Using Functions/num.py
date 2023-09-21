# Using Functions Self Assessment
# RaShiem KaLif Bell

# Write a program num.py that asks the user for their name and their 
# favorite number as input and outputs the following:
# The user’s name followed by “ ’s number” centered (assume 80 characters width) and all in title case. 
# For the apostrophe to work, you may need to strip spaces from the right of the name.
# Whether or not the number is a decimal number
# The number of 1’s in the number
# The factorial of the absolute number rounded to 0 decimals
# The log base 5 of the absolute value of the number
# An example run of this program might be:
# > Please enter your name: EMILY
# > Please enter your favorite number: 17
# > 			Emily’s Number
# > Is decimal? True
# > How many 1’s? 1
# > Factorial: 355687428096000
# > Log base 5: 1.7603744277225881


# Don’t forget to use meaningful variable names and add comments.


# Once you’re satisfied that your programs are working correctly, please take screenshots using the test case above & upload to canvas.

import math

name = input("What is your name? ")
num  = input("What is you favorite number? ")
line = name.title() + "'s Number"
centered_line = line.center(80)

print(centered_line)
print("Is decimal?", num.isdecimal())
print("How many 1's?", num.count("1"))
print("Log of 5", math.log(5))

num = int(num)
print (math.factorial(round(abs(num), 0)))
print(math.log(abs(num), 5))