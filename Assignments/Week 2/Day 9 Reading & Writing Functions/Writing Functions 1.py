# Writing Functions 1
# Kalif Bell


#1. Write a function, add, that takes two numbers as parameters and returns their sum.

def add(x, y):
    return x + y

# 2. Write a function, multiply, that takes two numbers as parameters and returns their product.

def multiply(x, y):
    return x * y

# 3. Now, test! Write python code that gets two numbers as input from the user 
# and prints out their sum and product by calling the two functions above. 
# Bonus points for putting this part in a main function.

num1 = int(input("Please enter a number: ")) 
num2 = int(input("Please enter another number: "))

print("Sum:", add(num1, num2))
print("Product:", multiply(num1, num2))

