# ForLoops Writing 2

# Rashiem Kalif Bell


# 1.  Using the range function, print the multiples of 5 from 10 through -25 (inclusive). 
# The numbers should each be separated by a space. (Hint: use the end parameter to the 
# print function like we did in for_range.py). Don’t forget to print a newline after this 
# loop by calling print() with no parameters.

for i in range(10,-26, -5):
    print(i, end=" ")
print()


# 2. Using the range function, print the multiples of 3 from -3 to 21 (inclusive). 
# Each number should be separated by a comma and a space. There should not be a 
# comma after the final number (21).

for j in range(-3, 21, 3):
    print(j, end=",")
print(21)

# 3. Create a program avg.py that calculates and prints the average of 10 real 
# (i.e., decimal) numbers entered by the user. Make sure you ask (i.e., prompt) 
# the user to enter each number (the user will hit enter after each number). 

# user_input = float(input("Please enter 10 real numbers: "))
s = 0
for k in range(10):
    user_input = float(input("Please enter 10 real numbers: "))
    s += user_input

print("Average: ", user_input)





