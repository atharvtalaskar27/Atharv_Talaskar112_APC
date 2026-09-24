# ============================================================
# 1. Write a Python program using NumPy to create a one-dimensional
# array containing 10 integers and display the array, its size,
# data type, and number of dimensions.
# ============================================================

import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print("Array:", arr)
print("Size:", arr.size)
print("Data Type:", arr.dtype)
print("Number of Dimensions:", arr.ndim)


# ============================================================
# 2. Create two NumPy arrays of 5 integers each. Perform and display:
# Addition
# Subtraction
# Multiplication
# Division
# Modulus
# ============================================================

import numpy as np

arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([2, 4, 5, 8, 10])

print("Array 1:", arr1)
print("Array 2:", arr2)

print("Addition:", arr1 + arr2)
print("Subtraction:", arr1 - arr2)
print("Multiplication:", arr1 * arr2)
print("Division:", arr1 / arr2)
print("Modulus:", arr1 % arr2)


# ============================================================
# 3. Create a NumPy array containing 10 numbers. Find and display
# the maximum, minimum, sum, and average of the elements.
# ============================================================

import numpy as np

arr = np.array([10, 25, 15, 40, 35, 50, 20, 45, 30, 60])

print("Array:", arr)
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Sum:", np.sum(arr))
print("Average:", np.mean(arr))


# ============================================================
# 4. Create a NumPy array of integers from 1 to 20. Use Boolean
# indexing to separate and display the even and odd numbers.
# ============================================================

import numpy as np

arr = np.arange(1, 21)

even = arr[arr % 2 == 0]
odd = arr[arr % 2 != 0]

print("Array:", arr)
print("Even Numbers:", even)
print("Odd Numbers:", odd)


# ============================================================
# 5. Create a one-dimensional array containing numbers from 1 to 12.
# Reshape it into:
# 2 × 6 matrix
# 3 × 4 matrix
# 4 × 3 matrix
# ============================================================

import numpy as np

arr = np.arange(1, 13)

print("Original Array:")
print(arr)

matrix_2x6 = arr.reshape(2, 6)
matrix_3x4 = arr.reshape(3, 4)
matrix_4x3 = arr.reshape(4, 3)

print("\n2 × 6 Matrix:")
print(matrix_2x6)

print("\n3 × 4 Matrix:")
print(matrix_3x4)

print("\n4 × 3 Matrix:")
print(matrix_4x3)


# ============================================================
# 6. Create two 3 × 3 NumPy matrices and perform matrix addition.
# ============================================================

import numpy as np

matrix1 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

matrix2 = np.array([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])

result = matrix1 + matrix2

