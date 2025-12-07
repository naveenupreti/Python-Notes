'''
1 __name__

__name__ is a special built-in variable in Python.

It tells Python how a script is being executed.

There are two main cases:

How the script runs	Value of __name__
Running the script directly	"__main__"
Importing the script as a module	The module’s filename (without .py)
'''
"""
Program: Demonstrate __name__, "__main__" and main() function behavior.

This file includes:
1. Printing __name__ at the top level.
2. Using if __name__ == "__main__": guard.
3. Defining a main() function.
4. Demonstrating behavior when running directly vs importing.
5. Inline comments explaining each step.
6. Sample outputs of both cases at the end.
"""

# -------------------------------
# TOP LEVEL PRINT
# Executes always, whether run directly or imported.
print("Top-level print: __name__ =", __name__)

# -------------------------------
# MAIN FUNCTION
def main():
    """
    Main logic of the program.
    Executes only if __name__ == "__main__"
    """
    print("Inside main(): This executes ONLY when running this file directly.")
    print("Inside main(): __name__ =", __name__)

# -------------------------------
# MAIN GUARD
# Only executes this block if the file is run directly.
if __name__ == "__main__":
    print('Condition check: __name__ == "__main__" is TRUE.')
    main()
else:
    print('Condition check: __name__ == "__main__" is FALSE (file imported).')


# ============================================================
#                 SAMPLE OUTPUT OF THE PROGRAM
# ============================================================

"""
===============================
CASE 1: Run the file directly
Command:
    python name_main_demo.py

Output:
Top-level print: __name__ = __main__
Condition check: __name__ == "__main__" is TRUE.
Inside main(): This executes ONLY when running this file directly.
Inside main(): __name__ = __main__
===============================


===============================
CASE 2: Import the file as a module
Create file2.py:

import name_main_demo

Run:
    python file2.py

Output:
Top-level print: __name__ = name_main_demo
Condition check: __name__ == "__main__" is FALSE (file imported).
===============================
"""
