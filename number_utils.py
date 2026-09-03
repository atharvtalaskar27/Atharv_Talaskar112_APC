# 3. Create a module number_utils.py containing functions to check
# whether a number is prime, palindrome, Armstrong, or perfect.
# Import the required functions into a main program.
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True
def is_palindrome(n):
    original = n
    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10

    return original == reverse
def is_armstrong(n):
    original = n
    digits = len(str(n))
    total = 0

    while n > 0:
        digit = n % 10
        total = total + digit ** digits
        n = n // 10

    return original == total
def is_perfect(n):
    total = 0

    for i in range(1, n):
        if n % i == 0:
            total = total + i

    return total == n
