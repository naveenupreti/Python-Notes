# -----------------------------
# Strings
# -----------------------------
# Strings are sequences of characters enclosed in quotes.
s1 = 'Hello'
s2 = "World"
s3 = '''This is
a multiline string.'''
print(s1, s2)
print(s3)

# Strings with special characters using escape sequence
msg2 = "He said, \"Let Us Python\""
file1 = "C:\\temp\\newfile"  # Escaping backslashes
file2 = r"C:\temp\newfile"   # Raw string to ignore escapes
print(msg2)
print(file1)
print(file2)

# -------------------------------------------------------------
# Multiline Strings
# -------------------------------------------------------------

# Using implicit concatenation across lines
msg3 = "multi...\n" \
       "line ..." \
       "string..."
print("msg3="+msg3)

# Using triple quotes (newline preserved)
msg4 = """multi...
line...
string......"""
print("msg4="+msg4)

# Using parentheses for concatenation
msg5 = ("multi..."
        "line...."
        "string....")
print("msg5="+msg5)

# -----------------------------
# Accessing Strings
# -----------------------------
s = "PYTHON"
print(s[0])   # First character: P
print(s[3])   # Fourth character: H
print(s[-1])  # Last character: N
print(s[-3])  # Third from last: H

# -----------------------------
# Basic Operations
# -----------------------------
s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)   # Concatenation
print(s1 * 3)          # Repetition
print("H" in s1)       # Membership (True)
print(len(s2))         # Length of string

# -----------------------------
# String Slices
# -----------------------------
s = "PYTHONPROGRAM"
print(s[0:6])    # PYTHON
print(s[:6])     # PYTHON (start to index 5)
print(s[6:])     # PROGRAM (index 6 to end)
print(s[-7:-1])  # PROGRA (negative indices)
print(s[::2])    # Every 2nd char
print(s[::-1])   # Reverse the string

# -----------------------------
# String Functions & Methods
# -----------------------------
s = " hello python "
print(s.upper())        # Convert to uppercase
print(s.lower())        # Convert to lowercase
print(s.title())        # Title case
print(s.capitalize())   # First letter capital
print(s.strip())        # Remove leading/trailing spaces
print(s.find("py"))     # Find substring (returns index)
print(s.count("o"))     # Count occurrences
print(s.replace("python", "world"))  # Replace substring
words = s.split()       # Split into list
print(words)
print("-".join(words))  # Join list with hyphen
print("123".isdigit())  # Check if digits
print("abc".isalpha())  # Check if alphabets
print(" ".isspace())    # Check if space

print(chr(65))      # 'A'
print(chr(97))      # 'a'
print(chr(48))      # '0'
print(chr(32))      # ' '
print(chr(8377))    # '₹'

# =========================================================
# CHR & ORD
# =========================================================

# -----------------------------
# ASCII value Lookup
# -----------------------------
ch = 'A'
print(f"ASCII value of {ch} is {ord(ch)}")

# -----------------------------
# Character from Code
# -----------------------------
num = 8377
print(f"Character for code {num} is {chr(num)}")

# -----------------------------
# Print A–Z and a–z
# -----------------------------
print("Uppercase letters:")
for i in range(65, 91):
    print(chr(i), end=" ")
print("\nLowercase letters:")
for i in range(97, 123):
    print(chr(i), end=" ")
print()


# -----------------------------
# ASCII Pattern (A-E)
# -----------------------------
rows = 5
for i in range(65, 65 + rows):
    for j in range(65, i + 1):
        print(chr(j), end=" ")
    print()


'''
Key Rules of String Comparison in Python:

Strings are compared character by character using Unicode/ASCII values.

Uppercase letters ("A"–"Z") have lower values than lowercase letters ("a"–"z").

"A" = 65, "B" = 66 … "Z" = 90

"a" = 97, "b" = 98 … "z" = 122

If all characters are equal, the shorter string is considered smaller.

'''
# String Comparison
# -------------------------------------------------------------
s1 = "Bombay"
s2 = "bombay"
s3 = "Nagpur"
s4 = "Bombaywala"
s5 = "Bombay"

print(s1 == s2)  # False
print(s1 == s5)  # True
print(s1 <= s3)  # True
print(s1 > s5)   # False
print(s1 < s2)   # True
print(s1 <= s4)  # True


# Finding and Replacing
s = "The Terrible Tiger Tore The Towel"
pos = -1
while True:
    pos = s.find("T", pos + 1)
    if pos == -1:  # Not found
        break
    print(pos, s[pos])

count_t = s.count("T")
print(f"count_t={count_t}")
s = s.replace("T", "t", count_t)
print(s)

