# Writing List 
# by Rashiem Kalif Bell

# 1. Write a program that creates a list of 20 numbers input by the user 
# and prints the average (mean) of the list.

# I have to the average first REMEMBER TO START 
# WITH THE SIMPLE PRINT THEN BUILD. 
# if you you dont know a formula LOOK
# IT UP!!!!!!IT ALL OPEN BOOK

# list = []
# for i in range(20):
#     user_input = int(input("Please enter 20 numbers: "))
#     list.append(user_input)

# print("Average:", sum(list)/len(list)) 


# 2. Write a function mangle that takes a string as a parameter and returns 
# the string after performing the following operations: 
# Converting the string to all upper case letters
# Removing the third character
# Removing the third to last character
# Test that your function works. 

def mangle(str):
    str = str.upper()
    str = str[0:2] + str[3:-3] + str[-2:]
    
    return str


# 3. Write a function, count_e, that takes a list of strings as a parameter and returns the total number of upper and lower case e’s 
# (“E” and “e”) in all the strings in the list. Test that your function works with multiple examples.


# print(count_e([“hi”, “hello”, “EEK!”]))	3

def count_e(list): # Write a function, count_e, that takes a list of strings as a parameter
    num_e = 0 # that will (count)total number of upper and lower case e’s # EMPTY VARIABLE MEAN WE WILL FILL WITH SOMETHING
    for string in list:
         num_e += string.upper().count("E") #update num_e with number of uppercase E.  It first turns the E to uppercase then counts them 
    return num_e # return


# 4 Write a function, count_vowels, that takes a list of strings as a parameter and returns the total number of upper and lower case vowels
#  (A, E, I, O, U) in all the strings in the list.


def count_vowels(list):
    num_vowels = 0
    for string in list:
        upper = string.upper()
        for vowels in "AEIOU":
            num_vowels += upper.count(vowels)
    return num_vowels



def main():
    # Test mangle
    test_input = ["hellothere", "42 degrees Celsius", "eeeeeee"]
    test_output = ["HELOTHRE", "42DEGREES CELSUS", "EEEEE"]
    for i in range(len(test_input)):
            print("Mangle", test_input[i] +":", mangle(test_input[i]) == test_output[i])
    
    # test count_e
    print(count_e(["hi", "hello", "EEK!"]))
    print("count_e", count_e(["hi", "hello", "EEK!"]) == 3)

    #test count_vowels
    print(count_vowels(["hi", "hello", "OOF!"]))
    print("count_vowels", count_vowels(["hi", "hello", "OOF!"]) == 5)

main()