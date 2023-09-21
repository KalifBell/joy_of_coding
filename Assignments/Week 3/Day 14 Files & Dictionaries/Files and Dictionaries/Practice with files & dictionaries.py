# Practice with files & dictionaries
# Rashiem Kalif Bell

# Write a program that reads in the csv file linked above 
# and outputs the mean, median, and standard deviation for 
# the fall & spring semesters. Make sure to write at least 
# two functions in your final solution. 

# The more generalizable you make your code, the more you 
# may be able to reuse it for your own project later.

import statistics

def output_stats(list):
    print("Mean:", statistics.mean(list))


spring = [] # another word for list is array. 
fall = [] 

csv = "sample_grades.csv"


file = open(csv)
for line in file:
    #rstrip removed \n carrige return showed in print
    list = line.rstrip().split(",") 
    if list[1] == 'Spring 2016':
        spring.append(eval(list[2]))
        print(list)
        print()
    else:
        fall.append(eval(list[2]))
        print(list)

file.close()

print("Fall 2016:")
output_stats(fall)
print()
print("Spring 2016:")
output_stats(spring)

