#1.	Write a Python program to create a file named student.txt and write the student's name, roll number, branch, and semester into the file.
with open("student.txt","w") as file:
    name=input("enter student name:")
    roll_number=input("enter student roll number:")
    branch=input("enter student branch:")
    semester=input("enter student semester:")
file.write("Name:{name}\n Roll number:{roll_number}\n Branch:{branch}\n Semester:{semester}")

file.close()

#2. Write a program to open a text file and display its complete contents.

filename = input("Enter filename to read: ")
try:
    with open(filename, "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found!")
file.close()

#3. Write a program to append additional student information to an
 #existing file without deleting its previous contents.

# Append student details

file = open("student.txt", "a")

name = input("Enter name: ")
roll = input("Enter roll number: ")
branch = input("Enter branch: ")
semester = input("Enter semester: ")

file.write("\nName: " + name + "\n")
file.write("Roll No: " + roll + "\n")
file.write("Branch: " + branch + "\n")
file.write("Semester: " + semester + "\n")

file.close()

print("Details appended successfully.")

# 4. Write a program to read a text file line by line and display each
#    line separately.
filename = input("Enter filename to read line by line: ")
try:
    with open(filename, "r") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("File not found!")

# 5. Write a program to count and display the total number of lines
#    present in a text file.
filename = input("Enter filename to count lines: ")
try:
    with open(filename, "r") as file:
        line_count = len(file.readlines())
        print(f"Total lines: {line_count}")
except FileNotFoundError:
    print("File not found!")

# 6. Write a program to count the total number of words present in a text file.
# ----------------------------------------------------------------------
filename = input("Enter filename to count words: ")
try:
    with open(filename, "r") as file:
        words = file.read().split()
        print(f"Total words: {len(words)}")
except FileNotFoundError:
    print("File not found!")

# 7. Write a program to count the total number of characters in a text
#    file, including spaces.

filename = input("Enter filename to count characters: ")
try:
    with open(filename, "r") as file:
        content = file.read()
        print(f"Total characters: {len(content)}")
except FileNotFoundError:
    print("File not found!")

 #8.Write a program to read a text file and display its lines in reverse order.
filename = input("Enter filename to display lines in reverse: ")
try:
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in reversed(lines):
            print(line.strip())
except FileNotFoundError:
    print("File not found!")

# 9. Read a text file and count the number of vowels and consonants present
#    in the file.
# ----------------------------------------------------------------------
filename = input("Enter filename to count vowels and consonants: ")
try:
    with open(filename, "r") as file:
        text = file.read().lower()
        vowels = "aeiou"
        v_count = 0
        c_count = 0
        for char in text:
            if char.isalpha():
                if char in vowels:
                    v_count += 1
                else:
                    c_count += 1
        print(f"Vowels: {v_count}, Consonants: {c_count}")
except FileNotFoundError:
    print("File not found!")


#13.Read textfile and find the longest word present in the file.
# ----------------------------------------------------------------------
filename = input("Enter filename to find longest word: ")
try:
    with open(filename, "r") as file:
        words = file.read().split()
        if words:
            longest = max(words, key=len)
            print(f"Longest word: {longest}")
        else:
            print("File is empty.")
except FileNotFoundError:
    print("File not found!")


# 12. Read a text file and count how many times each word occurs. Display
#     the result using a dictionary.
# ----------------------------------------------------------------------
filename = input("Enter filename: ")
try:
    with open(filename, "r") as file:
        words = file.read().lower().split()
        freq = {}
        for w in words:
            w = w.strip(".,!?;:\"'()[]{}")
            if w:
                freq[w] = freq.get(w, 0) + 1
        print("Word Frequency:", freq)
except FileNotFoundError:
    print("File not found!")


# 13 Read a text file and replace all occurrences of a specified word with
#     another word. Save the modified text in the same file or a new file.
# ----------------------------------------------------------------------
src_file = input("Enter source filename: ")
old_word = input("Enter word to replace: ")
new_word = input("Enter replacement word: ")
out_file = input("Enter output filename (or same name to overwrite): ")

