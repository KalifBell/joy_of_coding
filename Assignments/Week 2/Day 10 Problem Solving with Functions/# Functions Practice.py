# Functions Practice

def what(num):
    tip = -3
    for i in range(num):
        tip += i
    return tip
print(what(4))


def rectangle(width, height): 
    for i in range(height):
        print("*"* width)
    
    
   
rectangle(5, 3)