# ============================================================
# PROGRAM 1
# Create a dictionary containing Student ID, Student Name,
# Python Marks, DBMS Marks and Mathematics Marks for 5 students.
# Convert it into a Pandas DataFrame and:
# 1. Display the DataFrame.
# 2. Calculate total marks for each student.
# 3. Calculate average marks.
# 4. Display students who scored more than 75% average.
# ============================================================

import pandas as pd

data = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Student_Name": ["Amit", "Rahul", "Sneha", "Priya", "Rohan"],
    "Python": [80, 65, 90, 70, 85],
    "DBMS": [75, 70, 95, 68, 80],
    "Mathematics": [85, 60, 88, 72, 90]
}

df = pd.DataFrame(data)

print("Student Data:")
print(df)

df["Total"] = df["Python"] + df["DBMS"] + df["Mathematics"]
df["Average"] = df["Total"] / 3

print("\nDataFrame with Total and Average:")
print(df)

print("\nStudents with Average greater than 75:")
print(df[df["Average"] > 75])


# ============================================================
# PROGRAM 2
# Create a dictionary containing Employee ID, Employee Name,
# Department, Salary and Experience.
# Convert it into a Pandas DataFrame and:
# 1. Display employees with salary greater than ₹50,000.
# 2. Find the average salary.
# 3. Find the highest salary.
# 4. Find the employee with the highest experience.
# ============================================================

import pandas as pd

data = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Employee_Name": ["Amit", "Rahul", "Sneha", "Priya", "Rohan"],
    "Department": ["CSE", "IT", "CSE", "HR", "IT"],
    "Salary": [45000, 60000, 75000, 50000, 85000],
    "Experience": [2, 5, 7, 3, 9]
}

df = pd.DataFrame(data)

print("Employee Data:")
print(df)

print("\nEmployees with Salary greater than 50000:")
print(df[df["Salary"] > 50000])

print("\nAverage Salary:")
print(df["Salary"].mean())

print("\nHighest Salary:")
print(df["Salary"].max())

print("\nEmployee with Highest Experience:")
print(df.loc[df["Experience"].idxmax()])
# ============================================================
# PROGRAM 12
# Dataset: students.csv
# Columns:
# Student_ID, Name, Department, Python, DBMS, Maths
#
# 1. Display the first 5 records.
# 2. Display the last 5 records.
# 3. Find the total and average marks of each student.
# 4. Display students whose average marks are greater than 75.
# 5. Find the student with the highest average.
# 6. Find the average marks for each subject.
# ============================================================

import pandas as pd

# Read CSV file
df = pd.read_csv("students.csv")

# 1. Display first 5 records
print("First 5 Records:")
print(df.head())

# 2. Display last 5 records
print("\nLast 5 Records:")
print(df.tail())

# 3. Calculate total marks
df["Total"] = df["Python"] + df["DBMS"] + df["Maths"]

# Calculate average marks
df["Average"] = df["Total"] / 3

print("\nTotal and Average Marks:")
print(df)

# 4. Students with average greater than 75
print("\nStudents with Average greater than 75:")
print(df[df["Average"] > 75])

# 5. Student with highest average
print("\nStudent with Highest Average:")
print(df.loc[df["Average"].idxmax()])

# 6. Average marks for each subject
print("\nAverage Python Marks:")
print(df["Python"].mean())

print("\nAverage DBMS Marks:")
print(df["DBMS"].mean())

print("\nAverage Maths Marks:")
print(df["Maths"].mean())

# ============================================================
# PROGRAM 3
# Create a dictionary containing Product ID, Product Name,
# Category, Price and Quantity.
# Convert it into a DataFrame.
# Calculate Total Amount = Price × Quantity.
# Then find the product having the highest total sales.
# ============================================================

import pandas as pd

data = {
    "Product_ID": [1, 2, 3, 4, 5],
    "Product_Name": ["Laptop", "Mobile", "Keyboard", "Mouse", "Monitor"],
    "Category": ["Electronics", "Electronics", "Accessories", "Accessories", "Electronics"],
    "Price": [50000, 25000, 1500, 800, 12000],
    "Quantity": [2, 4, 10, 15, 5]
}

df = pd.DataFrame(data)

df["Total_Amount"] = df["Price"] * df["Quantity"]

