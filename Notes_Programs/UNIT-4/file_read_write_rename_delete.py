"""
A complete Python program demonstrating:
1. Writing to a file
2. Appending to a file
3. Reading a file
4. Renaming the file
5. Deleting the file
With proper try–except error handling and os.path.exists()
"""

import os

# ------------------------------------------------------------
# 1. WRITE to a file
# ------------------------------------------------------------
filename = "data.txt"

try:
    with open(filename, "w") as f:
        f.write("Hello, this is the first line.\n")
        f.write("This file demonstrates file operations in Python.\n")
    print("File created and written successfully.")
except Exception as e:
    print("Error while writing to file:", e)


# ------------------------------------------------------------
# 2. APPEND to the file
# ------------------------------------------------------------
try:
    with open(filename, "a") as f:
        f.write("This line was appended later.\n")
    print("Data appended successfully.")
except Exception as e:
    print("Error while appending:", e)


# ------------------------------------------------------------
# 3. READ the file
# ------------------------------------------------------------
try:
    print("\nReading File:")
    with open(filename, "r") as f:
        print(f.read())
except FileNotFoundError:
    print("The file does not exist; cannot read.")
except Exception as e:
    print("Error while reading the file:", e)


# ------------------------------------------------------------
# 4. RENAME the file
# ------------------------------------------------------------
new_name = "info.txt"

try:
    if os.path.exists(filename):
        os.rename(filename, new_name)
        print(f"File renamed from '{filename}' to '{new_name}'.")
    else:
        print(f"Cannot rename. '{filename}' does not exist.")
except Exception as e:
    print("Error while renaming file:", e)


# ------------------------------------------------------------
# 5. DELETE the file
# ------------------------------------------------------------
try:
    if os.path.exists(new_name):
        os.remove(new_name)
        print(f"'{new_name}' deleted successfully.")
    else:
        print(f"File '{new_name}' not found. Nothing to delete.")
except Exception as e:
    print("Error while deleting the file:", e)
