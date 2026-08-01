# Write a PYTHON program to print sum of odd numbers up to n

n = int(input("Enter the value of n: "))

sum = 0

for i in range(1, n + 1, 2):
    sum = sum + i

print("Sum of odd numbers =", sum)


# Write a PYTHON program to print sum of even numbers up to n

n = int(input("Enter the value of n: "))

sum = 0

for i in range(2, n + 1, 2):
    sum = sum + i

print("Sum of even numbers =", sum)


# Write a PYTHON program to print natural numbers up to n in reverse order

n = int(input("Enter the value of n: "))

for i in range(n, 0, -1):
    print(i, end=" ")


# Write a PYTHON program to print Fibonacci series up to n

n = int(input("\nEnter the number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c


# Write a PYTHON program to find factorial of a given number

n = int(input("\nEnter a number: "))

fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial =", fact)


# Write a PYTHON program to check the entered number is prime or not

n = int(input("Enter a number: "))

prime = True

if n < 2:
    prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

if prime:
    print("Prime Number")
else:
    print("Not a Prime Number")


# Write a PYTHON program to find the sum of digits of given number

n = int(input("Enter a number: "))

sum = 0

while n > 0:
    digit = n % 10
    sum = sum + digit
    n = n // 10

print("Sum of digits =", sum)


# Write a PYTHON program to check the entered number is palindrome or not

n = int(input("Enter a number: "))

temp = n
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

if temp == rev:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")


# Write a PYTHON program to reverse the given number

n = int(input("Enter a number: "))

rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

print("Reverse =", rev)


# Write a PYTHON program to print the multiplication table

n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)


# Write a PYTHON program to print the largest of n numbers

n = int(input("Enter how many numbers: "))

largest = int(input("Enter number 1: "))

for i in range(2, n + 1):
    num = int(input("Enter number: "))
    if num > largest:
        largest = num

print("Largest number =", largest)


# Write a PYTHON program to print smallest of n numbers

n = int(input("Enter how many numbers: "))

smallest = int(input("Enter number 1: "))

for i in range(2, n + 1):
    num = int(input("Enter number: "))
    if num < smallest:
        smallest = num

print("Smallest number =", smallest)