print("Product Data:")
print(df)

print("\nProduct with Highest Total Sales:")
print(df.loc[df["Total_Amount"].idxmax()])


# ============================================================
# PROGRAM 4
# Create a dictionary containing Patient ID, Patient Name,
# Age, Disease and Medical Charges.
# Convert the dictionary into a DataFrame and:
# 1. Display patients above 60 years.
# 2. Find the average medical charge.
# 3. Find the maximum medical charge.
# 4. Display patients whose medical charges are greater than ₹50,000.
# ============================================================

import pandas as pd

data = {
    "Patient_ID": [1, 2, 3, 4, 5],
    "Patient_Name": ["Amit", "Rahul", "Sneha", "Priya", "Rohan"],
    "Age": [65, 45, 72, 30, 68],
    "Disease": ["Diabetes", "Fever", "Heart", "Cold", "Diabetes"],
    "Medical_Charges": [60000, 25000, 90000, 15000, 55000]
}

df = pd.DataFrame(data)

print("Patient Data:")
print(df)

print("\nPatients above 60 years:")
print(df[df["Age"] > 60])

print("\nAverage Medical Charge:")
print(df["Medical_Charges"].mean())

print("\nMaximum Medical Charge:")
print(df["Medical_Charges"].max())

print("\nPatients with Medical Charges greater than 50000:")
print(df[df["Medical_Charges"] > 50000])


# ============================================================
# PROGRAM 5
# Create a dictionary containing Order_ID, Customer, Product,
# Quantity, Price and Discount.
# Create a DataFrame and calculate:
# Final Amount = Quantity × Price − Discount
# Then display:
# 1. All orders
# 2. Orders above ₹5,000
# 3. Highest-value order
# 4. Average order value
# ============================================================

import pandas as pd

data = {
    "Order_ID": [101, 102, 103, 104, 105],
    "Customer": ["Amit", "Rahul", "Sneha", "Priya", "Rohan"],
    "Product": ["Laptop", "Mobile", "Tablet", "Monitor", "Laptop"],
    "Quantity": [1, 2, 1, 2, 1],
    "Price": [60000, 25000, 30000, 15000, 55000],
    "Discount": [5000, 2000, 3000, 1000, 5000]
}

df = pd.DataFrame(data)

df["Final_Amount"] = (df["Quantity"] * df["Price"]) - df["Discount"]

print("All Orders:")
print(df)

print("\nOrders above 5000:")
print(df[df["Final_Amount"] > 5000])

print("\nHighest Value Order:")
print(df.loc[df["Final_Amount"].idxmax()])

print("\nAverage Order Value:")
print(df["Final_Amount"].mean())


# ============================================================
# PROGRAM 6
# Create a dictionary containing Student_ID, Name, Department,
# Total_Classes and Classes_Attended.
# Create a DataFrame and calculate:
# Attendance Percentage = (Classes_Attended / Total_Classes) × 100
# Display students whose attendance is below 75%.
# ============================================================

import pandas as pd

data = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Name": ["Amit", "Rahul", "Sneha", "Priya", "Rohan"],
    "Department": ["CSE", "IT", "CSE", "ENTC", "CSE"],
    "Total_Classes": [100, 100, 100, 100, 100],
    "Classes_Attended": [80, 65, 90, 70, 60]
}

df = pd.DataFrame(data)

df["Attendance_Percentage"] = (
    df["Classes_Attended"] / df["Total_Classes"]
) * 100

print("Student Attendance:")
print(df)

print("\nStudents with Attendance below 75%:")
print(df[df["Attendance_Percentage"] < 75])


# ============================================================
# PROGRAM 7
# A retail shop maintains sales information in a Python
# dictionary containing Product_ID, Product_Name, Category,
# Price and Quantity.
# Write a Python program to:
# 1. Convert the dictionary into a Pandas DataFrame.
# 2. Add a new column Total_Sales.
# 3. Calculate total sales using Price × Quantity.
# 4. Display products with sales greater than ₹10,000.
# 5. Find the product with maximum sales.
# 6. Calculate the average sales.
# ============================================================

import pandas as pd

