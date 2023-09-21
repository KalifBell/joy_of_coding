# Kalif Bell
# Learning to write my how funtions
# Write a function, header, that takes a string text and a single character surround as parameters

def header(text, surround):
    length = len(text) + 4 #16 = 12 + 4 lenth of string plus 2 on each side
    # surround = "*"
    # text = "Hello, World"
    print(surround * length)
    print(surround, text, surround)
    print(surround * length)

def main():
    header("Hello, World!", "*")
    header("Python Rocks", "!")
    header("Coders 4 EVER", "+")

main()