# Main program for salary module

import salary

name = input("Enter employee name: ")

basic = float(input("Enter basic salary: "))

allowance = float(input("Enter allowance: "))

deduction_percent = float(
    input("Enter deduction percentage: ")
)

gross = salary.gross_salary(basic, allowance)

deduction = salary.deductions(
    gross, deduction_percent
)

net = salary.net_salary(
    gross, deduction
)

print("\n----- EMPLOYEE SALARY -----")

print("Employee Name:", name)

print("Gross Salary:", gross)

print("Deduction:", deduction)

print("Net Salary:", net)
