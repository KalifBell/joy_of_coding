# Reading List 3
# Rashiem Bell

def square_it(string):
    for i in range(len(string)):
        for j in range(len(string)):
            print(string[(i + j) % len(string)], end=" ")
        print()

def count_it(string, letters):
    total = 0
    for s in string:
        if s in letters:
            total += 1
    return total

list = "Drew University Alma Mater by John Barclay".split(" ")
VOWELS = ["A", "E", "I", "O", "U"]
for s in list:
    print("\n==", s, "==")
    if len(s) % 2 == 1:
        print(count_it(s, "aeiouAEIOU"))
        square_it(s)
    else:
        print(count_it(s.upper(), VOWELS))

        # full stack, data science



#square_it("Mater")