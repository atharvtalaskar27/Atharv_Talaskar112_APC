# ============================================================
# INHERITANCE - PROGRAM 1
# ============================================================
# Create a class Employee with attributes emp_id, name, and salary.
# Create a derived class Manager that inherits from Employee and contains
# an additional attribute department.
# Display all employee and manager details and calculate the manager's annual
# salary.

class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)


class Manager(Employee):
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)
        self.department = department

    def annual_salary(self):
        return self.salary * 12

    def display_manager(self):
        self.display()
        print("Department:", self.department)
        print("Annual Salary:", self.annual_salary())


manager = Manager(101, "Atharv", 50000, "IT")

print("----- Manager Details -----")
manager.display_manager()


# ============================================================
# INHERITANCE - PROGRAM 2
# ============================================================
# Create a base class Vehicle with attributes brand and model.
# Create a derived class Car with additional attributes fuel_type and price.
# Define methods to display vehicle details and calculate the discounted price
# of the car.

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


class Car(Vehicle):
    def __init__(self, brand, model, fuel_type, price):
        super().__init__(brand, model)
        self.fuel_type = fuel_type
        self.price = price

    def discounted_price(self, discount):
        return self.price - (self.price * discount / 100)

    def display_car(self, discount):
        self.display()
        print("Fuel Type:", self.fuel_type)
        print("Price:", self.price)
        print("Discount:", discount, "%")
        print("Discounted Price:", self.discounted_price(discount))


car = Car("Toyota", "Fortuner", "Diesel", 4000000)

print("\n----- Car Details -----")
car.display_car(10)


# ============================================================
# INHERITANCE - PROGRAM 3
# ============================================================
# Create two classes Academic and Sports. The Academic class should store
# marks obtained by a student, while the Sports class should store sports
# points. Create a class Student that inherits from both classes and
# calculates the student's overall performance.

class Academic:
    def __init__(self, marks):
        self.marks = marks


class Sports:
    def __init__(self, sports_points):
        self.sports_points = sports_points


class Student(Academic, Sports):
    def __init__(self, name, marks, sports_points):
        Academic.__init__(self, marks)
        Sports.__init__(self, sports_points)
        self.name = name

    def overall_performance(self):
        return self.marks + self.sports_points

    def display(self):
        print("Name:", self.name)
        print("Academic Marks:", self.marks)
        print("Sports Points:", self.sports_points)
        print("Overall Performance:", self.overall_performance())


student = Student("Atharv", 85, 10)

print("\n----- Student Performance -----")
student.display()


# ============================================================
# INHERITANCE - PROGRAM 4
# ============================================================
# Create classes PersonalDetails and ProfessionalDetails. Store personal
# information such as name and age in the first class and employee ID,
# designation, and salary in the second class. Create an Employee class
# that inherits from both classes and displays complete employee information.

class PersonalDetails:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class ProfessionalDetails:
    def __init__(self, emp_id, designation, salary):
        self.emp_id = emp_id
        self.designation = designation
        self.salary = salary


class Employee(PersonalDetails, ProfessionalDetails):
    def __init__(self, name, age, emp_id, designation, salary):
        PersonalDetails.__init__(self, name, age)
        ProfessionalDetails.__init__(
            self, emp_id, designation, salary
        )

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.emp_id)
        print("Designation:", self.designation)
        print("Salary:", self.salary)


employee = Employee(
    "Atharv",
    20,
    101,
    "Software Developer",
    60000
)

print("\n----- Complete Employee Information -----")
employee.display()


# ============================================================
# INHERITANCE - PROGRAM 5
# ============================================================
# Create a class Person containing name and age. Derive a class Student
# from Person with roll number and course. Further derive a class
# ResearchStudent from Student with research topic and guide name.
# Display all details.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course


class ResearchStudent(Student):
    def __init__(self, name, age, roll_no, course,
                 research_topic, guide_name):
        super().__init__(name, age, roll_no, course)
        self.research_topic = research_topic
        self.guide_name = guide_name

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll Number:", self.roll_no)
        print("Course:", self.course)
        print("Research Topic:", self.research_topic)
        print("Guide Name:", self.guide_name)


research_student = ResearchStudent(
    "Atharv",
    20,
    101,
    "B.Tech CSE",
    "Artificial Intelligence",
    "Dr. Sharma"
)

print("\n----- Research Student Details -----")
research_student.display()


# ============================================================
# INHERITANCE - PROGRAM 6
# ============================================================
# Create a base class BankAccount with account number and balance.
# Derive SavingsAccount from it with an interest rate. Further derive
# PremiumSavingsAccount with additional benefits. Define methods to
# calculate interest and display account details.

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def display(self):
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate / 100

    def display_savings(self):
        self.display()
        print("Interest Rate:", self.interest_rate, "%")
        print("Interest:", self.calculate_interest())


class PremiumSavingsAccount(SavingsAccount):
    def __init__(self, account_number, balance, interest_rate, benefits):
        super().__init__(account_number, balance, interest_rate)
        self.benefits = benefits

    def display_premium(self):
        self.display_savings()
        print("Additional Benefits:", self.benefits)


