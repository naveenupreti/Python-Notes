# ===============================
# Global, Outer, and Inner Scope Demo
# ===============================

# Global variable
x = "Global variable"

def outer_function():
    # Outer variable (same name as global)
    x = "Outer variable"
    print("1️⃣ Inside outer_function (initial):", x)

    # ---- Inner Function Definition ----
    def inner_function():
        # Inner variable (same name again)
        x = "Inner variable"
        print("2️⃣ Inside inner_function:", x)

    # Call inner function
    inner_function()

    # After inner_function() call
    print("3️⃣ Inside outer_function (after inner):", x)

# ---- Call outer function ----
outer_function()

# Back in global scope
print("4️⃣ In global scope:", x)


print("\n==============================")
print("Now modifying outer variable using 'nonlocal' inside inner function")
print("==============================")

def outer_function2():
    x = "Outer variable"
    print("Before modification:", x)

    def inner_function2():
        nonlocal x  # refer to x from outer_function2, not create a new one
        x = "Modified outer variable"
        print("Inside inner_function2 (after nonlocal change):", x)

    inner_function2()
    print("After inner_function2:", x)

outer_function2()


print("\n==============================")
print("Now modifying global variable using 'global' inside inner function")
print("==============================")

def outer_function3():
    x = "Outer variable"

    def inner_function3():
        global x  # refers to global x, not outer or local one
        x = "Modified GLOBAL variable"
        print("Inside inner_function3 (modified global x):", x)

    inner_function3()
    print("Inside outer_function3 (x still outer):", x)

outer_function3()
print("After outer_function3, global x is now:", x)


print("\n==============================")
print("Same function name for outer and inner (shadowing example)")
print("==============================")

def func():
    print("This is outer func()")

    def func():  # inner function has SAME name → hides outer func inside
        print("This is inner func()")

    func()  # calls the inner one (outer func is shadowed)

func()


'''
Output:
1️⃣ Inside outer_function (initial): Outer variable
2️⃣ Inside inner_function: Inner variable
3️⃣ Inside outer_function (after inner): Outer variable
4️⃣ In global scope: Global variable

==============================
Now modifying outer variable using 'nonlocal' inside inner function
==============================
Before modification: Outer variable
Inside inner_function2 (after nonlocal change): Modified outer variable
After inner_function2: Modified outer variable

==============================
Now modifying global variable using 'global' inside inner function
==============================
Inside inner_function3 (modified global x): Modified GLOBAL variable
Inside outer_function3 (x still outer): Outer variable
After outer_function3, global x is now: Modified GLOBAL variable

==============================
Same function name for outer and inner (shadowing example)
==============================
This is outer func()
This is inner func()
'''