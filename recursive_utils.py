# 6. Create a module containing recursive functions for factorial,
# Fibonacci series, sum of digits, and binary conversion.
# Import and use these functions from another program.


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_of_digits(n // 10)


def binary(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return binary(n // 2) + str(n % 2)
