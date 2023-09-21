# Writing Functions 2
# by Kalif Bell

# 4 Write a function is_even that takes a number as a parameter 
# and returns whether or not it is even. Test that your function 
# works by calling it twice, once with an even 
# number and once with an odd number, and print the results.

def is_even(num):
    return num % 2 == 0

# 5 Write afunction calculate_total that takes 3 parameters

def calculate_total(meal, tax_rate, tip_rate):
    tax = meal * tax_rate
    tip = meal * tip_rate
    return meal + tip + tax

# 6 Write a function hey that takes a number as a parameter, 
#  squares it, and outputs the parameter squared:

def hey(num):
    return num ** 2

# 7 Write a function there that takes a number n as a parameter, 
# and returns 2n if n is positive, and 0 otherwise. 
# Your function should output the following for the given calls

def there(num):
    if num < 0:
        return 0
    return 2 ** num

# Write a function are_we that takes a number of times to repeat 
# and a phrase to be repeated as parameters and outputs the following
# for the given calls:

# are_we = int
def are_we(n, s):
    for i in range(n):
        print("Are we", s, "yet?", end=" ")
    print()


def main():
    print("4 is even: ", is_even(4))
    print("5 is even:", is_even(5))
    print("Total should be 66.85: ", calculate_total(53.48, .07, .18))
    print("hey(5)", hey(5) == 25)
    print("hey(0)", hey(0) == 0)
    print("hey(-3)", hey(-3)== 9)
    print("there(5)", there(5) == 32)
    print("there(0)", there(0) == 1)
    print("there(3)", there(3) == 8)
    print("there(-2)", there(-2) == 0)
    print("there(-6)", there(-2) == 0)
    print("are_we(2, 'there')")
    are_we(2, "there")
    print("are_we(3, '50')")
    are_we(3, "50")
    print("are_we(1, '""')") 
    are_we(1, "")
    print("are_we(0, 'hey')")
    are_we(0, "hey!")

main()





































































































































