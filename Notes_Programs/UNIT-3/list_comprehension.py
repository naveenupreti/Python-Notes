'''
What is a list comprehension?

A list comprehension is a compact way to create a list in Python using a single line of code, instead of writing multiple lines with loops.

General form:

[ expression for item in iterable if condition ]


expression → what each item in the new list should be

item in iterable → loops over each element in the original collection

if condition → optional, filters elements
'''

Simple Example 1: Squares of numbers

Instead of writing:

squares = []
for x in range(5):
    squares.append(x**2)
print(squares)


We can use list comprehension:

squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]


✅ One line does the same thing as three lines with a loop.

Simple Example 2: Even numbers

Using a normal loop:

evens = []
for x in range(10):
    if x % 2 == 0:
        evens.append(x)
print(evens)  # Output: [0, 2, 4, 6, 8]


With list comprehension:

evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]


💡 Key idea:
List comprehension is just a shortcut to create lists in a clean, readable way.