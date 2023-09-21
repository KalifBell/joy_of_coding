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

user_input = input("Please enter a word: ").lower()
e = 0
for i in user_input:
    if i == "e":
        e = e + 1
if e == 0:
    print("-1")
else:
    print(str(e))



# counting e

# find e and return the amount of e in user imput
# return -1 if the user_input does not contain an e