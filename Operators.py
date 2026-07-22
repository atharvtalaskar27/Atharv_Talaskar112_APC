Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = 10
b = 3

print("Arithmetic Operators")
print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
print("Division =", a / b)
print("Floor Division =", a // b)
print("Modulus =", a % b)
print("Exponent =", a ** b)

print("\nComparison Operators")
print("a == b =", a == b)
print("a != b =", a != b)
print("a > b =", a > b)
print("a < b =", a < b)
print("a >= b =", a >= b)
print("a <= b =", a <= b)

print("\nAssignment Operators")
x = 5
print("x =", x)

x += 2
print("x += 2 =", x)

x -= 1
print("x -= 1 =", x)

x *= 3
print("x *= 3 =", x)

x /= 2
print("x /= 2 =", x)

x //= 2
print("x //= 2 =", x)

x %= 2
print("x %= 2 =", x)

... x = 5
... x **= 2
... print("x **= 2 =", x)
... 
... print("\nLogical Operators")
... p = True
... q = False
... 
... print("p and q =", p and q)
... print("p or q =", p or q)
... print("not p =", not p)
... 
... print("\nBitwise Operators")
... m = 5
... n = 3
... 
... print("m & n =", m & n)
... print("m | n =", m | n)
... print("m ^ n =", m ^ n)
... print("~m =", ~m)
... print("m << 1 =", m << 1)
... print("m >> 1 =", m >> 1)
... 
... print("\nMembership Operators")
... list1 = [10, 20, 30, 40]
... 
... print("20 in list1 =", 20 in list1)
... print("50 in list1 =", 50 in list1)
... print("50 not in list1 =", 50 not in list1)
... 
... print("\nIdentity Operators")
... listA = [1, 2, 3]
... listB = listA
... listC = [1, 2, 3]
... 
... print("listA is listB =", listA is listB)
... print("listA is listC =", listA is listC)
... print("listA is not listC =", listA is not listC)
... 