account = PremiumSavingsAccount(
    123456,
    100000,
    6,
    "Free ATM and Premium Support"
)

print("\n----- Premium Savings Account -----")
account.display_premium()


# ============================================================
# INHERITANCE - PROGRAM 7
# ============================================================
# Create a base class Shape containing a method to display the name
# of the shape. Create three derived classes Circle, Rectangle,
# and Triangle. Each class should implement its own method to calculate
# the area.

import math


class Shape:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print("Shape:", self.name)


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


circle = Circle(5)
rectangle = Rectangle(10, 5)
triangle = Triangle(8, 6)

print("\n----- Circle -----")
circle.display_name()
print("Area:", circle.area())

print("\n----- Rectangle -----")
rectangle.display_name()
print("Area:", rectangle.area())

print("\n----- Triangle -----")
triangle.display_name()
print("Area:", triangle.area())


# ============================================================
# INHERITANCE - PROGRAM 8
# ============================================================
# Create a base class Employee containing employee ID, name, and basic
# salary. Create derived classes Manager, Developer, and Tester.
# Each derived class should calculate salary differently based on its
# respective allowances.

class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Basic Salary:", self.basic_salary)


class Manager(Employee):
    def calculate_salary(self):
        return self.basic_salary + (self.basic_salary * 30 / 100)


class Developer(Employee):
    def calculate_salary(self):
        return self.basic_salary + (self.basic_salary * 20 / 100)


class Tester(Employee):
    def calculate_salary(self):
        return self.basic_salary + (self.basic_salary * 15 / 100)


manager = Manager(101, "Rahul", 50000)
developer = Developer(102, "Amit", 45000)
tester = Tester(103, "Priya", 40000)

print("\n----- Manager -----")
manager.display()
print("Final Salary:", manager.calculate_salary())

print("\n----- Developer -----")
developer.display()
print("Final Salary:", developer.calculate_salary())

print("\n----- Tester -----")
tester.display()
print("Final Salary:", tester.calculate_salary())


# ============================================================
# INHERITANCE - PROGRAM 9
# ============================================================
# Create a class Person. Derive Student and Faculty from Person.
# Create another class TeachingAssistant that inherits from both
# Student and Faculty. Display the details and demonstrate the use
# of multiple and hierarchical inheritance together.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no

    def display_student(self):
        print("Student Name:", self.name)
        print("Age:", self.age)
        print("Roll Number:", self.roll_no)