try:
    with open(src_file, "r") as file:
        content = file.read()
    modified_content = content.replace(old_word, new_word)
    with open(out_file, "w") as file:
        file.write(modified_content)
    print("Replacement complete.")
except FileNotFoundError:
    print("File not found!")

 # 14. Read a text file and replace all occurrences of a specified word with
#     another word. Save the modified text in the same file or a new file.
src_file = input("Enter source filename: ")
old_word = input("Enter word to replace: ")
new_word = input("Enter replacement word: ")
out_file = input("Enter output filename (or same name to overwrite): ")

try:
    with open(src_file, "r") as file:
        content = file.read()
    modified_content = content.replace(old_word, new_word)
    with open(out_file, "w") as file:
        file.write(modified_content)
    print("Replacement complete.")
except FileNotFoundError:
    print("File not found!")
#15.	Read a Python source file and create another file after removing single-line comments
src_py = input("Enter source Python filename (.py): ")
dest_py = input("Enter destination filename: ")
try:
    with open(src_py, "r") as infile, open(dest_py, "w") as outfile:
        for line in infile:
            if "#" in line:
                line = line.split("#")[0] + "\n"
            if line.strip():
                outfile.write(line)
    print("Comments removed successfully.")
except FileNotFoundError:
    print("Source file not found!")

# 16. Read a text file and create another file containing the same text
#     in uppercase.
src_file = input("Enter source filename: ")
dest_file = input("Enter destination filename: ")
try:
    with open(src_file, "r") as infile, open(dest_file, "w") as outfile:
        outfile.write(infile.read().upper())
    print("Content converted to uppercase successfully.")
except FileNotFoundError:
    print("File not found!")

17. Create a file containing student records in the format:
#     RollNo,Name,Marks
#     101,Amit,85
#     102,Priya,92
#     103,Rahul,78
#     Write a program to:
#     • Display all records.
#     • Find the student with the highest marks.
#     • Calculate average marks.
#     • Display students who scored more than 80.
# ----------------------------------------------------------------------
filename = "records.csv"
with open(filename, "w") as f:
    f.write("RollNo,Name,Marks\n101,Amit,85\n102,Priya,92\n103,Rahul,78\n")

records = []
with open(filename, "r") as f:
    next(f)  
    for line in f:
        r, n, m = line.strip().split(",")
        records.append((r, n, float(m)))

print("--- All Records ---")
for r, n, m in records:
    print(f"Roll: {r}, Name: {n}, Marks: {m}")

highest = max(records, key=lambda x: x[2])
print(f"\nHighest Marks: {highest[1]} ({highest[2]})")

avg_marks = sum(r[2] for r in records) / len(records)
print(f"Average Marks: {avg_marks:.2f}")

print("\nStudents scoring > 80:")
for r, n, m in records:
    if m > 80:
        print(f"{n} ({m})") 


# 19. Store student attendance records in a file. Calculate the attendance
#     percentage and display students having attendance below 75%.
# ----------------------------------------------------------------------
att_file = "attendance.txt"
with open(att_file, "w") as f:
    f.write(
        "RollNo,Name,TotalClasses,AttendedClasses\n1,Amit,50,40\n2,Priya,50,30\n3,Rahul,50,45\n"
    )

print("Students with attendance < 75%:")
with open(att_file, "r") as f:
    next(f)
    for line in f:
        r, name, total, attended = line.strip().split(",")
        pct = (int(attended) / int(total)) * 100
        print(f"{name}: {pct:.2f}%")
        if pct < 75:
            print(f"  -> Alert: {name} has attendance below 75% ({pct:.2f}%)")

#20.Store deposits and withdrawals in a file. Read the file and calculate: 
•#Total deposits 
•#Total withdrawals 
•#Final balance 
•#Largest 

bank_file = "transactions.txt
with open(bank_file, "w") as f:
    f.write("DEPOSIT,5000\nWITHDRAWAL,1200\nDEPOSIT,3000\nWITHDRAWAL,400\n")

