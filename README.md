# SIMPLE CALCULATOR

## Overview:
This Python Calculator Program is a simple command-line utility that allows users to perform basic arithmetic operations. The program supports addition, subtraction, multiplication, and division. It repeatedly prompts the user to enter two numbers and select an operation, then displays the result of the chosen operation.

## Features:
- **Addition**: Adds two numbers.
- **Subtraction**: Subtracts the second number from the first number.
- **Multiplication**: Multiplies two numbers.
- **Division**: Divides the first number by the second number.

# How It Works:

**1. Function Definitions:**

   - **add(a, b)**: Returns the sum of a and b.
   - **sub(a, b)**: Returns the difference between a and b.
   - **multi(a, b)**: Returns the product of a and b.
   - **div(a, b)**: Returns the division of a by b.

**2. Main Function:**

**calc()**:
- Runs an infinite loop to continually prompt the user for input.
- Asks the user to input two numbers (num1 and num2).
- Prompts the user to select an operation (+, -, *, /).
- Depending on the selected operation, it calls the corresponding function (add, sub, multi, div) and prints the result.
- If an invalid operation is selected, it prints an error message.

**3. User Interaction:**

- The program uses a while loop to keep running until manually stopped by the user.
- Each iteration prompts the user for the first number, the second number, and the desired operation.
- The appropriate arithmetic function is called based on the user's selection, and the result is displayed.

## Example Usage:
Here’s a step-by-step example of how the program can be used:
- Run the program.
- Enter the first number: 10
- Enter the second number: 5
- Select an operation (+, -, *, /): +
- The program will output: Result: 15.0
- The program will then prompt the user to enter new numbers and select another operation.

## Notes
- Ensure that the numbers entered are valid floating-point numbers.
- Division by zero will raise an error; additional error handling can be implemented to manage such cases.
