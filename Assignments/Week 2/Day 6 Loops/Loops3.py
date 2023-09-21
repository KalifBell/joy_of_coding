# ForLoops Writing 3

# Rashiem Kalif Bell

# 1.Using the range function, print the multiples of 4 from -16 through 16 (inclusive). 
# The numbers should each be separated by a dash. There should not be a dash after the final number (16).
for i in range(-16, 17, 4):
    print(i, end="-") 
print()


# 2. Using the range function, print the multiples of 10 from -10 to 100 (inclusive). 
# Each number should be separated by “...” and a space.

for i in range(-10,101,10):
    print(i,end="... ")
print()

# 3.Create a program sum10.py that calculates and prints the sum of 10 real 
# (i.e., decimal) numbers entered by the user. Make sure you ask (i.e., prompt) 
# the user to enter each number (the user will hit enter after each number). 

# sum = 0
# for i in range(10):
#     sum += float(input("Please enter a real number: "))
# print("Sum is:", sum)

for i in "OOMPAH!":
    print(i)

for i in "01 4 16 64 256":
    print(i, end="")
print()

for s in "S-C-R-E-A-M for ice cream!":
    print(s, end="")
print()

sum = 0
for i in range(-400, 400):
    print(i)
    sum += 1