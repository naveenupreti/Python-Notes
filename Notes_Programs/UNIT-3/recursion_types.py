'''
Recursion is a method of solving a big problem by solving
smaller versions of the SAME problem.

Recursion invloves breaking down a problem into smaller pieces of
the same type to the point that it cannot be further broken down.

Recursion is a programming technique where a function
calls itself directly or indirectly to solve a problem.

Recursion means a function calling itself directly or
indirectly until a base condition is met.

Each recursive call creates a new copy of the function
on the call stack.
So a recursive function must always have a base case to
stop infinite
recursion.

Every recursive function must have:

Base Case – the stopping condition (to prevent infinite recursion)

Recursive Case – the part where the function calls itself

General Syntax:

def function_name(parameters):
    if base_condition:
        return some_value        # base case
    else:
        return function_name(modified_parameters)  # recursive case
    
    
✅ Advantages of Recursion

Simplifies problems that can be divided into smaller similar problems.

Easier to read and implement for tasks like factorial, Fibonacci,
tree traversal.

Reduces use of loops and simplifies code logic.

Natural fit for divide and conquer algorithms (like Merge Sort, Quick Sort).

❌ Disadvantages of Recursion

Memory heavy – each recursive call adds a new frame to the call stack.

Slower due to repeated function calls.

Risk of RecursionError if base case is missing or too deep recursion.

Often, iterative solutions are faster and use less memory.

'''

# ==========================================================
# PYTHON PROGRAM — ALL TYPES OF RECURSION (With Trace Diagrams)
# ==========================================================
# ----------------------------------------------------------
# 1️⃣ DIRECT RECURSION
# ----------------------------------------------------------
# Function calls itself directly.
# Example: Factorial of a number

def factorial(n):
    """Direct Recursion Example"""
    if n == 0:                 # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive call

print("1️⃣ DIRECT RECURSION: Factorial Example")
print("Factorial of 5 =", factorial(5))
# Output: 120

# 🔁 TRACE DIAGRAM
# factorial(5)
# → 5 * factorial(4)
# → 5 * (4 * factorial(3))
# → 5 * (4 * (3 * factorial(2)))
# → 5 * (4 * (3 * (2 * factorial(1))))
# → 5 * (4 * (3 * (2 * (1 * factorial(0)))))
# → 5 * 4 * 3 * 2 * 1 = 120
print("-" * 60)


# ----------------------------------------------------------
# 2️⃣ INDIRECT RECURSION
# ----------------------------------------------------------
# Function A calls Function B, and Function B calls Function A.

def functionA(x):
    if x > 0:
        print("A:", x)
        functionB(x - 1)        # A calls B

