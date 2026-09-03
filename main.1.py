# Main program to generate student result
import student
name = input("Enter student name: ")
marks = []
for i in range(3):
    mark = float(input("Enter marks: "))
    marks.append(mark)

total = student.total_marks(marks)
per = student.percentage(marks)
gr = student.grade(per)
print("\n----- STUDENT RESULT -----")
print("Name:", name)
print("Total Marks:", total)
print("Percentage:", per)
print("Grade:", gr)
