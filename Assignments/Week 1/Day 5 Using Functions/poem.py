# Using Functions Practice
# RaShiem Kalif Bell

# Create a program poem.py that asks the user for 2 parts of speech
#  as input (a plural noun and an adjective) and outputs the following:

# ______ are red, violets are blue
# Monty Python is _______, woo hoo!

# Make sure to convert the strings to the proper case so that the first blank
# is capitalized and the second blank is all lower case.

# An example run of this program might be:
# > Please enter a plural noun: LEGOS
# > Please enter an adjective: AWESOME
# > Legos are red, violets are blue
# > Monty Python is awesome, woo hoo!

plural = input("Please enter a plural noun: ").capitalize()
adjective = input("Please enter an adjective: ").lower()

print(plural, "are red, violets are blue,")
print("Monty Python is", adjective + " " + "woo hoo!" )