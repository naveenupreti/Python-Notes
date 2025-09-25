# -------------------------------------------------------------
# Basic String Creation and Escape Sequences
# -------------------------------------------------------------

# Simple string assignment
msg = "Hoopla"
print(msg)  # Prints: Hoopla

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
msg3 = "What is this life if full of care...\n" \
       "We have no time to stand and stare"
print(msg3)

# Using triple quotes (newline preserved)
msg4 = """What is this life if full of care...
We have no time to stand and stare"""
print(msg4)

# Using parentheses for concatenation
msg5 = ("What is this life if full of care..."
        "We have no time to stand and stare")
print(msg5)

# -------------------------------------------------------------
# String Replication
# -------------------------------------------------------------
msg6 = "Hoopla"
print(msg6 * 3)  # Prints: HooplaHooplaHoopla

# -------------------------------------------------------------
# String Immutability
# -------------------------------------------------------------
msg7 = "Utopia"
msg8 = "Today..."
# Strings are immutable, but concatenation produces a new string
msg7 = msg7 + msg8
print(msg7)  # Prints: UtopiaToday...

# -------------------------------------------------------------
# Built-in Functions with Strings
# -------------------------------------------------------------
print(len("Hoopla"))   # Length of string
print(min("Hoopla"))   # Minimum Unicode character
print(max("Hoopla"))   # Maximum Unicode character

# -------------------------------------------------------------
# String Slicing Examples
# -------------------------------------------------------------
s = "Bamboozled"

# Extracting specific parts
print(s[0], s[1])       # B a
print(s[7], s[9])       # e d
print(s[2:])            # mboozled
print(s[:6])            # Bamboo
print(s[::-1])          # Reverse string

# Concatenation with literals
s = s + "Hype"
print(s)  # BamboozledHype

# Insert string in between
s = s[:6] + "Monger" + s[6:]
print(s)

# -------------------------------------------------------------
# String Methods Examples
# -------------------------------------------------------------
msg = "Surreal"
print(type(msg))  # <class 'str'>
print(id(msg))    # Address in memory

print(msg.isalpha())     # True if only alphabets
print(msg.isdigit())     # False
print(msg.isalnum())     # True
print(msg.islower())     # True
print(msg.isupper())     # False
print(msg.startswith("Su"))  # True
print(msg.endswith("al"))    # True

# Replace
print(msg.replace("r", "R"))  # SuRReal

# Join
print("-".join("Hello"))  # H-e-l-l-o

# Case conversions
msg = "Hello"
print(msg.upper())       # HELLO
print(msg.lower())       # hello
print(msg.capitalize())  # Hello
print(msg.title())       # Hello
print(msg.swapcase())    # hELLO

# -------------------------------------------------------------
# Conversion Functions
# -------------------------------------------------------------
age = 25
print("She is " + str(age) + " years old")

i = int("123")
f = float("12.34")
c = complex("12+3j")
print(ord("A"))  # 65
print(chr(65))   # A

# -------------------------------------------------------------
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

# -------------------------------------------------------------
# Problem 4.5 Example (Finding and Replacing)
# -------------------------------------------------------------
s = "The Terrible Tiger Tore The Towel"
pos = -1
while True:
    pos = s.find("T", pos + 1)
    if pos == -1:  # Not found
        break
    print(pos, s[pos])

count_t = s.count("T")
s = s.replace("T", "t", count_t)
print(s)

# =============================================================
# Exercises - Section A
# =============================================================

# (a) String operations on "Shenanigan"
s = "Shenanigan"
print(s[0], s[1])     # S h
print(s[2], s[3])     # e n
print(s[2:])          # enanigan
print(s[:6])          # Shenan
print(s[::-1])        # naginaheS
print(s[::2])         # Seaia
print(s[::3])         # Snin
print(s[::4])         # Saa

# Concatenation
print(s + "Type")     # ShenaniganType
print(s[:6] + "Wabbite")  # ShenanWabbite

# (b) Title conversion
s = "Visit ykanetkar.com for online courses in programming"
print(s.title())

# (c) Selective uppercasing
s = "Light travels faster than sound. This is why some people appear bright until you hear them speak."
s = s.replace("Light", "LIGHT").replace("sound", "SOUND")
print(s)

# (d) Check string methods
s = "HumptyDumpty"
print("s =", s)
print(s.isalpha())       # True
print(s.isdigit())       # False
print(s.isalnum())       # True
print(s.islower())       # False
print(s.isupper())       # False
print(s.startswith("Hump"))  # True
print(s.endswith("Dump"))    # False

# (e) Raw string purpose
# Raw strings ignore escape sequences like \n, \t, etc.

# (f) Splitting a sentence into words
s = "The difference between stupidity and genius is that genius has its limits"
print(s.split())

# (g) Two ways to write "He said, 'Let Us Python'"
s1 = "He said, 'Let Us Python'"
s2 = 'He said, "Let Us Python"'
print(s1, s2)

# (h) id() and type()
print(id("Imaginary"))
print(type("Imaginary"))

# (i) Splitting and partitioning
s = "C:\\Users\\Kanetkar\\Documents"
print(s.split("\\"))        # Splitting
print(s.partition("\\"))    # Partitioning

# (j) Strings are iterable, sliceable, and immutable → True

# (k) Extract "TraPoete" from "ThreadProperties"
s = "ThreadProperties"
print(s[0] + s[2:4] + s[6:10])  # TraPoete

# (l) Trimming spaces
s = " Flanked by spaces on either side "
print(s.strip())

# (m) Same string IDs due to interning
s1 = s2 = s3 = "Hello"
print(id(s1), id(s2), id(s3))

# (n) Extract a character by index
msg = "Aeroplane"
ch = msg[-1]  # Last character
print(ch)

# =============================================================
# Exercises - Section B (Matching Pairs)
# =============================================================
msg = "Keep yourself warm"

# Expected matches from book
print(msg.partition(" "))      # ('Keep', ' ', 'yourself warm')
print(msg.split(" "))          # ['Keep', 'yourself', 'warm']
print(msg.startswith("Keep"))  # True
print(msg.endswith("Keep"))    # False
print(msg.swapcase())          # kEEP YOURSELF WARM
print(msg.capitalize())        # Keep yourself warm
print(msg.count("e"))          # 3
print(len(msg))                # 19
print(msg[0])                  # K
print(msg[-1])                 # m
print(msg[7])                  # y
print(msg[15:])                # arm
print(msg[5:])                 # yourself warm