class Faculty(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_faculty(self):
        print("Faculty Name:", self.name)
        print("Age:", self.age)
        print("Subject:", self.subject)


class TeachingAssistant(Student, Faculty):
    def __init__(self, name, age, roll_no, subject):
        Person.__init__(self, name, age)
        self.roll_no = roll_no
        self.subject = subject

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll Number:", self.roll_no)
        print("Subject:", self.subject)


student = Student("Atharv", 20, 101)
faculty = Faculty("Dr. Sharma", 40, "Python")
ta = TeachingAssistant("Atharv", 20, 101, "Python")

print("\n----- Student -----")
student.display_student()

print("\n----- Faculty -----")
faculty.display_faculty()

print("\n----- Teaching Assistant -----")
ta.display()


# ============================================================
# INHERITANCE - PROGRAM 10
# ============================================================
# Create a base class Vehicle. Derive Car and Bike from Vehicle.
# Create a class SportsCar that inherits from Car and another class
# ElectricBike that inherits from Bike. Add suitable attributes and
# methods to demonstrate a combination of inheritance types.

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def display_brand(self):
        print("Brand:", self.brand)


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def display_car(self):
        self.display_brand()
        print("Car Model:", self.model)


class Bike(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def display_bike(self):
        self.display_brand()
        print("Bike Model:", self.model)


class SportsCar(Car):
    def __init__(self, brand, model, speed):
        super().__init__(brand, model)
        self.speed = speed

    def display_sports_car(self):
        self.display_car()
        print("Top Speed:", self.speed, "km/h")


class ElectricBike(Bike):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    def display_electric_bike(self):
        self.display_bike()
        print("Battery Capacity:", self.battery_capacity, "kWh")


sports_car = SportsCar("BMW", "M4", 250)
electric_bike = ElectricBike("Ather", "450X", 3.7)

print("\n----- Sports Car -----")
sports_car.display_sports_car()

print("\n----- Electric Bike -----")
electric_bike.display_electric_bike()


# ============================================================
# INHERITANCE - PROGRAM 11
# ============================================================
# Create a base class Student with attributes roll_no, name, and course.
# Derive a class Result that stores marks in three subjects and calculates
# total marks, percentage, and grade.

class Student:
    def __init__(self, roll_no, name, course):
        self.roll_no = roll_no
        self.name = name
        self.course = course


class Result(Student):
    def __init__(self, roll_no, name, course, mark1, mark2, mark3):
        super().__init__(roll_no, name, course)
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def total_marks(self):
        return self.mark1 + self.mark2 + self.mark3

    def percentage(self):
        return self.total_marks() / 3

    def grade(self):
        percentage = self.percentage()

        if percentage >= 75:
            return "A"
        elif percentage >= 60:
            return "B"
        elif percentage >= 50:
            return "C"
        elif percentage >= 35:
            return "D"
        else:
            return "F"

    def display(self):
        print("Roll Number:", self.roll_no)
        print("Name:", self.name)
        print("Course:", self.course)
        print("Subject 1:", self.mark1)
        print("Subject 2:", self.mark2)
        print("Subject 3:", self.mark3)
        print("Total Marks:", self.total_marks())
        print("Percentage:", self.percentage())
        print("Grade:", self.grade())


result = Result(
    101,
    "Atharv",
    "B.Tech CSE",
    85,
    78,
    92
)

print("\n----- Student Result -----")
result.display()


# ============================================================
# INHERITANCE - PROGRAM 12
# ============================================================
# Create a class Product with product ID, name, and price. Derive
# ElectronicProduct with additional attributes such as brand and warranty.
# Calculate the final price after applying a discount.

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price


class ElectronicProduct(Product):
    def __init__(self, product_id, name, price, brand, warranty):
        super().__init__(product_id, name, price)
        self.brand = brand
        self.warranty = warranty

    def final_price(self, discount):
        return self.price - (self.price * discount / 100)

    def display(self, discount):
        print("Product ID:", self.product_id)
        print("Name:", self.name)
        print("Price:", self.price)
        print("Brand:", self.brand)
        print("Warranty:", self.warranty, "years")
        print("Discount:", discount, "%")
        print("Final Price:", self.final_price(discount))


product = ElectronicProduct(
    501,
    "Laptop",
    60000,
    "Dell",
    2
)

print("\n----- Electronic Product -----")
product.display(10)


# ============================================================
# INHERITANCE - PROGRAM 13
# ============================================================
# Create classes Printer and Scanner with suitable methods for printing
# and scanning documents. Create a MultifunctionDevice class that inherits
# from both and supports both operations.

class Printer:
    def print_document(self, document):
        print("Printing document:", document)


class Scanner:
    def scan_document(self, document):
        print("Scanning document:", document)


class MultifunctionDevice(Printer, Scanner):
    def display(self):
        print("Multifunction Device supports printing and scanning.")


device = MultifunctionDevice()

print("\n----- Multifunction Device -----")
device.display()
device.print_document("Report.pdf")
device.scan_document("Certificate.pdf")


# ============================================================
# INHERITANCE - PROGRAM 14
# ============================================================
# Create classes Camera and Phone. The Camera class should provide
# methods for taking photographs, while Phone should provide methods
# for making calls. Create a Smartphone class inheriting from both.

class Camera:
    def take_photo(self):
        print("Taking a photograph...")


class Phone:
    def make_call(self, number):
        print("Calling:", number)


class Smartphone(Camera, Phone):
    def display(self):
        print("Smartphone supports camera and phone operations.")


smartphone = Smartphone()

print("\n----- Smartphone -----")
smartphone.display()
smartphone.take_photo()
smartphone.make_call("9876543210")


# ============================================================
# INHERITANCE - PROGRAM 15
# ============================================================
# Create a class Person with name and age. Derive Student with roll
# number and course. Further derive ResearchStudent with research topic
# and guide name.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course


class ResearchStudent(Student):
    def __init__(self, name, age, roll_no, course,
                 research_topic, guide_name):
        super().__init__(name, age, roll_no, course)
        self.research_topic = research_topic
        self.guide_name = guide_name

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll Number:", self.roll_no)
        print("Course:", self.course)
        print("Research Topic:", self.research_topic)
        print("Guide Name:", self.guide_name)


research_student = ResearchStudent(
    "Atharv",
    20,
    101,
    "B.Tech CSE",
    "Machine Learning",
    "Dr. Sharma"
)

print("\n----- Research Student Details -----")
research_student.display()



# ============================================================
# INHERITANCE - PROGRAM 16
# ============================================================
# Create a class Person with name and age. Derive Student with roll
# number and course. Further derive ResearchStudent with research topic
# and guide name.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course


class ResearchStudent(Student):
    def __init__(self, name, age, roll_no, course,
                 research_topic, guide_name):
        super().__init__(name, age, roll_no, course)
        self.research_topic = research_topic
        self.guide_name = guide_name

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll Number:", self.roll_no)
        print("Course:", self.course)
        print("Research Topic:", self.research_topic)
        print("Guide Name:", self.guide_name)


student = ResearchStudent(
    "Atharv", 20, 101, "B.Tech CSE",
    "Artificial Intelligence", "Dr. Sharma"
)

print("----- Research Student Details -----")
student.display()


# ============================================================
# INHERITANCE - PROGRAM 17
# ============================================================
# Create a base class Animal with common attributes and methods.
# Derive Dog, Cat, and Cow classes and implement their specific
# sounds and behaviors.

class Animal:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Animal Name:", self.name)


class Dog(Animal):
    def sound(self):
        print("Sound: Woof Woof")

    def behavior(self):
        print("Behavior: Dog is loyal.")


class Cat(Animal):
    def sound(self):
        print("Sound: Meow")

    def behavior(self):
        print("Behavior: Cat is independent.")


class Cow(Animal):
    def sound(self):
        print("Sound: Moo")

    def behavior(self):
        print("Behavior: Cow gives milk.")


dog = Dog("Tommy")
cat = Cat("Kitty")
cow = Cow("Gauri")

print("\n----- Dog -----")
dog.display()
dog.sound()
dog.behavior()

print("\n----- Cat -----")
cat.display()
cat.sound()
cat.behavior()

print("\n----- Cow -----")
cow.display()
cow.sound()
cow.behavior()


# ============================================================
# INHERITANCE - PROGRAM 18
# ============================================================
# Create a class Person and derive Doctor and Patient.
# Create additional classes representing Surgeon and MedicalResearcher.
# Design the hierarchy so that the program demonstrates multiple
# inheritance along with hierarchical inheritance.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Doctor(Person):
    def __init__(self, name, age, specialization):
        super().__init__(name, age)
        self.specialization = specialization

    def display_doctor(self):
        self.display_person()
        print("Specialization:", self.specialization)


class Patient(Person):
    def __init__(self, name, age, disease):
        super().__init__(name, age)
        self.disease = disease

    def display_patient(self):
        self.display_person()
        print("Disease:", self.disease)


class Surgeon(Doctor):
    def __init__(self, name, age, specialization, surgery_type):
        super().__init__(name, age, specialization)
        self.surgery_type = surgery_type

    def display_surgeon(self):
        self.display_doctor()
        print("Surgery Type:", self.surgery_type)


class MedicalResearcher(Doctor, Patient):
    def __init__(self, name, age, specialization, disease):
        Person.__init__(self, name, age)
        self.specialization = specialization
        self.disease = disease

    def display_researcher(self):
        self.display_person()
        print("Specialization:", self.specialization)
        print("Research Disease:", self.disease)


surgeon = Surgeon(
    "Dr. Rahul", 45, "General Surgery", "Heart Surgery"
)

researcher = MedicalResearcher(
    "Dr. Priya", 40, "Medical Research", "Cancer"
)

print("\n----- Surgeon -----")
surgeon.display_surgeon()

print("\n----- Medical Researcher -----")
researcher.display_researcher()


# ============================================================
# POLYMORPHISM - PROGRAM 1
# ============================================================
# Create a base class Shape with a method area(). Derive Circle,
# Rectangle, and Triangle classes and override the area() method
# in each class. Create objects of each class and demonstrate
# runtime polymorphism.

import math


class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


shapes = [
    Circle(5),
    Rectangle(10, 5),
    Triangle(8, 6)
]

print("\n----- Shape Areas -----")

for shape in shapes:
    print("Area:", shape.area())


# ============================================================
# POLYMORPHISM - PROGRAM 2
# ============================================================
# Create a base class Employee with a method calculate_salary().
# Derive Manager, Developer, and Tester classes. Override the method
# in each class to calculate salary according to the employee's role.

class Employee:
    def calculate_salary(self):
        pass


class Manager(Employee):
    def calculate_salary(self):
        return 70000


class Developer(Employee):
    def calculate_salary(self):
        return 60000


class Tester(Employee):
    def calculate_salary(self):
        return 50000


employees = [
    Manager(),
    Developer(),
    Tester()
]

print("\n----- Employee Salaries -----")

for employee in employees:
    print("Salary:", employee.calculate_salary())


# ============================================================
# POLYMORPHISM - PROGRAM 3
# ============================================================
# Create a base class Vehicle with a method start(). Derive Car,
# Bike, and Bus classes and override start() to display the
# starting behavior of each vehicle.

class Vehicle:
    def start(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car starts with a key.")


class Bike(Vehicle):
    def start(self):
        print("Bike starts with a self-start button.")


class Bus(Vehicle):
    def start(self):
        print("Bus starts with a diesel engine.")


vehicles = [
    Car(),
    Bike(),
    Bus()
]

print("\n----- Vehicle Starting -----")

for vehicle in vehicles:
    vehicle.start()


# ============================================================
# POLYMORPHISM - PROGRAM 4
# ============================================================
# Create a base class Animal with a method sound(). Create subclasses
# Dog, Cat, Cow, and Lion. Override sound() in each class to display
# the appropriate sound.

class Animal:
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        print("Dog: Woof Woof")


class Cat(Animal):
    def sound(self):
        print("Cat: Meow")


class Cow(Animal):
    def sound(self):
        print("Cow: Moo")


class Lion(Animal):
    def sound(self):
        print("Lion: Roar")


animals = [
    Dog(),
    Cat(),
    Cow(),
    Lion()
]

print("\n----- Animal Sounds -----")

for animal in animals:
    animal.sound()


# ============================================================
# POLYMORPHISM - PROGRAM 5
# ============================================================
# Create a base class Notification with a method send(). Derive
# EmailNotification, SMSNotification, and PushNotification.
# Override send() to display the appropriate notification method.

class Notification:
    def send(self):
        pass


class EmailNotification(Notification):
    def send(self):
        print("Sending notification through Email.")


class SMSNotification(Notification):
    def send(self):
        print("Sending notification through SMS.")


class PushNotification(Notification):
    def send(self):
        print("Sending notification through Push Notification.")


notifications = [
    EmailNotification(),
    SMSNotification(),
    PushNotification()
]

print("\n----- Notifications -----")

for notification in notifications:
    notification.send()


# ============================================================
# POLYMORPHISM - PROGRAM 6
# ============================================================
# Create a base class Student with a method calculate_grade().
# Derive EngineeringStudent, MedicalStudent, and ManagementStudent.
# Override the method according to different grading criteria.

class Student:
    def calculate_grade(self, marks):
        pass


class EngineeringStudent(Student):
    def calculate_grade(self, marks):
        if marks >= 80:
            return "A"
        elif marks >= 60:
            return "B"
        elif marks >= 40:
            return "C"
        else:
            return "F"


class MedicalStudent(Student):
    def calculate_grade(self, marks):
        if marks >= 85:
            return "A"
        elif marks >= 70:
            return "B"
        elif marks >= 50:
            return "C"
        else:
            return "F"


class ManagementStudent(Student):
    def calculate_grade(self, marks):
        if marks >= 75:
            return "A"
        elif marks >= 60:
            return "B"
        elif marks >= 45:
            return "C"
        else:
            return "F"


students = [
    EngineeringStudent(),
    MedicalStudent(),
    ManagementStudent()
]

marks = 78

print("\n----- Student Grades -----")

for student in students:
    print("Grade:", student.calculate_grade(marks))


# ============================================================
# POLYMORPHISM - PROGRAM 7
# ============================================================
# Create a base class BankAccount with a method calculate_interest().
# Derive SavingsAccount, CurrentAccount, and FixedDepositAccount.
# Override the method to calculate interest differently for each
# account type.

class BankAccount:
    def calculate_interest(self, balance):
        pass


class SavingsAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.06


class CurrentAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.02


class FixedDepositAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.08


accounts = [
    SavingsAccount(),
    CurrentAccount(),
    FixedDepositAccount()
]

balance = 100000

print("\n----- Bank Account Interest -----")

for account in accounts:
    print("Interest:", account.calculate_interest(balance))


# ============================================================
# POLYMORPHISM - PROGRAM 8
# ============================================================
# Create a base class Report with a method generate(). Derive
# PDFReport, ExcelReport, and HTMLReport. Override generate()
# in each class. Write a function that accepts any report object
# and calls generate().

class Report:
    def generate(self):
        pass


class PDFReport(Report):
    def generate(self):
        print("Generating PDF Report.")


class ExcelReport(Report):
    def generate(self):
        print("Generating Excel Report.")


class HTMLReport(Report):
    def generate(self):
        print("Generating HTML Report.")


def generate_report(report):
    report.generate()


reports = [
    PDFReport(),
    ExcelReport(),
    HTMLReport()
]

print("\n----- Reports -----")

for report in reports:
    generate_report(report)


# ============================================================
# POLYMORPHISM - PROGRAM 9
# ============================================================
# Create a class Distance with feet and inches.
# Overload the + operator to add two distance objects and display
# the result in normalized form.

class Distance:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __add__(self, other):
        total_inches = self.inches + other.inches
        total_feet = self.feet + other.feet

        if total_inches >= 12:
            total_feet += total_inches // 12
            total_inches = total_inches % 12

        return Distance(total_feet, total_inches)

    def display(self):
        print(self.feet, "feet", self.inches, "inches")


d1 = Distance(5, 8)
d2 = Distance(4, 7)

d3 = d1 + d2

print("\n----- Distance Addition -----")
print("Distance 1:")
d1.display()

print("Distance 2:")
d2.display()

print("Result:")
d3.display()


# ============================================================
# POLYMORPHISM - PROGRAM 10
# ============================================================
# Create a class Student containing the student's name and total marks.
# Overload the > and < operators to compare the marks of two students.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks

    def __lt__(self, other):
        return self.marks < other.marks


student1 = Student("Atharv", 85)
student2 = Student("Rahul", 75)

print("\n----- Student Comparison -----")

print("Student 1 > Student 2:", student1 > student2)
print("Student 1 < Student 2:", student1 < student2)


# ============================================================
# POLYMORPHISM - PROGRAM 11
# ============================================================
# Create a class Product with product name and price. Overload the ==
# and > operators to compare two products based on their prices.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

    def __gt__(self, other):
        return self.price > other.price


product1 = Product("Laptop", 60000)
product2 = Product("Mobile", 40000)

print("\n----- Product Comparison -----")

print("Product 1 == Product 2:", product1 == product2)
print("Product 1 > Product 2:", product1 > product2)


# ============================================================
# POLYMORPHISM - PROGRAM 12
# ============================================================
# Develop an online shopping payment module using polymorphism.
# Create a base class Payment and derived classes UPIPayment,
# CardPayment, and WalletPayment. Each class should implement its
# own make_payment() method. Demonstrate polymorphism using a
# common function.

class Payment:
    def make_payment(self, amount):
        pass


class UPIPayment(Payment):
    def make_payment(self, amount):
        print("Payment of Rs.", amount, "made using UPI.")


class CardPayment(Payment):
    def make_payment(self, amount):
        print("Payment of Rs.", amount, "made using Card.")


class WalletPayment(Payment):
    def make_payment(self, amount):
        print("Payment of Rs.", amount, "made using Wallet.")


def process_payment(payment, amount):
    payment.make_payment(amount)


payments = [
    UPIPayment(),
    CardPayment(),
    WalletPayment()
]

print("\n----- Online Shopping Payments -----")

for payment in payments:
    process_payment(payment, 2500)


# ============================================================
# POLYMORPHISM - PROGRAM 13
# ============================================================
# Create a base class Person with a method display_role(). Derive Student,
# Faculty, and Administrator. Override the method to display the
# respective role. Store all objects in a list and invoke the same method
# using a loop.

class Person:
    def display_role(self):
        pass


class Student(Person):
    def display_role(self):
        print("Role: Student")


class Faculty(Person):
    def display_role(self):
        print("Role: Faculty")


class Administrator(Person):
    def display_role(self):
        print("Role: Administrator")


people = [
    Student(),
    Faculty(),
    Administrator()
]

print("----- Person Roles -----")

for person in people:
    person.display_role()


# ============================================================
# POLYMORPHISM - PROGRAM 14
# ============================================================
# Create a base class Media with a method play(). Derive Audio,
# Video, and Podcast. Override play() according to the media type.

class Media:
    def play(self):
        pass


class Audio(Media):
    def play(self):
        print("Playing audio.")


class Video(Media):
    def play(self):
        print("Playing video.")


class Podcast(Media):
    def play(self):
        print("Playing podcast.")


media_list = [
    Audio(),
    Video(),
    Podcast()
]

print("\n----- Media Playback -----")

for media in media_list:
    media.play()


# ============================================================
# POLYMORPHISM - PROGRAM 15
# ============================================================
# Create a base class SmartDevice with methods turn_on() and turn_off().
# Derive Light, Fan, AC, and TV. Override the methods according to
# each device.

class SmartDevice:
    def turn_on(self):
        pass

    def turn_off(self):
        pass


class Light(SmartDevice):
    def turn_on(self):
        print("Light is turned ON.")

    def turn_off(self):
        print("Light is turned OFF.")


class Fan(SmartDevice):
    def turn_on(self):
        print("Fan is turned ON.")

    def turn_off(self):
        print("Fan is turned OFF.")


class AC(SmartDevice):
    def turn_on(self):
        print("AC is turned ON.")

    def turn_off(self):
        print("AC is turned OFF.")


class TV(SmartDevice):
    def turn_on(self):
        print("TV is turned ON.")

    def turn_off(self):
        print("TV is turned OFF.")


devices = [
    Light(),
    Fan(),
    AC(),
    TV()
]

print("\n----- Smart Devices -----")

for device in devices:
    device.turn_on()
    device.turn_off()


# ============================================================
# ABSTRACTION - PROGRAM 1
# ============================================================
# Create an abstract class Shape with an abstract method area().
# Derive Circle, Rectangle, and Triangle classes and implement
# the area() method for each shape. Create objects of the derived
# classes and display their areas.

from abc import ABC, abstractmethod
import math


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


circle = Circle(5)
rectangle = Rectangle(10, 5)
triangle = Triangle(8, 6)

print("\n----- Shape Areas -----")
print("Circle Area:", circle.area())
print("Rectangle Area:", rectangle.area())
print("Triangle Area:", triangle.area())


# ============================================================
# ABSTRACTION - PROGRAM 2
# ============================================================
# Create an abstract class Vehicle with abstract methods start()
# and stop(). Derive Car, Bike, and Bus classes and implement
# these methods.

from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car starts.")

    def stop(self):
        print("Car stops.")


class Bike(Vehicle):
    def start(self):
        print("Bike starts.")

    def stop(self):
        print("Bike stops.")


class Bus(Vehicle):
    def start(self):
        print("Bus starts.")

    def stop(self):
        print("Bus stops.")


vehicles = [
    Car(),
    Bike(),
    Bus()
]

print("\n----- Vehicles -----")

for vehicle in vehicles:
    vehicle.start()
    vehicle.stop()


# ============================================================
# ABSTRACTION - PROGRAM 3
# ============================================================
# Create an abstract class BankAccount with abstract methods deposit()
# and withdraw(). Derive SavingsAccount and CurrentAccount and
# implement the required operations.

from abc import ABC, abstractmethod


class BankAccount(ABC):

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


class SavingsAccount(BankAccount):
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
        print("Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

        print("Balance:", self.balance)


class CurrentAccount(BankAccount):
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
        print("Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

        print("Balance:", self.balance)


savings = SavingsAccount(10000)
current = CurrentAccount(20000)

print("\n----- Savings Account -----")
savings.deposit(5000)
savings.withdraw(3000)

print("\n----- Current Account -----")
current.deposit(5000)
current.withdraw(4000)


# ============================================================
# ABSTRACTION - PROGRAM 4
# ============================================================
# Create an abstract class FoodOrder with abstract methods
# calculate_bill() and delivery_charge(). Derive RestaurantOrder
# and HomeDeliveryOrder and implement the methods appropriately.

from abc import ABC, abstractmethod


class FoodOrder(ABC):

    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def delivery_charge(self):
        pass


class RestaurantOrder(FoodOrder):
    def __init__(self, food_price):
        self.food_price = food_price

    def calculate_bill(self):
        return self.food_price

    def delivery_charge(self):
        return 0


class HomeDeliveryOrder(FoodOrder):
    def __init__(self, food_price):
        self.food_price = food_price

    def calculate_bill(self):
        return self.food_price + self.delivery_charge()

    def delivery_charge(self):
        return 50


restaurant = RestaurantOrder(500)
home_delivery = HomeDeliveryOrder(500)

print("\n----- Restaurant Order -----")
print("Food Bill:", restaurant.calculate_bill())
print("Delivery Charge:", restaurant.delivery_charge())

print("\n----- Home Delivery Order -----")
print("Food Bill:", home_delivery.food_price)
print("Delivery Charge:", home_delivery.delivery_charge())
print("Total Bill:", home_delivery.calculate_bill())


# ============================================================
# ABSTRACTION - PROGRAM 5
# ============================================================
# Create an abstract class Patient with abstract methods calculate_bill()
# and treatment(). Derive InPatient, OutPatient, and EmergencyPatient
# classes and implement the methods according to the patient type.

from abc import ABC, abstractmethod


class Patient(ABC):

    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def treatment(self):
        pass


class InPatient(Patient):
    def calculate_bill(self):
        return 10000

    def treatment(self):
        print("In-patient treatment with hospital admission.")


class OutPatient(Patient):
    def calculate_bill(self):
        return 3000

    def treatment(self):
        print("Out-patient treatment without admission.")


class EmergencyPatient(Patient):
    def calculate_bill(self):
        return 15000

    def treatment(self):
        print("Emergency treatment provided immediately.")


patients = [
    InPatient(),
    OutPatient(),
    EmergencyPatient()
]

print("\n----- Patient Details -----")

for patient in patients:
    patient.treatment()
    print("Bill:", patient.calculate_bill())


# ============================================================
# ABSTRACTION - PROGRAM 6
# ============================================================
# Create an abstract class Transport with an abstract method
# calculate_fare(distance). Implement subclasses:
# a) Bus
# b) Train
# c) Taxi
# d) Flight
# Calculate the fare according to the transportation type.

from abc import ABC, abstractmethod


class Transport(ABC):

    @abstractmethod
    def calculate_fare(self, distance):
        pass


class Bus(Transport):
    def calculate_fare(self, distance):
        return distance * 2


class Train(Transport):
    def calculate_fare(self, distance):
        return distance * 1.5


class Taxi(Transport):
    def calculate_fare(self, distance):
        return distance * 15


class Flight(Transport):
    def calculate_fare(self, distance):
        return distance * 10


distance = 100

transports = [
    Bus(),
    Train(),
    Taxi(),
    Flight()
]

print("\n----- Transport Fares -----")

for transport in transports:
    print("Fare for", distance, "km:", transport.calculate_fare(distance))


# ============================================================
# ABSTRACTION - PROGRAM 7
# ============================================================
# Create an abstract class Question with an abstract method
# evaluate_answer(). Derive:
# a) MCQQuestion
# b) TrueFalseQuestion
# c) DescriptiveQuestion
# Implement answer evaluation for each question type.

from abc import ABC, abstractmethod


class Question(ABC):

    @abstractmethod
    def evaluate_answer(self, answer):
        pass


class MCQQuestion(Question):
    def __init__(self, correct_answer):
        self.correct_answer = correct_answer

    def evaluate_answer(self, answer):
        if answer == self.correct_answer:
            return "Correct MCQ Answer"
        else:
            return "Wrong MCQ Answer"


class TrueFalseQuestion(Question):
    def __init__(self, correct_answer):
        self.correct_answer = correct_answer

    def evaluate_answer(self, answer):
        if answer == self.correct_answer:
            return "Correct True/False Answer"
        else:
            return "Wrong True/False Answer"


class DescriptiveQuestion(Question):
    def __init__(self, correct_answer):
        self.correct_answer = correct_answer

    def evaluate_answer(self, answer):
        if answer.lower() == self.correct_answer.lower():
            return "Correct Descriptive Answer"
        else:
            return "Answer needs evaluation"


mcq = MCQQuestion("B")
true_false = TrueFalseQuestion(True)
descriptive = DescriptiveQuestion("Python")

print("\n----- Question Evaluation -----")
print(mcq.evaluate_answer("B"))
print(true_false.evaluate_answer(True))
print(descriptive.evaluate_answer("Python"))


# ============================================================
# ABSTRACTION - PROGRAM 8
# ============================================================
# Create an abstract class Authentication with an abstract method
# authenticate(). Implement the method using:
# a) Password authentication
# b) OTP authentication
# c) Biometric authentication
# Demonstrate abstraction by interacting with objects through
# the abstract interface.

from abc import ABC, abstractmethod


class Authentication(ABC):

    @abstractmethod
    def authenticate(self):
        pass


class PasswordAuthentication(Authentication):
    def authenticate(self):
        print("Authenticated using Password.")


class OTPAuthentication(Authentication):
    def authenticate(self):
        print("Authenticated using OTP.")


class BiometricAuthentication(Authentication):
    def authenticate(self):
        print("Authenticated using Biometric.")


authentications = [
    PasswordAuthentication(),
    OTPAuthentication(),
    BiometricAuthentication()
]

print("\n----- Authentication -----")

for authentication in authentications:
    authentication.authenticate()


# ============================================================
# ABSTRACTION - PROGRAM 9
# ============================================================
# Create an abstract class CloudStorage with abstract methods:
# a) upload_file()
# b) download_file()
# c) delete_file()
# Create subclasses representing different storage services
# and implement the operations.

from abc import ABC, abstractmethod


class CloudStorage(ABC):

    @abstractmethod
    def upload_file(self):
        pass

    @abstractmethod
    def download_file(self):
        pass

    @abstractmethod
    def delete_file(self):
        pass


class GoogleDrive(CloudStorage):
    def upload_file(self):
        print("File uploaded to Google Drive.")

    def download_file(self):
        print("File downloaded from Google Drive.")

    def delete_file(self):
        print("File deleted from Google Drive.")


class Dropbox(CloudStorage):
    def upload_file(self):
        print("File uploaded to Dropbox.")

    def download_file(self):
        print("File downloaded from Dropbox.")

    def delete_file(self):
        print("File deleted from Dropbox.")


storage_services = [
    GoogleDrive(),
    Dropbox()
]

print("\n----- Cloud Storage -----")

for storage in storage_services:
    storage.upload_file()
    storage.download_file()
    storage.delete_file()


# ============================================================
# ABSTRACTION - PROGRAM 10
# ============================================================
# Create an abstract class Appointment with abstract methods
# book_appointment() and calculate_fee(). Derive GeneralAppointment,
# SpecialistAppointment, and EmergencyAppointment.

from abc import ABC, abstractmethod


class Appointment(ABC):

    @abstractmethod
    def book_appointment(self):
        pass

    @abstractmethod
    def calculate_fee(self):
        pass


class GeneralAppointment(Appointment):
    def book_appointment(self):
        print("General appointment booked.")

    def calculate_fee(self):
        return 500


class SpecialistAppointment(Appointment):
    def book_appointment(self):
        print("Specialist appointment booked.")

    def calculate_fee(self):
        return 1000


class EmergencyAppointment(Appointment):
    def book_appointment(self):
        print("Emergency appointment booked.")

    def calculate_fee(self):
        return 2000


appointments = [
    GeneralAppointment(),
    SpecialistAppointment(),
    EmergencyAppointment()
]

print("\n----- Appointments -----")

for appointment in appointments:
    appointment.book_appointment()
    print("Fee:", appointment.calculate_fee())


# ============================================================
# ABSTRACTION - PROGRAM 11
# ============================================================
# Additional practice program:
# Create an abstract class Payment with an abstract method
# make_payment(). Create subclasses CashPayment, CardPayment,
# and UPIPayment and implement the payment method.

from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def make_payment(self, amount):
        pass


class CashPayment(Payment):
    def make_payment(self, amount):
        print("Cash payment of Rs.", amount, "made.")


class CardPayment(Payment):
    def make_payment(self, amount):
        print("Card payment of Rs.", amount, "made.")


class UPIPayment(Payment):
    def make_payment(self, amount):
        print("UPI payment of Rs.", amount, "made.")


payments = [
    CashPayment(),
    CardPayment(),
    UPIPayment()
]

print("\n----- Payment Methods -----")

for payment in payments:
    payment.make_payment(1500)


# ============================================================
# ABSTRACTION - PROGRAM 12
# ============================================================
# Additional practice program:
# Create an abstract class Employee with an abstract method
# calculate_salary(). Create subclasses Manager, Developer,
# and Tester and implement the salary calculation.

from abc import ABC, abstractmethod


class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass


class Manager(Employee):
    def calculate_salary(self):
        return 80000


class Developer(Employee):
    def calculate_salary(self):
        return 60000


class Tester(Employee):
    def calculate_salary(self):
        return 50000


employees = [
    Manager(),
    Developer(),
    Tester()
]

print("\n----- Employee Salaries -----")

for employee in employees:
    print("Salary:", employee.calculate_salary())
