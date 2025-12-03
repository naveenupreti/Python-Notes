'''
What is a Module?

A module is simply a Python file (.py) that contains variables, functions or classes.
You can import this file in another Python program.
Example: user-defined module — mymath.py
# mymath.py
def add(a, b):
    return a + b

def square(x):
    return x * x

Using this module in another file
import mymath
print(mymath.add(10, 20))
print(mymath.square(5))

What is a Package?

A package is a directory containing multiple modules + a special file __init__.py.

Example package structure
calc_pkg/
    __init__.py
    arithmetic.py
    geometry.py

arithmetic.py
def add(a,b): return a+b
def sub(a,b): return a-b

geometry.py
def area_circle(r):
    from math import pi
    return pi * r * r

Using package
from calc_pkg.arithmetic import add
from calc_pkg.geometry import area_circle

print(add(5,3))
print(area_circle(4))

'''

import importlib

module_name = input("Enter module name (e.g., math, random, sys, datetime): ")

try:
    #this line is important to see the actual contents of a particular module
    mod = importlib.import_module(module_name) 

    print("\n===== CONTENTS OF MODULE (dir) =====")
    print(dir(mod))

    print("\n===== MODULE DOCUMENTATION (help) =====")
    help(mod)

except ModuleNotFoundError:
    print("Error: The module does not exist.")