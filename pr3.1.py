# Program 1: Print natural numbers up to n

n = int(input("Enter the value of n: "))

for i in range(1, n + 1):
    print(i, end=" ")

# Program 2: Print even numbers up to n

n = int(input("Enter the value of n: "))

for i in range(2, n + 1, 2):
    print(i, end=" ")

# Program 3: Print odd numbers up to n

n = int(input("Enter the value of n: "))

for i in range(1, n + 1, 2):
    print(i, end=" ")


# Program 4: Print the series 1, 2, 4, 8, 16, 32, ... up to 2^n

n = int(input("Enter the value of n: "))

for i in range(n + 1):
    print(2 ** i, end=" ")

# Program 5: Sum of the series 1 + 1/1! + 1/2! + ... + 1/n!

n = int(input("Enter the value of n: "))

fact = 1
sum = 1

for i in range(1, n + 1):
    fact = fact * i
    sum = sum + (1 / fact)

print("Sum of the series =", sum)

# Program 6: Compute cosine series

x = float(input("Enter the value of x: "))
n = int(input("Enter the number of terms: "))

sum = 1
sign = -1

for i in range(2, n + 1, 2):
    fact = 1

    for j in range(1, i + 1):
        fact = fact * j

    term = (x ** i) / fact
    sum = sum + (sign * term)
    sign = sign * -1

print("Cos(x) =", sum)


# Program 7: Check whether square root of a number is prime or not

import math

num = int(input("Enter a number: "))

root = int(math.sqrt(num))

prime = True

if root < 2:
    prime = False
else:
    for i in range(2, root):
        if root % i == 0:
            prime = False
            break

print("Square root =", root)

if prime:
    print("Square root is Prime")
else:
    print("Square root is Not Prime")

# Program 8: Print the pattern

for i in range(3):
    print("A B C")

# Program 9: Print alphabet triangle

n = int(input("Enter the value of n: "))

for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()

# Program 10: Print reverse alphabet triangle

n = int(input("Enter the value of n: "))

for i in range(n, 0, -1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()