deposits = 0
withdrawals = 0
largest_tx = 0

with open(bank_file, "r") as f:
    for line in f:
        tx_type, amt = line.strip().split(",")
        amt = float(amt)
        if amt > largest_tx:
            largest_tx = amt
        if tx_type.upper() == "DEPOSIT":
            deposits += amt
        elif tx_type.upper() == "WITHDRAWAL":
            withdrawals += amt

print(f"Total Deposits: {deposits}")
print(f"Total Withdrawals: {withdrawals}")
print(f"Final Balance: {deposits - withdrawals}")
print(f"Largest Transaction: {largest_tx}")



# 21. Maintain book records containing book ID, title, author, and
#     availability status. Implement operations to:
#     • Add a book.
#     • Search for a book.
#     • Issue a book.
#     • Return a book.
#     • Display available books.
# ----------------------------------------------------------------------
book_file = "books.txt"


def load_books():
    books = []
    try:
        with open(book_file, "r") as f:
            for line in f:
                b_id, title, author, status = line.strip().split(",")
                books.append(
                    {
                        "id": b_id,
                        "title": title,
                        "author": author,
                        "status": status,
                    }
                )
    except FileNotFoundError:
        pass
    return books


def save_books(books):
    with open(book_file, "w") as f:
        for b in books:
            f.write(f"{b['id']},{b['title']},{b['author']},{b['status']}\n")


def add_book(b_id, title, author):
    books = load_books()
    books.append(
        {"id": b_id, "title": title, "author": author, "status": "Available"}
    )
    save_books(books)


def search_book(title):
    books = load_books()
    found = [b for b in books if title.lower() in b["title"].lower()]
    return found


def issue_book(b_id):
    books = load_books()
    for b in books:
        if b["id"] == b_id and b["status"] == "Available":
            b["status"] = "Issued"
            save_books(books)
            print("Book issued successfully.")
            return
    print("Book not available or not found.")


def return_book(b_id):
    books = load_books()
    for b in books:
        if b["id"] == b_id and b["status"] == "Issued":
            b["status"] = "Available"
            save_books(books)
            print("Book returned successfully.")
            return
    print("Book not found or was not issued.")


def display_available():
    books = load_books()
    print("Available Books:")
    for b in books:
        if b["status"] == "Available":
            print(f"ID: {b['id']}, Title: {b['title']}, Author: {b['author']}")


add_book("101", "Python Programming", "Guido")
add_book("102", "Data Structures", "Mark")
display_available()
issue_book("101")
display_available()
return_book("101")

 22. Read the contents of two text files and create a third file
#     containing the contents of both files.
# ----------------------------------------------------------------------
file1 = input("Enter first filename: ")
file2 = input("Enter second filename: ")
file3 = input("Enter merged destination filename: ")

try:
    with open(file1, "r") as f1, open(file2, "r") as f2, open(
        file3, "w"
    ) as f3:
        f3.write(f1.read())
        f3.write("\n")
        f3.write(f2.read())
    print("Files merged successfully.")
except FileNotFoundError:
    print("One or both input files were not found!")

"""
Write a program to compare two text files and display whether their
#     contents are identical. If different, identify the first line where
#     they differ.
# ----------------------------------------------------------------------"""

file1 = input("Enter first filename to compare: ")
file2 = input("Enter second filename to compare: ")

try:
    with open(file1, "r") as f1, open(file2, "r") as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    identical = True
    max_lines = max(len(lines1), len(lines2))

    for idx in range(max_lines):
        l1 = lines1[idx] if idx < len(lines1) else None
        l2 = lines2[idx] if idx < len(lines2) else None

        if l1 != l2:
            identical = False
            print(f"Files differ at line {idx + 1}.")
            print(f"File 1: {l1.strip() if l1 is not None else '<EOF>'}")
            print(f"File 2: {l2.strip() if l2 is not None else '<EOF>'}")
            break

    if identical:
        print("Both files are identical.")
except FileNotFoundError:
    print("One or both files were not found!")