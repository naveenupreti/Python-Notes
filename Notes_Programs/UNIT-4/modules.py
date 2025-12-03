'''
Below is a clean, proper multi-file Python project demonstrating:

✔ User-defined modules
✔ Standard library modules: random, sys, math, datetime, re
✔ Built-in operations: string, list
✔ Third-party modules (numpy, scipy) – optional

✅ PROJECT STRUCTURE
project/
│
├── main.py
├── mymath.py
├── mystrings.py
├── mylists.py
├── myregex.py
├── mystdlib.py
└── thirdparty.py


Each module contains related functionality.
main.py imports all modules and runs them.

------------------------------------------------------------
1. mymath.py
------------------------------------------------------------
'''

"""
mymath.py
Demonstrates Math module and user-defined math functions.
"""

import math

def demo_math():
    print("=== MATH MODULE ===")
    print("Square root of 25:", math.sqrt(25))
    print("Value of π:", math.pi)
    print("sin(90°):", math.sin(math.radians(90)))

'''
------------------------------------------------------------
📄 2. mystrings.py
------------------------------------------------------------
'''

"""
mystrings.py
Demonstrates string operations.
"""

def demo_strings():
    print("=== STRING OPERATIONS ===")
    s = "Hello Python Programming"
    print("Original:", s)
    print("Uppercase:", s.upper())
    print("Split:", s.split())
    print("Replace:", s.replace("Python", "Advanced Python"))

'''
------------------------------------------------------------
📄 3. mylists.py
------------------------------------------------------------
'''

"""
mylists.py
Demonstrates list operations.
"""

def demo_lists():
    print("=== LIST OPERATIONS ===")
    numbers = [1, 5, 3, 9, 2]
    print("Original:", numbers)

    numbers.append(7)
    print("After append:", numbers)

    numbers.sort()
    print("After sorting:", numbers)

    numbers.remove(3)
    print("After removing 3:", numbers)

'''
------------------------------------------------------------
📄 4. myregex.py
------------------------------------------------------------
'''

"""
myregex.py
Demonstrates Regular Expressions: match, search, replace.
"""

import re

def demo_regex():
    print("=== REGULAR EXPRESSIONS ===")

    text = "Python programming is fun!"

    # match() Checks pattern at the start of string.
    match_obj = re.match("Python", text)
    print("Match:", match_obj.group() if match_obj else "No match")

    # search() Checks pattern anywhere in string.
    search_obj = re.search("programming", text)
    print("Search:", search_obj.group() if search_obj else "Not found")

    # sub() Replace text.
    new_text = re.sub("fun", "powerful", text)
    print("Replace:", new_text)

'''
------------------------------------------------------------
📄 5. mystdlib.py
------------------------------------------------------------
'''

"""
mystdlib.py
Shows usage of random, sys, datetime modules.
"""

import random
import sys
from datetime import datetime, timedelta

def demo_stdlib():
    print("=== RANDOM MODULE ===")
    print("Random integer (1–10):", random.randint(1, 10))
    print("Random float:", random.random())
    print("Random choice:", random.choice(["apple", "banana", "cherry"]))

    print("\n=== SYS MODULE ===")
    print("Executable:", sys.executable)
    print("Arguments:", sys.argv)

    print("\n=== DATE & TIME MODULE ===")
    now = datetime.now()
    print("Current time:", now)
    print("After 5 days:", now + timedelta(days=5))
'''
------------------------------------------------------------
📄 6. thirdparty.py
------------------------------------------------------------
'''
"""
thirdparty.py
Demonstrates NumPy and SciPy (optional).
"""

def demo_thirdparty():
    print("=== THIRD-PARTY MODULES ===")
    try:
        import numpy as np
        print("Numpy array:", np.array([1, 2, 3]))
        print("Mean:", np.mean([1, 2, 3]))
    except ImportError:
        print("NumPy not installed. Install using: pip install numpy")

    try:
        import scipy
        print("SciPy version:", scipy.__version__)
    except ImportError:
        print("SciPy not installed. Install using: pip install scipy")

'''
------------------------------------------------------------
📄 7. main.py
------------------------------------------------------------
'''

"""
main.py
This file imports all user-defined modules and runs them.
"""

from mymath import demo_math
from mystrings import demo_strings
from mylists import demo_lists
from myregex import demo_regex
from mystdlib import demo_stdlib
from thirdparty import demo_thirdparty

print("===== PYTHON MODULE DEMONSTRATION PROGRAM =====\n")

demo_math()
print()

demo_strings()
print()

demo_lists()
print()

demo_regex()
print()

demo_stdlib()
print()

demo_thirdparty()

print("\n===== END OF PROGRAM =====")