print("Matrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

print("\nMatrix Addition:")
print(result)


# ============================================================
# 7. Create two compatible matrices using NumPy and perform
# matrix multiplication using an appropriate NumPy function.
# ============================================================

import numpy as np

matrix1 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

matrix2 = np.array([
    [7, 8],
    [9, 10],
    [11, 12]
])

result = np.matmul(matrix1, matrix2)

print("Matrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

print("\nMatrix Multiplication:")
print(result)


# ============================================================
# 8. Create a 3 × 4 matrix and display its transpose.
# ============================================================

import numpy as np

matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

print("Original Matrix:")
print(matrix)

print("\nTranspose:")
print(matrix.T)


# ============================================================
# 9. Create a 4 × 4 NumPy array and write a program to:
# Display the first row
# Display the last column
# Display the diagonal elements
# Display the elements from the second and third rows
# ============================================================

import numpy as np

arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

print("4 × 4 Array:")
print(arr)

print("\nFirst Row:")
print(arr[0])

print("\nLast Column:")
print(arr[:, -1])

print("\nDiagonal Elements:")
print(np.diag(arr))

print("\nSecond and Third Rows:")
print(arr[1:3])


# ============================================================
# 10. Create a 4 × 4 matrix and calculate the sum of each row
# and each column separately.
# ============================================================

import numpy as np

matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

print("Matrix:")
print(matrix)

row_sum = np.sum(matrix, axis=1)
column_sum = np.sum(matrix, axis=0)

print("\nSum of Each Row:")
print(row_sum)

print("\nSum of Each Column:")
print(column_sum)

# ============================================================
# 11. Create a NumPy array containing numbers from 1 to 20.
# Using slicing, display:
# First 5 elements
# Last 5 elements
# Alternate elements
# Elements in reverse order
# ============================================================

import numpy as np

arr = np.arange(1, 21)

print("Array:", arr)

print("\nFirst 5 Elements:")
print(arr[:5])

print("\nLast 5 Elements:")
print(arr[-5:])

print("\nAlternate Elements:")
print(arr[::2])

print("\nElements in Reverse Order:")
print(arr[::-1])


# ============================================================
# 12. Create an array of 10 integers. Replace all elements
# greater than 50 with 0 using NumPy Boolean indexing.
# ============================================================

import numpy as np

arr = np.array([25, 60, 45, 80, 30, 90, 55, 40, 75, 20])

print("Original Array:")
print(arr)

arr[arr > 50] = 0

print("\nArray after replacing elements greater than 50 with 0:")
print(arr)


# ============================================================
# 13. Create an unsorted NumPy array and display it in:
# Ascending order
# Descending order
# ============================================================

import numpy as np

arr = np.array([45, 12, 89, 23, 67, 5, 34, 90])

print("Original Array:")
print(arr)

ascending = np.sort(arr)
descending = np.sort(arr)[::-1]

print("\nAscending Order:")
print(ascending)

print("\nDescending Order:")
print(descending)


# ============================================================
# 14. Create an array containing duplicate values.
# Find and display only the unique elements.
# ============================================================

import numpy as np

arr = np.array([10, 20, 10, 30, 40, 20, 50, 30, 60, 40])

print("Original Array:")
print(arr)

unique_elements = np.unique(arr)

print("\nUnique Elements:")
print(unique_elements)


# ============================================================
# 15. Create two NumPy arrays and concatenate them
# horizontally and vertically.
# ============================================================

import numpy as np

arr1 = np.array([
    [1, 2],
    [3, 4]
])

arr2 = np.array([
    [5, 6],
    [7, 8]
])

print("Array 1:")
print(arr1)

print("\nArray 2:")
print(arr2)

horizontal = np.hstack((arr1, arr2))
vertical = np.vstack((arr1, arr2))

print("\nHorizontal Concatenation:")
print(horizontal)

print("\nVertical Concatenation:")
print(vertical)


# ============================================================
# 16. Store marks of 10 students in a NumPy array.
# Calculate:
# Highest marks
# Lowest marks
# Average marks
# Median
# Standard deviation
# ============================================================

import numpy as np

marks = np.array([75, 82, 68, 90, 55, 88, 72, 95, 64, 80])

print("Marks:", marks)

print("\nHighest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))
print("Average Marks:", np.mean(marks))
print("Median:", np.median(marks))
print("Standard Deviation:", np.std(marks))


# ============================================================
# 17. Take marks of 20 students, calculate the class average
# and display the marks of students who scored above the average.
# ============================================================

import numpy as np

marks = np.array([
    65, 78, 82, 55, 90,
    72, 88, 45, 69, 95,
    76, 84, 60, 92, 70,
    81, 58, 87, 73, 66
])

average = np.mean(marks)

above_average = marks[marks > average]

print("Marks of 20 Students:")
print(marks)

print("\nClass Average:", average)

print("\nMarks Above Class Average:")
print(above_average)


# ============================================================
# 18. Write a Python program using NumPy to create a 3D array
# of shape (2, 3, 4) containing numbers from 1 to 24.
# Display the array and its:
# Number of dimensions
# Shape
# Size
# ============================================================

import numpy as np

arr = np.arange(1, 25).reshape(2, 3, 4)

print("3D Array:")
print(arr)

print("\nNumber of Dimensions:", arr.ndim)
print("Shape:", arr.shape)
print("Size:", arr.size)


# ============================================================
# 19. Create a 3D array of shape (2, 3, 4) and write a program
# to access:
# First element
# Last element
# Element at index [0,1,2]
# Element at index [1,2,3]
# ============================================================

import numpy as np

arr = np.arange(1, 25).reshape(2, 3, 4)

print("3D Array:")
print(arr)

print("\nFirst Element:")
print(arr[0, 0, 0])

print("\nLast Element:")
print(arr[-1, -1, -1])

print("\nElement at index [0,1,2]:")
print(arr[0, 1, 2])

print("\nElement at index [1,2,3]:")
print(arr[1, 2, 3])


# ============================================================
# 20. Create a (2, 3, 4) array and calculate:
# Sum of all elements
# Sum of each layer
# Sum along rows
# Sum along columns
# ============================================================

import numpy as np

arr = np.arange(1, 25).reshape(2, 3, 4)

print("3D Array:")
print(arr)

print("\nSum of All Elements:")
print(np.sum(arr))

print("\nSum of Each Layer:")
print(np.sum(arr, axis=(1, 2)))

print("\nSum Along Rows:")
print(np.sum(arr, axis=2))

print("\nSum Along Columns:")
print(np.sum(arr, axis=1))


# ============================================================
# 21. Create a 3D array of random integers between 1 and 100.
# Replace all values greater than 50 with 0
# ============================================================

import numpy as np

arr = np.random.randint(1, 101, size=(2, 3, 4))

print("Original 3D Array:")
print(arr)

arr[arr > 50] = 0

print("\nArray after replacing values greater than 50 with 0:")
print(arr)


# ============================================================
# 22. Generate a random 3D array of shape (3, 4, 5)
# and calculate its:
# mean, median, standard deviation, variance,
# minimum, and maximum.
# ============================================================

import numpy as np

arr = np.random.randint(1, 101, size=(3, 4, 5))

print("Random 3D Array:")
print(arr)

print("\nMean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))
print("Variance:", np.var(arr))
print("Minimum:", np.min(arr))
print("Maximum:", np.max(arr))


# ============================================================
# 23. Create a 3D NumPy array of shape (2, 3, 4)
# containing numbers from 1 to 24. Flatten the array into
# a one-dimensional array and display both the original
# and flattened arrays.
# ============================================================

import numpy as np

arr = np.arange(1, 25).reshape(2, 3, 4)

flattened = arr.flatten()

print("Original 3D Array:")
print(arr)

print("\nFlattened One-Dimensional Array:")
print(flattened)


# ============================================================
# 24. Create a 3D array containing integers from 1 to 27.
# Flatten the array and calculate:
# Sum
# Average
# Maximum
# Minimum
# ============================================================

import numpy as np

arr = np.arange(1, 28).reshape(3, 3, 3)

flattened = arr.flatten()

print("Original 3D Array:")
print(arr)

print("\nFlattened Array:")
print(flattened)

print("\nSum:", np.sum(flattened))
print("Average:", np.mean(flattened))
print("Maximum:", np.max(flattened))
print("Minimum:", np.min(flattened))


# ============================================================
# 25. Create a random 3D NumPy array of shape (3, 4, 5).
# Flatten it and display only the elements that are:
# Greater than 50
# Even numbers
# Less than the average value
# ============================================================

import numpy as np

arr = np.random.randint(1, 101, size=(3, 4, 5))

flattened = arr.flatten()

average = np.mean(flattened)

greater_than_50 = flattened[flattened > 50]
even_numbers = flattened[flattened % 2 == 0]
less_than_average = flattened[flattened < average]

print("Original 3D Array:")
print(arr)

print("\nFlattened Array:")
print(flattened)

print("\nElements Greater Than 50:")
print(greater_than_50)

print("\nEven Numbers:")
print(even_numbers)

print("\nAverage:", average)

print("\nElements Less Than Average:")
print(less_than_average)


    

































