# 1. Write a PYTHON program to input a string and display its length without using len() function.

s = input("Enter a string: ")

count = 0

for i in s:
    count = count + 1

print("Length =", count)


# 2. Write a PYTHON program to count vowels, consonants, digits, spaces and special characters.

s = input("Enter a string: ")

vowels = 0
consonants = 0
digits = 0
spaces = 0
special = 0

for ch in s:
    if ch in "AEIOUaeiou":
        vowels = vowels + 1
    elif ch.isalpha():
        consonants = consonants + 1
    elif ch.isdigit():
        digits = digits + 1
    elif ch == " ":
        spaces = spaces + 1
    else:
        special = special + 1

print("Vowels =", vowels)
print("Consonants =", consonants)
print("Digits =", digits)
print("Spaces =", spaces)
print("Special Characters =", special)


# 3. Write a PYTHON program to reverse a string.

s = input("Enter a string: ")

rev = ""

for ch in s:
    rev = ch + rev

print("Reversed String =", rev)


# 4. Write a PYTHON program to check whether the entered string is palindrome or not.

s = input("Enter a string: ")

rev = ""

for ch in s:
    rev = ch + rev

if s == rev:
    print("Palindrome")
else:
    print("Not Palindrome")


# 5. Write a PYTHON program to count uppercase and lowercase letters.

s = input("Enter a string: ")

upper = 0
lower = 0

for ch in s:
    if ch.isupper():
        upper = upper + 1
    elif ch.islower():
        lower = lower + 1

print("Uppercase Letters =", upper)
print("Lowercase Letters =", lower)


# 6. Write a PYTHON program to replace all occurrences of a character with another character.

s = input("Enter a string: ")

old = input("Enter character to replace: ")
new = input("Enter new character: ")

result = ""

for ch in s:
    if ch == old:
        result = result + new
    else:
        result = result + ch

print("New String =", result)


# 7. Write a PYTHON program to remove all spaces from the input string.

s = input("Enter a string: ")

result = ""

for ch in s:
    if ch != " ":
        result = result + ch

print("String without spaces =", result)


# 8. Write a PYTHON program to find the frequency of a character.

s = input("Enter a string: ")

ch = input("Enter character to search: ")

count = 0

for i in s:
    if i == ch:
        count = count + 1

print("Frequency =", count)


# 9. Write a PYTHON program to print the first and last character of a string.

s = input("Enter a string: ")

print("First Character =", s[0])
print("Last Character =", s[-1])


# 10. Write a PYTHON program to display each character along with its ASCII value.

s = input("Enter a string: ")

for ch in s:
    print(ch, "=", ord(ch))
# 11. Write a PYTHON program to count the total number of words in a sentence.

s = input("Enter a sentence: ")

words = s.split()

print("Total words =", len(words))


# 12. Write a PYTHON program to find the longest word in a sentence.

s = input("Enter a sentence: ")

words = s.split()

longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word =", longest)


# 13. Write a PYTHON program to find the shortest word in a sentence.

s = input("Enter a sentence: ")

words = s.split()

shortest = words[0]

for word in words:
    if len(word) < len(shortest):
        shortest = word

print("Shortest word =", shortest)


# 14. Write a PYTHON program to convert the first letter of every word to uppercase.

s = input("Enter a sentence: ")

print("Title Case =", s.title())


# 15. Write a PYTHON program to print all duplicate characters in a string.

s = input("Enter a string: ")

printed = ""

for ch in s:
    if s.count(ch) > 1 and ch not in printed:
        print(ch)
        printed = printed + ch


# 16. Write a PYTHON program to display the frequency of every character in a string.

s = input("Enter a string: ")

printed = ""

for ch in s:
    if ch not in printed:
        print(ch, "=", s.count(ch))
        printed = printed + ch


# 17. Write a PYTHON program to check whether two strings are anagrams.

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")


# 18. Write a PYTHON program to remove duplicate characters while maintaining original order.

s = input("Enter a string: ")

result = ""

for ch in s:
    if ch not in result:
        result = result + ch

print("String after removing duplicates =", result)


# 19. Write a PYTHON program to check whether a given substring exists in the main string.

s = input("Enter the main string: ")

sub = input("Enter the substring: ")

if sub in s:
    print("Substring Found")
else:
    print("Substring Not Found")


# 20. Write a PYTHON program to count how many times a specific word appears in a sentence.

s = input("Enter a sentence: ")

word = input("Enter the word to search: ")

words = s.split()

count = 0

for w in words:
    if w == word:
        count = count + 1

print("Occurrences =", count)
# 21. Write a PYTHON program to validate a password.

password = input("Enter Password: ")

upper = False
lower = False
digit = False
special = False

for ch in password:
    if ch.isupper():
        upper = True
    elif ch.islower():
        lower = True
    elif ch.isdigit():
        digit = True
    else:
        special = True

if len(password) >= 8 and upper and lower and digit and special:
    print("Valid Password")
else:
    print("Invalid Password")


# 22. Write a PYTHON program for Run-Length Encoding.

s = input("Enter a string: ")

result = ""
count = 1

for i in range(len(s)):
    if i < len(s) - 1 and s[i] == s[i + 1]:
        count = count + 1
    else:
        result = result + s[i] + str(count)
        count = 1

print("Encoded String =", result)


# 23. Write a PYTHON program for String Compression.

s = input("Enter a string: ")

result = ""
count = 1

for i in range(len(s)):
    if i < len(s) - 1 and s[i] == s[i + 1]:
        count = count + 1
    else:
        result = result + s[i] + str(count)
        count = 1

if len(result) < len(s):
    print("Compressed String =", result)
else:
    print("Original String =", s)


# 24. Write a PYTHON program to find the most frequent character.

s = input("Enter a string: ")

max_char = ""
max_count = 0

for ch in s:
    if s.count(ch) > max_count:
        max_count = s.count(ch)
        max_char = ch

print("Most Frequent Character =", max_char)


# 25. Write a PYTHON program to find the second most frequent character.

s = input("Enter a string: ")

freq = {}

for ch in s:
    freq[ch] = s.count(ch)

sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

if len(sorted_freq) > 1:
    print("Second Most Frequent Character =", sorted_freq[1][0])
else:
    print("Not Available")


# 26. Write a PYTHON program for Caesar Cipher.

text = input("Enter Text: ")
shift = int(input("Enter Shift Value: "))

result = ""

for ch in text:
    if ch.isalpha():
        if ch.isupper():
            result = result + chr((ord(ch) - 65 + shift) % 26 + 65)
        else:
            result = result + chr((ord(ch) - 97 + shift) % 26 + 97)
    else:
        result = result + ch

print("Encrypted Text =", result)


# 27. Write a PYTHON program to validate an email.

email = input("Enter Email: ")

if "@" in email and "." in email:
    print("Valid Email")
else:
    print("Invalid Email")


# 28. Write a PYTHON program to count the frequency of every word.

s = input("Enter a sentence: ")

words = s.split()

printed = []

for word in words:
    if word not in printed:
        print(word, "=", words.count(word))
        printed.append(word)


# 29. Write a PYTHON program to reverse the order of words in a sentence.

s = input("Enter a sentence: ")

words = s.split()

for i in range(len(words) - 1, -1, -1):
    print(words[i], end=" ")


# 30. Write a PYTHON program to check whether one string is rotation of another.

s1 = input("\nEnter First String: ")
s2 = input("Enter Second String: ")

if len(s1) == len(s2) and s2 in (s1 + s1):
    print("Yes, Rotation")
else:
    print("No, Not Rotation")
