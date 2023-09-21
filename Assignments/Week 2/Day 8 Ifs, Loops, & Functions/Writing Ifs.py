# Writing Ifs

# 1 Create a program that asks the user for the current temperature and outputs what they should wear. 
# Your program should meet the following requirements:

# Has a variable, temp, that stores the temperature input from the user
# Requests the user to enter the temperature
# Displays the following information based on the temperature range: 
# Above 90: “Whoa, it’s boiling!”
# Above or equal to 80: “It’s getting hot”
# Below 80: “A perfect day”
# Below 60: “Don’t forget your sweater”
# Below freezing: “Brrr, you need a coat!”

# Only one phrase should be displayed to the user for any given temperature input. Make sure to test your program with multiple temperatures.

temp = int(input("What the current temperture outside?: "))
if temp > 90:
    print("Whoa, it's boiling!")
elif temp >= 80:
    print("It's getting hot")
elif temp > 60:
    print("A perfect day")
elif temp >= 32:
    print("Don't forget your sweater")
else:
  print("Brrr, you need a coat!")


# 2 Write a program that takes a number from 0-100 as input and prints the equivalent string letter grade (no +/-).

grade = int(input("Please enter a number from 0-100: "))
if grade >= 90:
    print("You got an A")
elif grade >= 80:
    print("You got a B")
elif grade >= 70:
    print("You got a C")
elif grade >= 60:
    print("You got a D")
else:
    print("You got a F")
