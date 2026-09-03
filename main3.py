# Main program for string_utils module

import string_utils

text = input("Enter a string: ")

print("\nNumber of vowels:", string_utils.count_vowels(text))

print("Reverse of string:", string_utils.reverse_string(text))

if string_utils.is_palindrome(text):
    print("The string is Palindrome.")
else:
    print("The string is not Palindrome.")

print("Number of words:", string_utils.count_words(text))

print("String without spaces:", string_utils.remove_spaces(text))
