# Writiing List 3
# Rashiem Kalif Bell

# 1. Write a function average_evens that takes a list of numbers as parameters, 
# and adds all the even numbers together and returns their average using a list. 

def average_evens(list):
    sum = 0
    num = 0
    for i in list:
        if i % 2 == 0:
            sum += i
            num += 1
    if num != 0:
        return sum / num
    return 0

# print(average_evens([-2, -3, -4, 0, 1, 2, 3, 4])) == 0



# 2. Write a function match that takes two strings as a parameter 
# and returns how many letters the strings have in common. 
# You should treat upper and lower case letters as the same letter 
# (‘A’ == ‘a’, etc). Test that your function works. 

def match(x, y): # takes to strings as parameters this time x and y was chosen 
    common = 0 #sum aggregating "returns how many" 
    x = x.upper() # make all upper since the problem is not case senstive 
    y = y.upper()
    seen = [] # Empty list to count 

    for letter in x:
        if letter not in seen and y.count(letter) > 0: # for each letter in the string h e l l o 
            common += 1
            seen.append(letter) # tell program to count common times we see the same letter in this case
        
    return common # I should return 3 using test cases 
    

# print(match(“hello”, “Healing”))			3
# print(match(“Healing”, “hello”))			3
# print(match(“hellllllo”, “Healllllling”))	3


def main():
    print(average_evens([-2, -3, -4, 0, 1, 2, 3, 4]))
    print(match("hello", "Healing") == 3)
    print(match("Healing", "hello") == 3)
    print(match("hellllllo", "Healllllling") == 3)
    print()

main()