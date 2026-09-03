# Main program for calculator module
import calculator
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Addition:", calculator.addition(a, b))
print("Subtraction:", calculator.subtraction(a, b))
print("Multiplication:", calculator.multiplication(a, b))
print("Division:", calculator.division(a, b))
