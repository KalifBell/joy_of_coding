# Writing Whiles 
# Rashiem Kalif Bell

# # 1

# # a
# i = 1
# while  i < 5:
#     print(i)
#     i += 1
# # print(i)

# # b
# i = 2
# while i < 11:
#     print(i)
#     i += 3
# # print(i)

# C
# i = -10
# while i  <= 0:
#     print(i, end= " ")
#     i += 2
# print()

# d 
# i = 1
# while i <= 4:
#     print("****")
#     i += 1

# 2. Write a while loop that prints the letters in “CSCI 150” on separate lines.

# string = "CSCI 150"
# i = 0
# while i < len(string):
#     print(string[i])
#     i += 1

# 3. Create a program that allows the user to enter in a list of numbers, 
# prints them out in sorted order, and prints the sum and average of the numbers. 
# Prompt the user to continue entering numbers, and enter the number ‘0’ 
# when finished.


list = []
prompt = "Please enter a number ('0' to finish: )"
response = float(input(prompt))

while response != 0:
    list.append(response)
    response = float(input(prompt))
print(sorted(list))
print(sum(list))
print(sum(list)/len(list))






# while user_input 
# print