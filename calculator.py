def addition(x,y):
    return x+y
def subtraction(x,y):
    return x-y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero!"
    return x / y

def logarithm(x):
    if x <= 0:
        return "Error: Logarithm is not defined for non-positive numbers!"
    import math
    return round(math.log(x),3)
def square_root(x):
    # if x < 0:
    #     return "Error: Square root is not defined for negative numbers!"
    import math
    return math.sqrt(x)
