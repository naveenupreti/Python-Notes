# ------------------------------------------------------------
# FILE HANDLING IN PYTHON - CONCEPTS + PROGRAMS (EXECUTABLE)
# ------------------------------------------------------------
# ============================================================
#                   CONCEPTS OF FILE HANDLING
# ============================================================

# A file is a resource which is used to store data permanently
# on storage devices.

# File handling means performing operations on files such as:
# Opening a file
# Reading data
# Writing data
# Closing the file
# Python provides built-in functions to do all these.
# Steps in File Handling
# The main steps:
    # Open the file
    # Perform operations (read/write)
    # Close the file
# Python performs file operations using the built-in 'open()' function.
# open(filename, mode)

# Common modes:
#   'r'  -> read (file must exist)
#   'w'  -> write (overwrites, creates file)
#   'a'  -> append (adds data at the end)
#   'r+' -> read + write (does not create new file)
#   'w+' -> write + read (creates file)
#   'a+' -> append + read (creates file)
#
# File pointer functions:
#   seek(position) -> moves pointer
#   tell()         -> returns current pointer position
#
# Always close the file using close() OR use with-statement (recommended).


# ============================================================
#                PROGRAM 1 — Writing to a File
# ============================================================

# Creating/writing data to a file using 'w' mode
f = open("example.txt", "w")      # opens file in write mode (creates file)
f.write("Hello, this is line 1.\n")
f.write("Hello, this is line 2.\n")
f.close()                         # close the file
print("Program 1: Writing completed.")


# ============================================================
#                PROGRAM 2 — Reading Entire File
# ============================================================

f = open("example.txt", "r")      # open file in read mode
content = f.read()                # read whole file as a string
print("\nProgram 2: Reading entire file:")
print(content)
f.close()


# ============================================================
#                PROGRAM 3 — Reading Line-by-Line
# ============================================================

f = open("example.txt", "r")
print("Program 3: Reading line by line:")
print(f.readline())               # reads first line
print(f.readline())               # reads second line
f.close()


# ============================================================
#                PROGRAM 4 — Using readlines()
# ============================================================

f = open("example.txt", "r")
lines = f.readlines()             # returns list of all lines
print("Program 4: Using readlines():")
print(lines)
f.close()


# ============================================================
#             PROGRAM 5 — Append Mode ('a')
# ============================================================

f = open("example.txt", "a")      # open in append mode
f.write("This line is added later.\n")
f.close()
print("Program 5: Append complete.")


# ============================================================
#      PROGRAM 6 — Using 'with' (auto-close file)
# ============================================================

print("\nProgram 6: Using with statement (best practice)")

with open("example_with.txt", "w") as f:
    f.write("This file is created using 'with'.\n")
    f.write("File closes automatically.")

# No need to close(), 'with' handles it


# ============================================================
#        PROGRAM 7 — File Pointer: tell() and seek()
# ============================================================

f = open("example.txt", "r")
print("\nProgram 7: File Pointer Demonstration")

print("Initial Pointer Position:", f.tell())   # should be 0
print("Reading 5 chars:", f.read(5))           # read first 5 characters
print("Pointer After Reading:", f.tell())      # new position

f.seek(0)                                      # move pointer to beginning
print("Pointer Reset to:", f.tell())
f.close()


# ============================================================
#    PROGRAM 8 — Handling Exceptions (Safe File Access)
# ============================================================

print("\nProgram 8: Exception Handling Example")

try:
    f = open("no_such_file.txt", "r")          # file does not exist
    print(f.read())
except FileNotFoundError:                       # specific exception
    print("Error: The file does not exist!")
finally:
    print("Finally block executed.")


# ============================================================
#   END OF FILE
# ============================================================
