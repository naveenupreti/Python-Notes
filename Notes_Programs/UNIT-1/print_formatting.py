# ------------------------------------------------------------
# Python Script: Student Details Formatting Demonstration
# Includes:
#  - Inline comments explaining every formatting method
#  - Sample input and sample output (at the end)
# ------------------------------------------------------------

# Taking input
name = input("Enter student name: ")
roll_no = int(input("Enter roll number (int): "))
fees = float(input("Enter fees (float): "))

print("\n--- Printing in Different Ways ---\n")

# 1. Simple print with commas (auto convert + space)
print("1. With commas ->", "Name:", name, "Roll:", roll_no, "Fees:", fees)

# 2. String concatenation (must convert numbers to str)
print("2. Concatenation -> " + "Name: " + name + " Roll: " +
      str(roll_no) + " Fees: " + str(fees))

# 3. Old-style % formatting
print("3. %% formatting -> Name: %s Roll: %d Fees: %.2f" % (name, roll_no, fees))

# %-10s = left align in width 10
# %05d = pad with zeroes to width 5
# %10.2f = width=10, 2 decimals
print("   Width & Align -> Name: %-10s Roll: %05d Fees: %10.2f" %
      (name, roll_no, fees))

# 4. .format() method (basic)
print("4. .format() -> Name: {} Roll: {} Fees: {}".format(name, roll_no, fees))

# .format() with specifiers
print("   With specifiers -> Name: {:<10} Roll: {:05d} Fees: {:10.2f}".format(
    name, roll_no, fees))

# 5. .format() with indexes
print("5. With indexes -> Name: {0} Roll: {1} Fees: {2}".format(
    name, roll_no, fees))

# 6. .format() with names
print("6. With names -> Name: {n} Roll: {r} Fees: {f}".format(
    n=name, r=roll_no, f=fees))

# 7. f-string formatting (modern and best)
print(f"7. f-string -> Name: {name} Roll: {roll_no} Fees: {fees}")

# f-string with specifiers
print(f"   With specifiers -> Name: {name:<10} Roll: {roll_no:05d} Fees: {fees:10.2f}")

# 8. format_map() with dictionary
student = {"name": name, "roll": roll_no, "fees": fees}
print("8. format_map -> Name: {name} Roll: {roll} Fees: {fees:.2f}".format_map(student))

# ----------------------------------------------------------------
# TABULAR OUTPUT
print("\n--- Tabular Output (Student Record) ---\n")

print("Using % formatting:")
print("%-15s %-10s %-10s" % ("Name", "Roll No", "Fees"))
print("%-15s %-10d %-10.2f" % (name, roll_no, fees))

print("\nUsing .format():")
print("{:<15} {:<10} {:<10}".format("Name", "Roll No", "Fees"))
print("{:<15} {:<10d} {:<10.2f}".format(name, roll_no, fees))

print("\nUsing f-strings:")
print(f"{'Name':<15} {'Roll No':<10} {'Fees':<10}")
print(f"{name:<15} {roll_no:<10d} {fees:<10.2f}")


# ------------------------------------------------------------
# SAMPLE INPUT + OUTPUT (FOR REFERENCE)
# ------------------------------------------------------------

"""
================ SAMPLE INPUT ================
Enter student name: Naveen
Enter roll number (int): 101
Enter fees (float): 45000.50


================ SAMPLE OUTPUT ===============

--- Printing in Different Ways ---

1. With commas -> Name: Naveen Roll: 101 Fees: 45000.5
2. Concatenation -> Name: Naveen Roll: 101 Fees: 45000.5
3. % formatting -> Name: Naveen Roll: 101 Fees: 45000.50
   Width & Align -> Name: Naveen     Roll: 00101 Fees:   45000.50
4. .format() -> Name: Naveen Roll: 101 Fees: 45000.5
   With specifiers -> Name: Naveen     Roll: 00101 Fees:   45000.50
5. With indexes -> Name: Naveen Roll: 101 Fees: 45000.5
6. With names -> Name: Naveen Roll: 101 Fees: 45000.5
7. f-string -> Name: Naveen Roll: 101 Fees: 45000.5
   With specifiers -> Name: Naveen     Roll: 00101 Fees:   45000.50
8. format_map -> Name: Naveen Roll: 101 Fees: 45000.50

--- Tabular Output (Student Record) ---

Using % formatting:
Name            Roll No    Fees      
Naveen          101        45000.50 

Using .format():
Name            Roll No    Fees      
Naveen          101        45000.50  

Using f-strings:
Name            Roll No    Fees      
Naveen          101        45000.50
"""
