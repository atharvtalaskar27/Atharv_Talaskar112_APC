# Main program for recursive_utils module

import recursive_utils

n = int(input("Enter a number: "))

print("\nFactorial:", recursive_utils.factorial(n))

print("Sum of digits:", recursive_utils.sum_of_digits(n))

print("Binary:", recursive_utils.binary(n))

print("\nFibonacci Series:")

for i in range(n):
    print(recursive_utils.fibonacci(i), end=" ")
