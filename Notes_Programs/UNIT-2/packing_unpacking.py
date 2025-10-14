nums = [1, 2, 3, 4, 5]

a, *b = nums
print(a)  # 1
print(b)  # [2, 3, 4, 5]

*a, b = nums
print(a)  # [1,2, 3, 4]
print(b)  # 5

# ---------------------------------------------------------
# Topic: Packing and Unpacking in Python
# Author: Naveen Upreti
# Purpose: Demonstration for MCA Students (BMC301: Python Programming)
# ---------------------------------------------------------

print("\n========== Packing and Unpacking Demonstration ==========")

# 1️⃣ Packing Example - Tuple Packing
print("\n--- Example 1: Tuple Packing ---")
student = ("Naveen", 101, "MCA", 88.5)
print("Packed Tuple:", student)

# 2️⃣ Unpacking Example - Extracting Tuple Values
print("\n--- Example 2: Tuple Unpacking ---")
name, roll, course, marks = student
print("Name:", name)
print("Roll No:", roll)
print("Course:", course)
print("Marks:", marks)

# 3️⃣ Partial Unpacking Example
print("\n--- Example 3: Partial Unpacking using * ---")
student_info = ("Naveen", 101, "MCA", 88.5, 22, "naveen@mail.com")
name, roll, course, *other_details = student_info
print("Name:", name)
print("Roll No:", roll)
print("Course:", course)
print("Other Details:", other_details)

# 4️⃣ Packing using *args
print("\n--- Example 4: Packing using *args in a Function ---")
def student_summary(*details):
    print("Packed Details (tuple):", details)

student_summary("Naveen", 101, "MCA", 88.5)

# 5️⃣ Unpacking Tuple into Function Arguments
print("\n--- Example 5: Unpacking Tuple into Function Arguments ---")
def display(name, roll, course, marks):
    print(f"{name} ({course}) - Roll {roll}, Marks {marks}")

student = ("Naveen", 101, "MCA", 88.5)
display(*student)

# 6️⃣ Packing and Unpacking with Function Return Values
print("\n--- Example 6: Function Returning Multiple Values ---")
def get_student():
    return ("Naveen", "MCA", 88.5)

name, course, marks = get_student()
print(f"{name} ({course}) scored {marks}%")

# 7️⃣ Dictionary Packing and Unpacking
print("\n--- Example 7: Dictionary Packing and Unpacking ---")
def show_info(**info):
    print("Packed Dictionary:", info)

show_info(name="Naveen", age=30, city="Dehradun")

data = {"name": "Naveen", "roll": 101, "course": "MCA", "marks": 88.5}
print("Unpacking dictionary into function:")
def show_student(name, roll, course, marks):
    print(f"{name} ({course}) - Roll {roll}, Marks {marks}")

show_student(**data)

print("\n✅ Demonstration completed successfully!")
print("========================================================")
