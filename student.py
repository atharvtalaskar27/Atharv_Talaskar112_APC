# 1. Create a module student.py containing functions to calculate
# total marks, percentage, and grade. Import the module into another
# Python program and generate a student's result.

def total_marks(marks):
    return sum(marks)
def percentage(marks):
    total = total_marks(marks)
    return total / len(marks)
def grade(per):
    if per >= 90:
        return "A+"
    elif per >= 80:
        return "A"
    elif per >= 70:
        return "B"
    elif per >= 60:
        return "C"
    elif per >= 50:
        return "D"
    else:
        return "Fail"