def functionB(x):
    if x > 0:
        print("B:", x)
        functionA(x // 2)       # B calls A

print("2️⃣ INDIRECT RECURSION")
functionA(5)
# Output:
# A: 5
# B: 4
# A: 2
# B: 1

# 🔁 TRACE DIAGRAM
# functionA(5) → functionB(4)
# functionB(4) → functionA(2)
# functionA(2) → functionB(1)
# functionB(1) → functionA(0) → stop
print("-" * 60)


# ----------------------------------------------------------
# 3️⃣ TAIL RECURSION
# ----------------------------------------------------------
# The recursive call is the LAST operation.
# Work is done before the recursive call → Top-Down execution.

def tail_rec(n):
    if n == 0:
        return
    print(n, end=" ")           # work before recursion
    tail_rec(n - 1)             # recursive call last

print("3️⃣ TAIL RECURSION: Countdown Example")
tail_rec(5)
# Output: 5 4 3 2 1

# 🔁 TRACE DIAGRAM
# tail_rec(5) → print(5), call tail_rec(4)
# tail_rec(4) → print(4), call tail_rec(3)
# tail_rec(3) → print(3), call tail_rec(2)
# tail_rec(2) → print(2), call tail_rec(1)
# tail_rec(1) → print(1), call tail_rec(0)
# tail_rec(0) → stop
print("\n" + "-" * 60)


# ----------------------------------------------------------
# 4️⃣ HEAD RECURSION
# ----------------------------------------------------------
# The recursive call happens FIRST.
# Work is done after recursion returns → Bottom-Up execution.

def head_rec(n):
    if n == 0:
        return
    head_rec(n - 1)             # recursive call first
    print(n, end=" ")           # work after returning

print("4️⃣ HEAD RECURSION: Print 1 to N Example")
head_rec(5)
# Output: 1 2 3 4 5

# 🔁 TRACE DIAGRAM
# head_rec(5)
#   → head_rec(4)
#       → head_rec(3)
#           → head_rec(2)
#               → head_rec(1)
#                   → head_rec(0)
#                   ← print(1)
#               ← print(2)
#           ← print(3)
#       ← print(4)
#   ← print(5)
print("\n" + "-" * 60)


# ----------------------------------------------------------
# 5️⃣ TREE RECURSION
# ----------------------------------------------------------
# Function calls itself multiple times.
# Example: Fibonacci sequence.

def fibonacci(n):
    """Tree Recursion Example"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("5️⃣ TREE RECURSION: Fibonacci Series (0–5)")
for i in range(6):
    print(fibonacci(i), end=" ")
# Output: 0 1 1 2 3 5

# 🔁 TRACE DIAGRAM for fibonacci(4)
#           fib(4)
#          /      \
#      fib(3)     fib(2)
#     /     \     /    \
#  fib(2) fib(1) fib(1) fib(0)
#  /   \
# fib(1) fib(0)
print("\n" + "-" * 60)


# ----------------------------------------------------------
# 6️⃣ NESTED RECURSION
# ----------------------------------------------------------
# Function calls itself with another recursive call as argument.

def mcCarthy91(n):
    """Nested Recursion Example"""
    if n > 100:
        return n - 10
    else:
        return mcCarthy91(mcCarthy91(n + 11))  # recursion inside recursion

print("6️⃣ NESTED RECURSION: McCarthy 91 Function")
print("mcCarthy91(95) =", mcCarthy91(95))
print("mcCarthy91(200) =", mcCarthy91(200))

# Output: mcCarthy91(95) = 91
# Output: mcCarthy91(200) = 190
# 🔁 TRACE DIAGRAM
# mcCarthy91(95)
# → mcCarthy91(mcCarthy91(106))
# → mcCarthy91(96)
# → mcCarthy91(mcCarthy91(107)) → ... repeats
# Eventually returns 91 for all n ≤ 100

# mcCarthy91(99)
#  → mcCarthy91(mcCarthy91(110))
#       ↳ mcCarthy91(110) = 100
#  → mcCarthy91(100)
#       → mcCarthy91(mcCarthy91(111))
#            ↳ mcCarthy91(111) = 101
#       → mcCarthy91(101)
#            ↳ returns 91
#  ✅ returns 91

print("-" * 60)


# ----------------------------------------------------------
# 7️⃣ COMBINATION (INDIRECT + TREE RECURSION)
# ----------------------------------------------------------
# Function A calls B multiple times, and B calls A.

def A(n):
    if n > 0:
        print("A:", n)
        B(n - 1)
        B(n - 2)

def B(n):
    if n > 0:
        print("B:", n)
        A(n - 1)

print("7️⃣ COMBINED RECURSION (Indirect + Tree)")
A(3)
# Typical Output:
# A: 3
# B: 2
# A: 1
# B: 1
# (Order may vary slightly based on recursive call flow)

# 🔁 TRACE DIAGRAM
# 
#                                  A(3)
#                               ↙    ↘
#                            B(2)        B(1)
#                            |             |
#                           A(1)           A(0)
#                        ↙    ↘         ↩
#                       B(0)    B(-1)
#                      ↩       ↩
# 
# Return chain:
# B(0) → A(1) → B(2) → A(3)
# B(-1) → A(1) → B(2) → A(3)
# A(0) → B(1) → A(3)
# Key Takeaways
# 1. A(0) returns immediately → control goes back to B(1)
# 2. B(0) returns immediately → control goes back to A(1)
# 3. B(-1) returns immediately → also back to A(1)
# 4. Each caller continues with its next statement.
# 5. If no code remains, it returns to its caller.
print("-" * 60)


# END OF PROGRAM

