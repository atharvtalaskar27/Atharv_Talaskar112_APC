# 2. Create a package student containing:
# a) marks.py – total and percentage
# b) grade.py – grade calculation
# c) attendance.py – attendance eligibility
# Write a main program that uses all three modules to generate a student report.


from student.marks import total_marks, percentage
from student.grade import calculate_grade
from student.attendance import attendance_percentage, is_eligible


name = input("Enter student name: ")

marks = []

for i in range(3):
    mark = float(input("Enter marks: "))
    marks.append(mark)


present = int(input("Enter present days: "))
total_days = int(input("Enter total days: "))


total = total_marks(marks)

per = percentage(marks)

grade = calculate_grade(per)

attendance = attendance_percentage(
    present, total_days
)


print("\n----- STUDENT REPORT -----")

print("Name:", name)

print("Total Marks:", total)

print("Percentage:", per)

print("Grade:", grade)

print("Attendance:", round(attendance, 2), "%")


if is_eligible(attendance):
    print("Attendance Status: Eligible")
else:
    print("Attendance Status: Not Eligible")
