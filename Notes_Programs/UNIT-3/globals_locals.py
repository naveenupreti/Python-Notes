"""
What are globals() and locals()?
globals()

Returns a dictionary containing all global variables of the current module.

Global = variables defined outside functions, module-level definitions, imported modules, functions, classes.

locals()

Returns a dictionary containing local variables inside the current function, class method, loop, comprehension, etc.

Local = variables created inside a function or block.

✔ Both return live dictionaries → Changing them sometimes affects the namespace.

"""

print("\n=== EXAMPLE 1: Basic globals() ===")
a = 10
b = 20
print("globals:", {k: v for k, v in globals().items() if k in ['a', 'b']})

print("\n=== EXAMPLE 2: locals() inside a Function ===")
def demo():
    x = 5
    y = 7
    print("locals in demo():", locals())
demo()

print("\n=== EXAMPLE 3: Difference between globals() and locals() ===")
x = 100
def func():
    y = 200
    print("globals keys:", [k for k in globals().keys() if k in ['x', 'func']])
    print("locals keys:", locals().keys())
func()

print("\n=== EXAMPLE 4: locals() is read-only inside functions ===")
def f():
    x = 10
    locals()['x'] = 777
    print("x after modifying locals():", x)  # still 10
f()

print("\n=== EXAMPLE 5: globals() is mutable ===")
globals()['z'] = 99
print("z created dynamically:", z)

print("\n=== EXAMPLE 6: exec() with globals() ===")
code = "m = 250"
exec(code, globals())
print("Value of m:", m)

print("\n=== EXAMPLE 7: eval() with globals() ===")
a = 10
b = 20
expr = "a + b"
print("Result of eval(a + b):", eval(expr, globals()))

print("\n=== EXAMPLE 8: locals() inside class method ===")
class Test:
    def method(self):
        x = 55
        print("locals in method():", locals())

obj = Test()
obj.method()

print("\n=== EXAMPLE 9: locals() in loops ===")
for i in range(2):
    print("locals in loop:", locals().get('i'))

print("\n=== EXAMPLE 10: locals() in list comprehensions ===")
x = 100
lst = [locals().get('x') for _ in range(3)]
print("List:", lst)

print("\n=== EXAMPLE 11: Modifying globals() inside function ===")
x = 10
def update_global():
    globals()['x'] = 500
update_global()
print("Updated x:", x)

print("\n=== EXAMPLE 12: Debugging with locals() ===")
def debug_example():
    a = 5
    b = 10
    return locals()
print("locals returned:", debug_example())

print("\n=== EXAMPLE 13: Nested functions ===")
x = 100
def outer():
    y = 200
    def inner():
        z = 300
        print("inner locals:", locals())
    inner()
outer()

print("\n=== EXAMPLE 14: Dynamic globals creation in loop ===")
for i in range(1, 4):
    globals()[f"var{i}"] = i * 10
print(var1, var2, var3)

print("\n=== EXAMPLE 15: Returning locals snapshot ===")
def compute(a, b):
    c = a + b
    return locals()
print(compute(5, 6))

print("\n=== EXAMPLE 16: locals() at global level ===")
locals()['p'] = 777
print("p created using locals():", p)

print("\n=== EXAMPLE 17: Why modifying locals() in functions doesn't work ===")
def fail_modify():
    a = 10
    d = locals()
    d['a'] = 99
    print("a is still:", a)
fail_modify()

print("\n=== EXAMPLE 18: Using globals() for template rendering ===")
name = "Naveen"
score = 95
template = "Student: {name}, Score: {score}"
print(template.format(**globals()))

print("\n=== EXAMPLE 19: globals() for dependency injection ===")
db_url = "mysql://localhost"
def connect():
    print("Connecting to:", globals()['db_url'])
connect()

print("\n=== EXAMPLE 20: Dynamic math evaluator ===")
x = 7
y = 3
formula = "x**y + x*y"
print("Result:", eval(formula, globals()))
