"""
Program to demonstrate basic structure of Python without classes

Comments – explain code (single/multi-line).

Constants – defined at the top, usually in UPPERCASE.

Imports – bring in libraries.

Global Variables – accessible throughout program.

Functions – reusable blocks of code.

Local Variables – exist only inside functions or blocks.

Main Block – controls execution when the file is run directly.
"""

# Import statements
import math
from datetime import datetime

# Constant
PI = 3.14159

# Global variable
global_variable=10

# Function definition
def area_of_circle(radius):
    """Calculate area of a circle"""
    # Local variable
    area = PI * radius * radius
    return area

area=area_of_circle(global_variable)
print("area:",area)

# Main program
if __name__ == "__main__":
    # Local variable inside main block
    r = 7
    print("Radius:", r)
    print("Area of circle:", area_of_circle(r))
    global_variable='A'
    # Working with global variable
    #global_counter += 1
    #print("Program executed", global_counter, "time(s)")
    print("global_variable:",global_variable)
    # Using imported module
    print("Current Year:", datetime.now().year)
