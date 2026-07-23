"""Write a PYTHON program that reads a value of n and check the number is zero or non zero value."print"""
n=0
n=input("enter number:")
if n==0:
    print("number is zero",n)
else:
    print("number is non zero",n)

"""Write a PYTHON program to find a largest of two numbers."""
a=input("enter number 1st number:")
b=input("enter 2nd number:")

if a>b:
    print("a is greater")
elif a==b:
    print("both number has same value")
else:
    print("b is greater")

    
""".Write a PYTHON program that reads the number and check the no is positive or negative."""


num = float(input("Enter a number: "))


if num > 0:
    print(f"{num} is a Positive number")
elif num < 0:
    print(f"{num} is a Negative number")
else:
    print("The number is Zero")

"""Write a PYTHON program to evaluate the student performance
      If % is >=90 then Excellent performance
      If % is >=80 then  Very Good performance
      If % is >=70 then Good performance
      If % is >=60 then average performance"""

marks_input = input("Enter marks for 5 subjects out of 100, separated by space: ")
mark = list(map(float, marks_input.split()))

total = sum(mark)
percentage = total / 5  

print("Marks:", mark)
print("Total:", total)
print("Percentage:", percentage, "%")


if percentage >= 90:
    print("Excellent performance")
elif percentage >= 80:
    print("Very Good performance")
elif percentage >= 70:
    print("Good performance")
elif percentage >= 60:
    print("Average performance")
else:
    print("Poor performance")

""" Write a PYTHON program to find largest of three numbers."""
a=input("enter 1st number:")
b=input("enter 2nd number:")
c=input("enter 3rd number:")
if a>b and a>c:
    print("a is gretaer:")
elif b>a and b>c:
    print("b is gretaer:")
else:
    print("c is gretaer:")

"""Write a PYTHON program to find smallest of three numbers"""
a=input("enter 1st number:")
b=input("enter 2nd number:")
c=input("enter 3rd number:")
if a<b and a<c:
    print("a is smaller:")
elif b<a and b<c:
    print("b is smaller:")
else:
    print("c is smaller:")

    
"""Write a PYTHON program to check weather number is even or odd """

num=int(input("enter number:"))
if num%2==0:
    print("number is even:")
else:
    print("number is odd:")

"""Write a PYTHON program to check a year for leap year."""
year=int(input("enter number:"))
if year%4==0:
    print("year is leap")
else:
    print("normal is leap year:")
    
"""A company insures its drivers in the following cases:- If the driver is married.- If the driver is unmarried, male and above 30 years        
         of age.      - If the driver is unmarried, female and above 25 years of age.
         
        In all the other cases, the driver is not insured.        Write a PYTHON program to determine whether the driver     
        is insured or not"""


married_status=input("enter marrietal status:")
gender=input("enter gender male/female:")
age=int(input("enter a age:"))
        
if married_status=="Married" or (married_status=="unmarried" and gender=="male" and age>30)or (married_status=="unmarried" and gender=="feamle" and age>25):
                                                                                            print("insure")
else:
    print("not insured:")



#1 create a program to calculate area triangle ,volume of circle and sphere,total suface area of cylender, area of square,
b = float(input("base of triangle:"))
h = float(input("height of triangle:"))
r = float(input("radius:"))
l = float(input("length of cylinder:"))
s = float(input("side of square:"))

area_triangle = 0.5 * b * h
volume_circle = 3.14159 * r * r
volume_sphere = (4/3) * 3.14159 * r * r * r
tsa_cylinder = 2 * 3.14159 * r * (r + l)
area_square = s * s

print("Area Triangle:", area_triangle)
print("Area Circle:", volume_circle)
print("Volume Sphere:", volume_sphere)
print("TSA Cylinder:", tsa_cylinder)
print("Area Square:", area_square)

#2 wap to convert pounds into kg,km into miles 

pounds = float(input("Enter weight in pounds: "))
kg = pounds * 0.45359237
print(f"{pounds} lbs = {kg:.2f} kg")


km = float(input("Enter distance in kilometers: "))
miles = km * 0.621371
print(f"{km} km = {miles:.2f} miles")
 
#3 wap to calculate factorial number,to check whether the number is prime of not
# Calculate Factorial
num = int(input("Enter a number for factorial: "))
factorial = 1
if num < 0:
    print("Factorial does not exist for negative numbers.")
else:
    for i in range(1, num + 1):
        factorial *= i
    print("Factorial of ", num ,"is",factorial)

#4 wap to check number is pallindrome or not

# Check if a number is a palindrome
num = int(input("Enter a number to check palindrome: "))
temp = num
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

if num == reverse:
    print(num "is a palindrome.")
else:
    print(num "is not a palindrome.")

#5 wap to convert decimal to binary,decimal to octal,to hexadecimal:

num=input("enter number:")
print("octa:",oct(num))
print("hexadecimal:",hex(num))
print("decimal:",bin(num))

#6 6.wap to calculate factors of number
num = int(input("Enter a number: "))

print("Factors are:")

for i in range(1, num + 1):
    if num % i == 0:
        print(i)

#7.wap to find ascii value of character 
ch = input("Enter a character: ")

print("ASCII value is:", ord(ch))











