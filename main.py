def add(a, b):
    """Function to add two numbers"""
    return a + b

def sub(a, b):
    """Function to subtract two numbers"""
    return a - b

def multi(a, b):
    """Function to multiply two numbers"""
    return a * b

def div(a, b):
    """Function to divide two numbers"""
    return a / b

def calc():
    """Function to perform basic arithmetic operations in a loop"""
    while True:
        # Taking input from the user for two numbers
        num1 = float(input("Enter the First Number: "))
        num2 = float(input("Enter the Second Number: "))
        
        # Asking user to select an operation
        select = input("Select operation (+, -, *, /): ")
        
        # Performing the selected operation
        if select == "+":
            print("Result:", add(num1, num2))
        elif select == "-":
            print("Result:", sub(num1, num2))
        elif select == "*":
            print("Result:", multi(num1, num2))
        elif select == "/":
            # Handling division by zero error
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                print("Result:", div(num1, num2))
        else:
            print("Error: Invalid operation selected.")

# Calling the calculator function
calc()
