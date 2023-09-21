# Writing List 2
# by Rashiem Kalif Bell

# Your friend is overwhelmed with the number of candidates running in a 
# local election and is undecided on whom to vote for.  Write a program 
# to help him decide.  Your friend admires experience—at least 5 years—but 
# not too much experience that the candidate is disconnected from the American 
# people (no more than 20 years)—and wants a candidate who agrees with him
#  on at least 80% of the important issues.  Prompt the user to input
#  the candidate’s number of years of experience and the percentage 
# agreement on important issues.

year = float(input("How many years of esperience do you have? "))
agree = float(input("What percentage of the issues do you and the candidate agree on? "))

if 5 <= year <= 20 and agree >= 80:
    print("Vote for this candidate ")
else:
    print("Don't vote for this candidate ")