"""
Program: Demonstration of Different Import Variations in Python
--------------------------------------------------------------
This script shows:
1. Basic import
2. Import with alias
3. Import specific functions
4. Import specific functions with alias
5. Import all (*) from a module
6. Import inside a function
7. Dynamic import using importlib

"""

# -------------------------------------------------
# 1. BASIC IMPORT
# -------------------------------------------------
import math
print("\n1. BASIC IMPORT")
print("math.sqrt(16) =", math.sqrt(16))


# -------------------------------------------------
# 2. IMPORT WITH ALIAS
# -------------------------------------------------
import math as m
print("\n2. IMPORT WITH ALIAS")
print("m.pi =", m.pi)


# -------------------------------------------------
# 3. IMPORT SPECIFIC FUNCTIONS
# -------------------------------------------------
from math import factorial, sin
print("\n3. IMPORT SPECIFIC FUNCTIONS")
print("factorial(5) =", factorial(5))
print("sin(30°) =", sin(m.radians(30)))


# -------------------------------------------------
# 4. IMPORT SPECIFIC FUNCTION WITH ALIAS
# -------------------------------------------------
from math import sqrt as s
print("\n4. IMPORT FUNCTION WITH ALIAS")
print("s(49) =", s(49))


# -------------------------------------------------
# 5. IMPORT ALL (*)  — NOT RECOMMENDED
# -------------------------------------------------
from math import *
print("\n5. IMPORT ALL (*)")
print("ceil(4.2) =", ceil(4.2))
print("cos(0) =", cos(0))


# -------------------------------------------------
# 6. IMPORT INSIDE A FUNCTION
# -------------------------------------------------
print("\n6. IMPORT INSIDE A FUNCTION")

def calculate_circle_area(r):
    import math     # imported only when function is called
    return math.pi * r * r

print("Area (r=5) =", calculate_circle_area(5))


# -------------------------------------------------
# 7. DYNAMIC IMPORT USING importlib
# -------------------------------------------------
import importlib

print("\n7. DYNAMIC IMPORT USING importlib")

module_name = "random"
dynamic_mod = importlib.import_module(module_name)

print("Random number using dynamically imported module:",
      dynamic_mod.randint(1, 10))


# End of program
print("\n----- END OF IMPORT DEMONSTRATION -----")
