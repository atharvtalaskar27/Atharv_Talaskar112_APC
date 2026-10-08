1
import numpy as np
num1=np.array([[1,2],[4,5]])
num2=np.array([[6,7],[9,10]])

c=np.dot(num1,num2)
print(c)

 2
num=[5,3,45,2,10]
for i in range(len(num)):
    for j in range(len(num)-1-i):
        if num[j]>num[j+1]:
            num[j],num[j+1]=num[j+1],num[j]
print("sorted list:",num)



3
word=input("enter word to search:")
with open("sample.txt","r") as file1:
    text=file1.read()
    frequency=text.lower().split().count(word.lower())
    print(frequency)




