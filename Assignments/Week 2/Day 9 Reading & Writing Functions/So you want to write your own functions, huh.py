# Practice Problems
# Kalif Bell

# 2. Write a function, pyramid, that takes a single character and a number 
# as parameters and displays an ASCII art pyramid to the screen with number rows

# print("*")
# print("*" * 2) this is the basic version repeated 

def pyramid(char, num): #not fruitful -- void, no return
    for i in range(1, num +1):
        print(char * i)

def main():
    print('pyramid("x", 2)')
    pyramid("x", 2)

    print('pyramid("*", 5)')
    pyramid("*", 5)

    print('pyramid("x", 10)')
    pyramid("x", 10)

main()
print()

# for a in range(1, 3):
#     print("*" * a)

# for i in range(1, 6):
#     print("+" * i)

# for j in range(1,11):
#     print("x" * j)

# 2. Write a function, absolute_difference, that takes 
# two numbers as parameters and returns their absolute difference

def absolute_difference(num1, num2):
    diff = abs(num1 - num2)
    return diff 

def main(): # Test cases will give me true or false output good start. 
    print("difference 5 10", absolute_difference(5, 10) == 5)
    print("difference 10 5", absolute_difference(10, 5) == 5) 
    print("difference 5 10", absolute_difference(200, -200) == 400)
    print()
    
main()
    

# What I had to get the answer then got confused...
# print(5 % 10)
# print(10 - 5)
# print((200 * 3) -200)
