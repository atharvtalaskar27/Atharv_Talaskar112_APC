# 1. Create a Python module calculator.py containing functions
# for addition, subtraction, multiplication, and division.
# Create another program that imports the module and performs
# calculations based on user input.
def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    if b == 0:
        return "Division by zero is not possible"
    return a / b
