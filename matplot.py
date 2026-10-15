import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.title("Simple Line Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()


import matplotlib.pyplot as plt

subjects = ["Maths", "Science", "English", "Python","History"]
marks = [85, 90, 75, 95, 80]

plt.bar(subjects, marks, color="green")
plt.title("Student Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

import matplotlib.pyplot as plt

labels = ["Python", "Java", "C++", "JavaScript"]
sizes = [40, 25, 20, 15]

plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.title("Programming Languages")
plt.show()

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [5, 7, 4, 8, 6]

plt.scatter(x, y, color="red")
plt.title("Scatter Plot")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()

import matplotlib.pyplot as plt

marks = [45, 50, 55, 60, 60, 65, 70, 75, 80, 90]

plt.hist(marks, bins=5, color="blue", edgecolor="black")
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.title("Line Graph")
plt.subplot(1, 2, 2)
plt.bar(x, y, color="pink")
plt.title("Bar Chart")
plt.tight_layout()
plt.show()
