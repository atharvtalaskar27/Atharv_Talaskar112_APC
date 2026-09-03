# 4. Create a module string_utils.py containing functions to count
# vowels, reverse a string, check palindrome, count words, and remove spaces.


def count_vowels(text):
    count = 0

    for ch in text.lower():
        if ch in "aeiou":
            count = count + 1

    return count


def reverse_string(text):
    return text[::-1]


def is_palindrome(text):
    text = text.lower()

    return text == text[::-1]


def count_words(text):
    words = text.split()

    return len(words)


def remove_spaces(text):
    return text.replace(" ", "")
