"""
Objective:
----------
This program demonstrates three different ways of storing and retrieving
student names and marks using FILE HANDLING in Python:

1. TEXT Mode (.txt)   - Simple, human readable
2. JSON Mode (.json)  - Structured format, easily used by programs
3. CSV Mode (.csv)    - Excel-friendly, tabular format

Each section includes:
- Writing data to a file
- Reading data back from the file

The purpose is to understand different file formats and when to use them.
"""

import json       # For JSON operations
import csv        # For CSV operations


# ------------------------------------------------------------
# 1) TEXT MODE: Write and Read student data as plain text
# ------------------------------------------------------------
def text_mode():
    filename = "students.txt"

    # Writing student data to a text file
    with open(filename, "w") as f:
        while True:
            name = input("Enter student name for TEXT (or 'stop'): ")
            if name.lower() == "stop":
                break
            marks = input("Enter marks: ")

            # Writing in simple "name, marks" format
            f.write(name + ", " + marks + "\n")

    print("\n--- Reading from TEXT file ---")
    with open(filename, "r") as f:
        for line in f:
            print(line.strip())  # Prints each student record

    print("TEXT mode completed.\n")


# ------------------------------------------------------------
# 2) JSON MODE: Write and Read student data in JSON format
# ------------------------------------------------------------
def json_mode():
    filename = "students.json"
    students = []  # Will hold dictionaries like {"name": "...", "marks": ...}

    # Collecting input from user
    while True:
        name = input("Enter student name for JSON (or 'stop'): ")
        if name.lower() == "stop":
            break
        marks = int(input("Enter marks: "))
        students.append({"name": name, "marks": marks})

    # Writing JSON file with proper formatting
    with open(filename, "w") as f:
        json.dump(students, f, indent=4) 
    #dump() converts Python objects (like dict, list) into JSON format and write them directly to a file
    print("\n--- Reading from JSON file ---")
    with open(filename, "r") as f:
        data = json.load(f)  # Converts JSON → Python list
        for student in data:
            print(student)

    print("JSON mode completed.\n")


# ------------------------------------------------------------
# 3) CSV MODE: Write and Read student data in CSV format
# ------------------------------------------------------------
def csv_mode():
    filename = "students.csv"

    # Writing data to CSV file (best for Excel)
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f) 
        #csv.writer(f) creates a writer object that allows you to write tabular data (rows and columns) to a CSV file.
        writer.writerow(["Name", "Marks"])  # Header row

        while True:
            name = input("Enter student name for CSV (or 'stop'): ")
            if name.lower() == "stop":
                break
            marks = input("Enter marks: ")

            writer.writerow([name, marks])  # Write row to CSV

    print("\n--- Reading from CSV file ---")
    with open(filename, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

    print("CSV mode completed.\n")


# ------------------------------------------------------------
# MAIN PROGRAM: Calls all 3 file-handling methods
# ------------------------------------------------------------
def main():
    print("\n===== FILE HANDLING: TEXT, JSON & CSV Combined Program =====\n")

    print("\n>>> Running TEXT mode...\n")
    text_mode()

    print("\n>>> Running JSON mode...\n")
    json_mode()

    print("\n>>> Running CSV mode...\n")
    csv_mode()

    print("\nAll 3 methods completed successfully!\n")


# Run the program
main()

