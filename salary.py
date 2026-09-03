# 5. Create a module containing functions to calculate gross salary,
# deductions, and net salary for an employee.
def gross_salary(basic, allowance):
    return basic + allowance
def deductions(gross, deduction_percent):
    return gross * deduction_percent / 100
def net_salary(gross, deduction):
    return gross - deduction
