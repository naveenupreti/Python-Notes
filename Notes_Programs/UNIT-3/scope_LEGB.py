'''

What is LEGB in Python?

LEGB is the rule Python follows to resolve identifier names —
that is, when you use a variable, Python looks for it in this order:

Order	Scope Type				Meaning
L		Local				Inside the current function
E		Enclosing			In the outer (enclosing) function if it’s a nested function
G		Global				At the top level of the script/module
B		Built-in			Python’s built-in names (like len, sum, print)

If Python can’t find the variable in any of these scopes, it raises a NameError.
'''


# --------------------------------------------------------
# Program: Simple Example of LEGB Rule in Python
# --------------------------------------------------------

# ---------- Global Scope ----------
x = "Global X"  # This is a global variable

def outer_function():
    # ---------- Enclosing Scope ----------
    x = "Enclosing X"  # Variable in enclosing (outer) function

    def inner_function():
        # ---------- Local Scope ----------
        x = "Local X"  # Variable in local (inner) function
        print("Inside inner_function:", x)  # Local scope is searched first

    inner_function()  # Call the inner function
    print("Inside outer_function:", x)  # Enclosing variable is used here

# ---------- Main Program ----------
outer_function()       # Call outer function
print("In Global Scope:", x)  # Global variable is used here

# ---------- Built-in Scope ----------
# Built-in names like len(), print(), sum(), etc.
print("Built-in len() example:", len([1, 2, 3]))  # Built-in scope
