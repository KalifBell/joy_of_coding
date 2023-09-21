# Using Functions Writing
# RaShiem KaLif Bell

# Write a program mad.py that asks the user to enter a phrase, and then prints out the following:
# The “mad” version of the phrase in all caps.
# A confused (i.e., mad) version of the phrase where all letter e’s are replaced by x’s.
# The maddest of all: print whether the phrase is printable.

# Hint: To find how you can print if something is printable, do the following:
# Convert your input to a string with str(input(“…”)) so that 
# PyCharm “knows” that your input variable is a string
# Type the name of your variable
# Type dot (“.”)
# Scroll through the list of functions & see if any look promising


user_input = str(input("Please enter a phase: "))

print("Ahh, I see you choose,", user_input.upper())
print("Ahh, I see you choose,", user_input.replace("e", "x"))
print("Ahh, I see you choose,", user_input.isprintable())