def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

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
    return math.log(x)

def square_root(x):
    if x < 0:
        return "Error: Square root is not defined for negative numbers!"
    import math
    return math.sqrt(x)

def calculate():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Logarithm")
    print("6. Square Root")

    choice = input("Enter choice (1/2/3/4/5/6): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
    elif choice == '5':
        num = float(input("Enter number: "))
        print("Result:", logarithm(num))
    elif choice == '6':
        num = float(input("Enter number: "))
        print("Result:", square_root(num))
    else:
        print("Invalid input")

if __name__ == "__main__":
    calculate()
