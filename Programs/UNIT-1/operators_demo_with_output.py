   # operators_demo_with_output.py

"""
Python Operators Demo with Actual Values and Inline Comments
-----------------------------------------------------------
Demonstrates all 7 operator categories with actual results and logic explanation.

"""

# -----------------------------
# 1. ARITHMETIC OPERATORS
# -----------------------------
print("=== 1. ARITHMETIC OPERATORS ===")

a, b, c, d = 7, 3, -2, 0

print(f"{a} + {b} = {a + b}")   # 7+3=10
print(f"{a} - {b} = {a - b}")   # 7-3=4
print(f"{a} * {b} = {a * b}")   # 7*3=21
print(f"{a} / {b} = {a / b}")   # 7/3=2.3333333333333335 (float division)
print(f"{a} // {b} = {a // b}") # 7//3=2 (floor division. a//b=floor(a/b))
print(f"{a} % {b} = {a % b}")   # 7%3=1 (remainder. sign same as divisor (a = (a//b)*b + (a%b))
print(f"{a} ** {b} = {a ** b}") # 7**3=343 (7^3)

# Edge cases
print(f"{a} / {c} = {a / c}")   # 7/-2=-3.5
print(f"{c} // {b} = {c // b}") # -2//3=-1 (floor division rounds towards negative infinity)
print(f"{c} % {b} = {c % b}")   # -2%3=1 (Python modulo always has same sign as divisor)
print(f"7.5 % 2.3 = {7.5 % 2.3}") # 7.5%2.3=0.6 (a = (a//b)*b + (a%b))

'''
a = (a//b)*b + a%b
a%b = a - (a//b)*b
a%b = a - floor(a/b)*b
7.5 % 2.3 = 7.5 - floor(7.5 / 2.3) * 2.3
 =7.5 - floor(3.26) * 2.3
 =7.5 - 3.0 * 2.3
 =7.5 - 6.9 = 0.6

In case of -2%3,a=-2,b=3
-2/3= -0.66
-2//3 = -1 (floor(-0.66))
-2%3 = -2 - (-1)*3
 = 1

'''
try:
    print(f"{a} / {d} = {a / d}")
except ZeroDivisionError as e:
    print("Division by zero error:", e) # division by zero raises exception

print("\n")

# -----------------------------
# 2. COMPARISON OPERATORS
# -----------------------------
print("=== 2. COMPARISON OPERATORS ===")

print(f"{a} == {b} -> {a == b}")   # 7==3 False
print(f"{a} != {b} -> {a != b}")   # 7!=3 True
print(f"{a} > {b} -> {a > b}")     # 7>3 True
print(f"{a} < {b} -> {a < b}")     # 7<3 False
print(f"{a} >= {b} -> {a >= b}")   # 7>=3 True
print(f"{a} <= {b} -> {a <= b}")   # 7<=3 False

# Edge cases
print(f"7 == 7.0 -> {7 == 7.0}")   # True (int==float)
print(f"7 == '7' -> {7 == '7'}")   # False (int != str)
print(f"1 < 2 < 3 -> {1 < 2 < 3}") # True (chained comparison)

print("\n")

# -----------------------------
# 3. LOGICAL OPERATORS
# -----------------------------
print("=== 3. LOGICAL OPERATORS ===")

x, y = True, False

print(f"{x} and {y} -> {x and y}") # True and False = False
print(f"{x} or {y} -> {x or y}")   # True or False = True
print(f"not {x} -> {not x}")       # not True = False

# Short-circuit examples
def side_effect(val):
    print(f"Function called with {val}")
    return val

print("Short-circuit AND example:")
result_and = side_effect(False) and side_effect(True)
print("Result:", result_and)  # False, second function not called

print("Short-circuit OR example:")
result_or = side_effect(True) or side_effect(False)
print("Result:", result_or)   # True, second function not called

print("\n")

# -----------------------------
# 4. BITWISE OPERATORS
# -----------------------------
print("=== 4. BITWISE OPERATORS ===")

p, q = 6, 3 # 0b110 & 0b011

print(f"{p} & {q} = {p & q}")   # 6&3=2 (0b110 & 0b011 = 0b010)
print(f"{p} | {q} = {p | q}")   # 6|3=7 (0b110 | 0b011 = 0b111)
print(f"{p} ^ {q} = {p ^ q}")   # 6^3=5 (0b110 ^ 0b011 = 0b101)
print(f"~{p} = {~p}")           # ~6=-7 (Use formula: ~x = -x - 1)
print(f"{p} << 2 = {p << 2}")   # 6<<2=24 (shift left. x<<n means multiply by 2**n)
print(f"{p} >> 1 = {p >> 1}")   # 6>>1=3 (shift right. x>>n means divide by 2**n)

# Negative number behavior
n = -6
print(f"~{n} = {~n}")           # ~-6=5
print(f"{n} >> 1 = {n >> 1}")   # -6>>1=-3

print("\n")

# -----------------------------
# 5. ASSIGNMENT OPERATORS
# -----------------------------
print("=== 5. ASSIGNMENT OPERATORS ===")

x = 5 # integer for safe bitwise operations
print(f"Initial x = {x}")

# Arithmetic assignments
x += 3
print(f"x += 3 -> {x}")  # 5+3=8
x -= 2
print(f"x -= 2 -> {x}")  # 8-2=6
x *= 4
print(f"x *= 4 -> {x}")  # 6*4=24
x //= 3
print(f"x //= 3 -> {x}") # 24//3=8
x %= 5
print(f"x %= 5 -> {x}")  # 8%5=3
x **= 2
print(f"x **= 2 -> {x}") # 3**2=9

# Bitwise assignments
x &= 7
print(f"x &= 7 -> {x}")  # 9&7=1
x |= 2
print(f"x |= 2 -> {x}")  # 1|2=3
x ^= 5
print(f"x ^= 5 -> {x}")  # 3^5=6
x <<= 1
print(f"x <<= 1 -> {x}") # 6<<1=12
x >>= 2
print(f"x >>= 2 -> {x}") # 12>>2=3

print("\n")

# -----------------------------
# 6. IDENTITY OPERATORS
# -----------------------------
print("=== 6. IDENTITY OPERATORS ===")

m = [1,2,3]
n = m
o = [1,2,3]

print(f"m is n -> {m is n}")     # True, same object
print(f"m is o -> {m is o}")     # False, different object
print(f"m == o -> {m == o}")     # True, values equal
print(f"m is not n -> {m is not n}") # False
print(f"m is not o -> {m is not o}") # True

print("\n")

# -----------------------------
# 7. MEMBERSHIP OPERATORS
# -----------------------------
print("=== 7. MEMBERSHIP OPERATORS ===")

fruits = ["apple","banana","cherry"]
print(f"'apple' in {fruits} -> {'apple' in fruits}")   # True
print(f"'grape' not in {fruits} -> {'grape' not in fruits}") # True

text = "hello"
print(f"'e' in '{text}' -> {'e' in text}")             # True
print(f"'a' not in '{text}' -> {'a' not in text}")     # True

empty_list = []
print(f"1 in empty_list -> {1 in empty_list}")         # False
print(f"1 not in empty_list -> {1 not in empty_list}") # True

print("\n=== End of Operators Demo ===")
