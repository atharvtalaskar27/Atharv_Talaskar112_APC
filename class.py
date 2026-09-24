# Question 1:
# Create a class Student with attributes roll_no, name, and marks.
# Create objects for multiple students and display their details and percentage.

class Student:
    def _init_(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def percentage(self):
        return sum(self.marks) / len(self.marks)

    def display(self):
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Percentage:", self.percentage(), "%")
        print("----------------------")


s1 = Student(1, "Shravani", [85, 90, 78, 88, 92])
s2 = Student(2, "Ananya", [90, 85, 89, 95, 91])
s3 = Student(3, "Sneha", [78, 82, 88, 80, 85])

s1.display()
s2.display()
s3.display()

# Question 2:
# Create a class Employee with attributes emp_id, name, and basic_salary.
# Define methods to calculate HRA, DA, and gross salary.

class Employee:
    def _init_(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def calculate_hra(self):
        return self.basic_salary * 0.20

    def calculate_da(self):
        return self.basic_salary * 0.10

    def calculate_gross_salary(self):
        return self.basic_salary + self.calculate_hra() + self.calculate_da()

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Basic Salary:", self.basic_salary)
        print("HRA:", self.calculate_hra())
        print("DA:", self.calculate_da())
        print("Gross Salary:", self.calculate_gross_salary())


e1 = Employee(101, "Priya", 30000)
e1.display()
# Question 3:
# Create a class Rectangle with attributes length and breadth.
# Define methods to calculate area and perimeter.

class Rectangle:
    def _init_(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


r = Rectangle(10, 5)

print("Length:", r.length)
print("Breadth:", r.breadth)
print("Area:", r.area())
print("Perimeter:", r.perimeter())

# Question 4:
# Create a class Circle with an attribute radius.
# Define methods to calculate the area and circumference of the circle.

import math

class Circle:
    def _init_(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def circumference(self):
        return 2 * math.pi * self.radius


c = Circle(7)

print("Radius:", c.radius)
print("Area:", c.area())
print("Circumference:", c.circumference())

# Question 5:
# Create a class Book containing book_id, title, author, and price.
# Create objects for three books and display their information.

class Book:
    def _init_(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print("----------------------")


b1 = Book(101, "Python Basics", "Riya Sharma", 450)
b2 = Book(102, "Data Science", "Neha Patil", 550)
b3 = Book(103, "Web Development", "Priya Desai", 600)

b1.display()
b2.display()
b3.display()

# Question 6:
# Create a class ElectricityBill containing consumer number,
# consumer name, and units consumed.
# Define a method to calculate the electricity bill according to
# different unit slabs.

class ElectricityBill:
    def _init_(self, consumer_no, consumer_name, units):
        self.consumer_no = consumer_no
        self.consumer_name = consumer_name
        self.units = units

    def calculate_bill(self):
        if self.units <= 100:
            bill = self.units * 2
        elif self.units <= 200:
            bill = (100 * 2) + ((self.units - 100) * 3)
        else:
            bill = (100 * 2) + (100 * 3) + ((self.units - 200) * 5)

        return bill

    def display(self):
        print("Consumer Number:", self.consumer_no)
        print("Consumer Name:", self.consumer_name)
        print("Units Consumed:", self.units)
        print("Electricity Bill:", self.calculate_bill())


bill = ElectricityBill(1001, "Kavya", 250)
bill.display()

# Question 7:
# Create a class MobilePhone with attributes brand, model, storage, and price.
# Define methods to display specifications and calculate the price after discount.

class MobilePhone:
    def _init_(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price

    def display_specs(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Storage:", self.storage)
        print("Price:", self.price)

    def price_after_discount(self, discount):
        return self.price - (self.price * discount / 100)


phone = MobilePhone("Samsung", "Galaxy A55", "128 GB", 35000)

phone.display_specs()

discount = 10
print("Discount:", discount, "%")
print("Price After Discount:", phone.price_after_discount(discount))

# Question 8:
# Create a class Patient containing patient ID, name, age, disease,
# and consultation fee.
# Define methods to display patient information and calculate the total bill.

class Patient:
    def _init_(self, patient_id, name, age, disease, consultation_fee):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease
        self.consultation_fee = consultation_fee

    def display(self):
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Disease:", self.disease)
        print("Consultation Fee:", self.consultation_fee)

    def total_bill(self, medicine_charge):
        return self.consultation_fee + medicine_charge


p = Patient(101, "Aarohi", 21, "Fever", 500)

p.display()

medicine_charge = 800
print("Medicine Charge:", medicine_charge)
print("Total Bill:", p.total_bill(medicine_charge))

# Question 9:
# Design an ATM class that allows a user to:
# a) Check balance
# b) Deposit money
# c) Withdraw money
# d) Display account details
# Create an object of the class and implement the operations
# through a menu-driven program.

class ATM:
    def _init_(self, account_no, name, balance):
        self.account_no = account_no
        self.name = name
        self.balance = balance

    def check_balance(self):
        print("Current Balance:", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited:", amount)
        print("New Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount Withdrawn:", amount)
            print("Remaining Balance:", self.balance)
        else:
            print("Insufficient Balance")

    def account_details(self):
        print("Account Number:", self.account_no)
        print("Account Holder:", self.name)
        print("Balance:", self.balance)


atm = ATM(123456, "Meera", 10000)

while True:
    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Account Details")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        atm.check_balance()

    elif choice == 2:
        amount = float(input("Enter deposit amount: "))
        atm.deposit(amount)

    elif choice == 3:
        amount = float(input("Enter withdrawal amount: "))
        atm.withdraw(amount)

    elif choice == 4:
        atm.account_details()

    elif choice == 5:
        print("Thank you for using ATM.")
        break

    else:
        print("Invalid Choice")

# Question 10:
# Create a class Vehicle containing vehicle number, model,
# rental rate, and availability.
# Implement methods to rent and return a vehicle and calculate
# rental charges based on the number of days.

class Vehicle:
    def _init_(self, vehicle_no, model, rental_rate):
        self.vehicle_no = vehicle_no
        self.model = model
        self.rental_rate = rental_rate
        self.available = True

    def rent(self):
        if self.available:
            self.available = False
            print("Vehicle rented successfully.")
        else:
            print("Vehicle is not available.")

    def return_vehicle(self):
        self.available = True
        print("Vehicle returned successfully.")

    def rental_charges(self, days):
        return self.rental_rate * days

    def display(self):
        print("Vehicle Number:", self.vehicle_no)
        print("Model:", self.model)
        print("Rental Rate:", self.rental_rate)
        print("Available:", self.available)


v = Vehicle("MH09AB1234", "Swift", 1500)

v.display()

v.rent()

days = 3
print("Rental Charges for", days, "days:", v.rental_charges(days))

v.return_vehicle()
v.display()

# Question 11:
# Create a class ShoppingCart with customer name and cart ID.
# Initialize these values using a constructor.
# Implement methods to add products, remove products, and calculate
# the total bill.
# Use a destructor to display a message when the shopping cart object
# is destroyed.

class ShoppingCart:
    def _init_(self, customer_name, cart_id):
        self.customer_name = customer_name
        self.cart_id = cart_id
        self.products = []

    def add_product(self, name, price):
        self.products.append([name, price])
        print(name, "added to cart.")

    def remove_product(self, name):
        for product in self.products:
            if product[0] == name:
                self.products.remove(product)
                print(name, "removed from cart.")
                return

        print("Product not found.")

    def total_bill(self):
        total = 0

        for product in self.products:
            total += product[1]

        return total

    def display(self):
        print("Customer Name:", self.customer_name)
        print("Cart ID:", self.cart_id)
        print("Products:", self.products)
        print("Total Bill:", self.total_bill())

    def _del_(self):
        print("Shopping cart object destroyed.")


cart = ShoppingCart("Isha", "C101")

cart.add_product("Laptop Bag", 1200)
cart.add_product("Headphones", 1500)
cart.add_product("Mouse", 500)

cart.display()

cart.remove_product("Mouse")

cart.display()

# Question 12:
# Create a class FoodOrder with order ID, customer name, food item,
# quantity, and price.
# Use a constructor to initialize the order.
# Define a method to calculate the total bill including tax.
# Implement a destructor to display an order completion message.

class FoodOrder:
    def _init_(self, order_id, customer_name, food_item, quantity, price):
        self.order_id = order_id
        self.customer_name = customer_name
        self.food_item = food_item
        self.quantity = quantity
        self.price = price

    def total_bill(self):
        subtotal = self.quantity * self.price
        tax = subtotal * 0.05
        return subtotal + tax

    def display(self):
        print("Order ID:", self.order_id)
        print("Customer Name:", self.customer_name)
        print("Food Item:", self.food_item)
        print("Quantity:", self.quantity)
        print("Price per Item:", self.price)
        print("Total Bill including 5% tax:", self.total_bill())

    def _del_(self):
        print("Order completed successfully.")


order = FoodOrder(101, "Pooja", "Pizza", 2, 300)

order.display()

# Question 13:
# Create a class StudentResult with student name and marks in five subjects.
# Use a constructor to initialize the details.
# Define methods to calculate total, percentage, and grade.
# Implement a destructor to display a suitable message.

class StudentResult:
    def _init_(self, name, marks):
        self.name = name
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total() / 5

    def grade(self):
        percentage = self.percentage()

        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 50:
            return "D"
        else:
            return "F"

    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)
        print("Total:", self.total())
        print("Percentage:", self.percentage(), "%")
        print("Grade:", self.grade())

    def _del_(self):
        print("Student result object destroyed.")


student = StudentResult("Riya", [85, 90, 78, 88, 92])

student.display()