data = {
    "Product_ID": [1, 2, 3, 4, 5],
    "Product_Name": ["Laptop", "Mobile", "Keyboard", "Monitor", "Printer"],
    "Category": ["Electronics", "Electronics", "Accessories", "Electronics", "Electronics"],
    "Price": [50000, 25000, 1500, 12000, 15000],
    "Quantity": [2, 3, 10, 2, 4]
}

df = pd.DataFrame(data)

df["Total_Sales"] = df["Price"] * df["Quantity"]

print("Product Data:")
print(df)

print("\nProducts with Sales greater than 10000:")
print(df[df["Total_Sales"] > 10000])

print("\nProduct with Maximum Sales:")
print(df.loc[df["Total_Sales"].idxmax()])

print("\nAverage Sales:")
print(df["Total_Sales"].mean())


# ============================================================
# PROGRAM 8
# Create a Pandas Series using a dictionary where the student
# names are keys and their marks are values.
# Perform:
# 1. Display the Series.
# 2. Display marks of a particular student.
# 3. Find maximum and minimum marks.
# 4. Calculate average marks.
# 5. Display students who scored more than 75.
# ============================================================

import pandas as pd

data = {
    "Amit": 80,
    "Rahul": 65,
    "Sneha": 90,
    "Priya": 72,
    "Rohan": 85
}

s = pd.Series(data)

print("Student Marks:")
print(s)

print("\nMarks of Amit:")
print(s["Amit"])

print("\nMaximum Marks:")
print(s.max())

print("\nMinimum Marks:")
print(s.min())

print("\nAverage Marks:")
print(s.mean())

print("\nStudents who scored more than 75:")
print(s[s > 75])


# ============================================================
# PROGRAM 9
# Create a Pandas Series using a dictionary containing employee
# names and their salaries.
# Perform:
# 1. Display the Series.
# 2. Find the highest salary.
# 3. Find the lowest salary.
# 4. Calculate average salary.
# 5. Display employees earning more than ₹50,000.
# ============================================================

import pandas as pd

data = {
    "Amit": 45000,
    "Rahul": 60000,
    "Sneha": 75000,
    "Priya": 50000,
    "Rohan": 85000
}

s = pd.Series(data)

print("Employee Salaries:")
print(s)

print("\nHighest Salary:")
print(s.max())

print("\nLowest Salary:")
print(s.min())

print("\nAverage Salary:")
print(s.mean())

print("\nEmployees earning more than 50000:")
print(s[s > 50000])


# ============================================================
# PROGRAM 10
# Create a Pandas Series using a dictionary containing product
# names and prices.
# Perform:
# 1. Display all products and prices.
# 2. Increase every price by 10%.
# 3. Find the most expensive product.
# 4. Find products costing more than ₹1,000.
# ============================================================

import pandas as pd

data = {
    "Laptop": 50000,
    "Mobile": 25000,
    "Keyboard": 1500,
    "Mouse": 800,
    "Monitor": 12000
}

s = pd.Series(data)

print("Products and Prices:")
print(s)

s = s * 1.10

print("\nPrices after 10% increase:")
print(s)

print("\nMost Expensive Product:")
print(s.idxmax())
print("Price:", s.max())

print("\nProducts costing more than 1000:")
print(s[s > 1000])


# ============================================================
# PROGRAM 11
# Create a Pandas Series using a dictionary where patient IDs
# are the index and patient ages are the values.
# Perform:
# 1. Find the average age.
# 2. Find the oldest patient.
# 3. Find the youngest patient.
# 4. Display patients above 60 years.
# ============================================================

import pandas as pd

data = {
    101: 45,
    102: 65,
    103: 72,
    104: 30,
    105: 68
}

s = pd.Series(data)

print("Patient Ages:")
print(s)

print("\nAverage Age:")
print(s.mean())

print("\nOldest Patient:")
print(s.idxmax(), "Age:", s.max())

print("\nYoungest Patient:")
print(s.idxmin(), "Age:", s.min())

print("\nPatients above 60 years:")
print(s[s > 60])

# ============================================================
# PROGRAM 12
# Dataset: students.csv
# Columns:
# Student_ID, Name, Department, Python, DBMS, Maths
#
# 1. Display the first 5 records.
# 2. Display the last 5 records.
# 3. Find the total and average marks of each student.
# 4. Display students whose average marks are greater than 75.
# 5. Find the student with the highest average.
# 6. Find the average marks for each subject.
# ============================================================

