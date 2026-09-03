# Main program for number_utils module

import number_utils

n = int(input("Enter a number: "))

if number_utils.is_prime(n):
    print("The number is Prime.")
else:
    print("The number is not Prime.")

if number_utils.is_palindrome(n):
    print("The number is Palindrome.")
else:
    print("The number is not Palindrome.")

if number_utils.is_armstrong(n):
    print("The number is Armstrong.")
else:
    print("The number is not Armstrong.")

if number_utils.is_perfect(n):
    print("The number is Perfect.")
else:
    print("The number is not Perfect.")
