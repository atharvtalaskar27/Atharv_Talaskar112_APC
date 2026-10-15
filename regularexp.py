
import re

# 1. Write a Python program using regular expressions to extract all digits from a given string.
text = "My roll number is 12345 and my age is 20."
print(re.findall(r'\d', text))

# 2. Accept a sentence and display all words beginning with the letter A or a.
text = input("Enter a sentence: ")
print(re.findall(r'\b[Aa]\w*', text))

# 3. Write a program to count the occurrences of vowels in a given string using regular expressions.
text = input("Enter a string: ")
print("Vowel count:", len(re.findall(r'[aeiouAEIOU]', text)))

# 4. Write a program to extract all uppercase letters from a given string.
text = input("Enter a string: ")
print(re.findall(r'[A-Z]', text))

# 5. Write a program to identify all spaces, tabs, and newline characters in a text.
text = "Hello World\nPython\tProgramming"
print(re.findall(r'[ \t\n]', text))

# 6. Write a program to replace multiple consecutive spaces with a single space.
text = "Python    is   easy    to learn"
print(re.sub(r' +', ' ', text))

# 7. Accept a sentence and display all words containing exactly five characters.
text = input("Enter a sentence: ")
print(re.findall(r'\b\w{5}\b', text))

# 8. Write a program to identify all words ending with the letter s.
text = input("Enter a sentence: ")
print(re.findall(r'\b\w*s\b', text, re.IGNORECASE))

# 9. Write a program to remove all special characters from a given string while retaining letters, digits, and spaces.
text = input("Enter a string: ")
print(re.sub(r'[^A-Za-z0-9 ]', '', text))

# 10. Write a program to count the number of words in a sentence using regular expressions.
text = input("Enter a sentence: ")
print("Word count:", len(re.findall(r'\b\w+\b', text)))

# 11. Write a program to validate a 10-digit Indian mobile number using a regular expression.
mobile = input("Enter mobile number: ")
print("Valid" if re.fullmatch(r'[6-9]\d{9}', mobile) else "Invalid")

# 12. Accept an email address and check whether it follows a reasonable email format.
email = input("Enter email address: ")
pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
print("Valid" if re.fullmatch(pattern, email) else "Invalid")

# 13. Write a program to extract dates in DD-MM-YYYY format from a given paragraph.
text = "Date of birth is 15-08-2005 and admission date is 10-06-2025."
print(re.findall(r'\b\d{2}-\d{2}-\d{4}\b', text))

# 14. Write a program to identify web addresses beginning with http:// or https://.
text = "Visit https://example.com and http://test.org"
print(re.findall(r'https?://[^\s]+', text))

# 15. Write a program to extract all hashtags from a social media post.
text = "Learning #Python and #Programming is fun."
print(re.findall(r'(?<!\w)#[A-Za-z0-9_]+', text))

# 16. Write a program to check whether a password contains at least eight characters, one uppercase letter, one lowercase letter, one digit, and one special character.
password = input("Enter password: ")
pattern = r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}'
print("Valid password" if re.fullmatch(pattern, password) else "Invalid password")

# 17. Write a program to identify consecutive repeated words in a sentence, ignoring case differences.
text = "Python python is easy and AND useful."
print(re.findall(r'\b(\w+)\s+\1\b', text, re.IGNORECASE))

# 18. Write a program to extract six-digit Indian PIN codes from a paragraph.
text = "My PIN code is 416001 and another PIN code is 400001."
print(re.findall(r'\b[1-9]\d{5}\b', text))

# 19. Write a program to check whether an input matches a common Indian vehicle registration format, such as MH12AB1234.
vehicle = input("Enter vehicle number: ")
pattern = r'[A-Z]{2}\d{2}[A-Z]{1,2}\d{4}'
print("Valid" if re.fullmatch(pattern, vehicle.upper()) else "Invalid")

# 20. Write a program to extract file extensions from filenames in a given string.
text = "Files: report.pdf, image.jpg, program.py and notes.txt"
print(re.findall(r'\.([A-Za-z0-9]+)\b', text))

# 21. Write a program to remove HTML tags, extra whitespace, and unwanted punctuation from a text document.
text = "<p>Hello,   World!!!</p> <b>Python</b> is   easy."
text = re.sub(r'<[^>]+>', '', text)
text = re.sub(r'[^\w\s.,]', '', text)
text = re.sub(r'\s+', ' ', text).strip()
print(text)

# 22. Extract invoice numbers, dates, and monetary amounts from invoice text using regular expressions.
text = "Invoice No: INV-1234, Date: 15-08-2025, Amount: Rs. 2500.50"
print("Invoice:", re.findall(r'\bINV-\d+\b', text))
print("Date:", re.findall(r'\b\d{2}-\d{2}-\d{4}\b', text))
print("Amount:", re.findall(r'(?:Rs\.?|INR)\s*\d+(?:,\d{3})*(?:\.\d{2})?', text))

# 23. Write a program to identify single-line comments in Python source code. Discuss why regular expressions alone may not correctly handle every string literal or multiline case.
text = 'x = 10  # variable\n# This is a comment\nprint("# not a comment")'
print(re.findall(r'(?m)#.*$', text))

# 24. Validate product codes following the pattern ABC-1234-XY, where letters and digits must appear in the specified positions.
code = input("Enter product code: ")
pattern = r'[A-Z]{3}-\d{4}-[A-Z]{2}'
print("Valid" if re.fullmatch(pattern, code) else "Invalid")

# 25. Given a paragraph containing student names, roll numbers, and marks, extract each field using regular expressions.
text = "Name: Rahul, Roll: 101, Marks: 85"
pattern = r'Name:\s*([A-Za-z ]+),\s*Roll:\s*(\d+),\s*Marks:\s*(\d+)'
match = re.search(pattern, text)
if match:
    print("Name:", match.group(1))
    print("Roll Number:", match.group(2))
    print("Marks:", match.group(3))

# 26. Extract DOI identifiers, publication years, email addresses, and URLs from a collection of research paper references.
text = "Research paper DOI: 10.1234/abcd.5678, Year: 2024, Email: author@example.com, URL: https://example.com/paper"
print("DOI:", re.findall(r'\b10\.\d{4,9}/[^\s,]+', text))
print("Years:", re.findall(r'\b(?:19|20)\d{2}\b', text))
print("Emails:", re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', text))
print("URLs:", re.findall(r'https?://[^\s,]+', text))