import pandas as pd

# Read CSV file
df = pd.read_csv("students.csv")

# 1. Display first 5 records
print("First 5 Records:")
print(df.head())

# 2. Display last 5 records
print("\nLast 5 Records:")
print(df.tail())

# 3. Calculate total marks
df["Total"] = df["Python"] + df["DBMS"] + df["Maths"]

# Calculate average marks
df["Average"] = df["Total"] / 3

print("\nTotal and Average Marks:")
print(df)

# 4. Students with average greater than 75
print("\nStudents with Average greater than 75:")
print(df[df["Average"] > 75])

# 5. Student with highest average
print("\nStudent with Highest Average:")
print(df.loc[df["Average"].idxmax()])

# 6. Average marks for each subject
print("\nAverage Python Marks:")
print(df["Python"].mean())

print("\nAverage DBMS Marks:")
print(df["DBMS"].mean())

print("\nAverage Maths Marks:")
print(df["Maths"].mean())

# ============================================================
# PROGRAM 13
# Dataset: employees.csv
# Columns:
# Employee_ID, Name, Department, Experience, Salary
#
# 1. Display employees from the CSE department.
# 2. Find the average salary.
# 3. Find the highest and lowest salary.
# 4. Display employees having salary greater than ₹50,000.
# 5. Calculate department-wise average salary.
# ============================================================

import pandas as pd

# Read CSV file
df = pd.read_csv("employees.csv")

# 1. Employees from CSE department
print("Employees from CSE Department:")
print(df[df["Department"] == "CSE"])

# 2. Average salary
print("\nAverage Salary:")
print(df["Salary"].mean())

# 3. Highest salary
print("\nHighest Salary:")
print(df["Salary"].max())

# Lowest salary
print("\nLowest Salary:")
print(df["Salary"].min())

# 4. Employees with salary greater than 50000
print("\nEmployees with Salary greater than 50000:")
print(df[df["Salary"] > 50000])

# 5. Department-wise average salary
print("\nDepartment-wise Average Salary:")
print(df.groupby("Department")["Salary"].mean())
# ============================================================
# PROGRAM 14
# Dataset: patients.csv
# Columns:
# Patient_ID, Name, Age, Gender, Disease, Medical_Expense
#
# 1. Display patients above 60 years.
# 2. Calculate average medical expense.
# 3. Find the patient with the highest medical expense.
# 4. Count patients for each disease.
# 5. Display patients whose medical expense exceeds ₹50,000.
# ============================================================

import pandas as pd

# Read CSV file
df = pd.read_csv("patients.csv")

# 1. Patients above 60 years
print("Patients above 60 years:")
print(df[df["Age"] > 60])

# 2. Average medical expense
print("\nAverage Medical Expense:")
print(df["Medical_Expense"].mean())

# 3. Patient with highest medical expense
print("\nPatient with Highest Medical Expense:")
print(df.loc[df["Medical_Expense"].idxmax()])

# 4. Count patients for each disease
print("\nNumber of Patients for Each Disease:")
print(df["Disease"].value_counts())

# 5. Patients with medical expense greater than 50000
print("\nPatients with Medical Expense greater than 50000:")
print(df[df["Medical_Expense"] > 50000])

# ============================================================
# PROGRAM 15
# Dataset: weather.csv
# Columns:
# Date, City, Temperature, Humidity, Rainfall
#
# 1. Find the maximum temperature.
# 2. Find the minimum temperature.
# 3. Calculate the average temperature.
# 4. Display records where temperature is above 35°C.
# 5. Calculate city-wise average temperature.
# ============================================================

import pandas as pd

# Read CSV file
df = pd.read_csv("weather.csv")

# 1. Maximum temperature
print("Maximum Temperature:")
print(df["Temperature"].max())

# 2. Minimum temperature
print("\nMinimum Temperature:")
print(df["Temperature"].min())

# 3. Average temperature
print("\nAverage Temperature:")
print(df["Temperature"].mean())

# 4. Records where temperature is above 35
print("\nRecords with Temperature above 35:")
print(df[df["Temperature"] > 35])

# 5. City-wise average temperature
print("\nCity-wise Average Temperature:")
print(df.groupby("City")["Temperature"].mean())
