'''
Exception:
    A runtime error that stops normal program flow.

Why Exception Handling?
   To prevent program crash and handle errors gracefully.
   Exception Handling allows your program to continue running even if an error occurs.
   Instead of stopping the program immediately, Python lets you handle the error gracefully. 
   

Keywords:
  1. try     → Code that may cause an exception
  2. except  → Handles the exception
  3. else    → Runs only if no exception occurs
  4. finally → Always runs (cleanup code)
  5. raise   → Manually throw an exception

User-defined Exceptions:
    Create custom exceptions using classes derived from Exception.
'''
# ------------------------------------------------------------
# 1. Basic try-except example
# ------------------------------------------------------------
print("--- Basic try-except Example ---")
try:
    a = int("abc")  # raises ValueError
except ValueError:
    print("Invalid conversion!")

# ------------------------------------------------------------
# 2. Multiple except blocks
# ------------------------------------------------------------
print("--- Multiple except blocks Example ---")
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except TypeError:
    print("Wrong data type!")

# ------------------------------------------------------------
# 3. Generic exception handling
# ------------------------------------------------------------
print("--- Generic Exception Example ---")
try:
    x = int("abc")
except Exception as e:
    print("Error:", e)

# ------------------------------------------------------------
# 4. try-except-else block
# ------------------------------------------------------------
print("--- try-except-else Example ---")
try:
    num = int("5")
except ValueError:
    print("Error in conversion")
else:
    print("Conversion successful:", num)

# ------------------------------------------------------------
# 5. finally block example
# ------------------------------------------------------------
print("--- finally Example ---")
try:
    f = open("not_available.txt")
except FileNotFoundError:
    print("File not found!")
finally:
    print("Always executed: closing resources if any...")

# ------------------------------------------------------------
# 6. Using raise
# ------------------------------------------------------------
print("--- raise Example ---")
age = -5
try:
    if age < 0:
        raise ValueError("Age cannot be negative")
except ValueError as e:
        print("Raised Error:", e)

# ------------------------------------------------------------
# 7. Complete Example (try, except, else, finally)
# ------------------------------------------------------------
print("--- Complete Example (try, except, else, finally) ---")
try:
    number = int(input("Enter any number:"))
    result = 10 / number
except ZeroDivisionError:
    print("Division error: cannot divide by zero!")
except ValueError:
    print("Invalid number!")
else:
    print("Division successful:", result)
finally:
    print("Program ended (finally block executed).")

# ------------------------------------------------------------
# 8. User-defined exceptions
# ------------------------------------------------------------
'''
User-defined exceptions in Python allow you to create your own custom
error types that make your code more meaningful and easier to debug.

Why User-Defined Exceptions?
Built-in exceptions (like ValueError, TypeError, IndexError) may not always
describe the type of error you want to handle.

Example:

Age must not be negative
Marks cannot exceed 100
Username must not contain spaces

These rules require custom exceptions.

How to Create a User-Defined Exception?

A custom exception is created by inheriting from the built-in Exception class.
Syntax:
class MyException(Exception):
    pass

Meaning:
MyException becomes a new exception type.
It behaves like any other Python exception.

pass means “do nothing”.
The class has no additional functionality, but it works because it extends Exception.
Even an empty custom exception is valid.
'''
print("--- User Defined Exception Example 1 ---")

# Define a simple custom exception
class AgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        # Raise the custom exception with a message
        raise AgeError("Age must be 18 or above.")
    else:
        print("Valid age! You are eligible to vote.")

# -------- Test the custom exception --------
try:
    age = 16
    check_age(age)
except AgeError as e:
    print("Caught Exception:", e)


print("--- User Defined Exception Example 2 ---")

class NegativeNumberError(Exception):
    """Custom exception for negative numbers"""
    pass

def check_number(n):
    if n < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")
    else:
        print("Number is positive:", n)
try:
    check_number(-5)
except NegativeNumberError as e:
    print("Custom Exception Caught:", e)

print("--- End of Exception Handling Demo ---")
