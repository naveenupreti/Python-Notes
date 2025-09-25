# console_io_exercises.py
# Ready-to-run solutions for Console Input/Output exercises

import math

# -------------------------------
# Problem 7.1: Circle and Rectangle
# -------------------------------
r, l, b = input('Enter radius, length and breadth: ').split()
radius = int(r)
length = int(l)
breadth = int(b)
circumference = 2 * 3.14 * radius
perimeter = 2 * (length + breadth)
print(f'Circumference of circle: {circumference}')
print(f'Perimeter of rectangle: {perimeter}')

# -------------------------------
# Problem 7.2: Numbers, Squares and Cubes
# -------------------------------
start, end, step = input('Enter start, end, step values: ').split()
start, end, step = int(start), int(end), int(step)

print("\nRight-aligned:")
for n in range(start, end, step):
    print(f'{n:>5}{n**2:>7}{n**3:>8}')

print("\nLeft-aligned:")
for n in range(start, end, step):
    print(f'{n:<5}{n**2:<7}{n**3:<8}')

# -------------------------------
# Problem 7.3: Contacts Table
# -------------------------------
contacts = {
    'Dilip': 9823077892,
    'Shekhar': 6784512345,
    'Vivek': 9823011245,
    'Riddhi': 9766556779
}
print("\nContacts Table:")
for name, cellno in contacts.items():
    print(f'{name:15} : {cellno:10d}')

# -------------------------------
# Problem 7.4: Multiple fstrings alignment
# -------------------------------
min_val, max_val = 25, 75
mean = 35
sd = 0.56
var = 0.9
print(
    f'\n{"Max Value:":<15}{max_val:>10}',
    f'\n{"Min Value:":<15}{min_val:>10}',
    f'\n{"Mean:":<15}{mean:>10}',
    f'\n{"Std Dev:":<15}{sd:>10}',
    f'\n{"Variance:":<15}{var:>10}'
)

# -------------------------------
# Problem 7.5: Square root and Cube root (formatted)
# -------------------------------
width = 10
precision = 3
print("\nNumber | Sqrt | Cube Root")
for n in range(1, 11):
    sqrt_val = math.sqrt(n)
    cube_val = n ** (1/3)
    print(f'{n:^5}{sqrt_val:{width}.{precision}}{cube_val:{width}.{precision}}')

# -------------------------------
# Exercise A
# -------------------------------

# (a) Compact input for 3 ages
ages = [int(input(f'Enter age of person {i+1}: ')) for i in range(3)]
print("Ages entered:", ages)

# (b) Print on same line
print("Rendezvous", end='')  # cursor stays on same line

# (c) Output with f-string
l, b = 1.5678, 10.5
print(f'\nlength = {l} breadth = {b}')

# (d) Right-alignment
n = 7
print(f'{n:>5}{n**2:>7}{n**3:>8}')  # >5, >7, >8 = column width

# (e) Name and cell number formatting
name, cellno = 'Sanjay', 9823017892
print(f'{name:15} : {cellno:10}')

# (f) Using f-string for multiple variables
x, y, z = 10, 20, 40
print(f'{x:<5}{y:<7}{z:<8}')

# (g) Arbitrary floats input
float_numbers = [float(x) for x in input('Enter floats: ').split()]
print("Floats received:", float_numbers)

# (h) f-string formatting example
x, y = 14.99, 114.39
print(f'x = {x:>6}\ny = {y:>6}')

# (i) Receive boolean input
bool_val = input('Enter True/False: ')
bool_val = bool_val.strip().lower() == 'true'
print('Boolean received:', bool_val)

# (j) Receive complex number
comp_val = complex(input('Enter complex number (a+bj): '))
print('Complex number:', comp_val)

# (k) Display price in 10 columns, 4 decimals
price = 1.5567894
print(f'Price: {price:10.4f}')

# (l) Average of arbitrary floats
numbers = [float(x) for x in input('Enter floats: ').split()]
average = sum(numbers) / len(numbers) if numbers else 0
print('Average:', average)

# (m) Agreement deduction
name = input('Enter name: ')
years = float(input('Enter years of service: '))
bonus = float(input('Enter Diwali bonus received: '))
deduction = 2 * years + bonus * 5.5 / 100
print(f'Agreement deduction for {name}: {deduction}')

# (n) input() and print() are built-ins, no import needed

# (o) Invalid expression demonstration
# print('Result = ' + 4 > 3) # This will error

# (p) Print multiple values
a, b, c, d, e = 12.34, 234.39, 444.34, 1.23, 34.67
print(f'a = {a}\nb = {b}\nc = {c}\nd = {d}\ne = {e}')

# -------------------------------
# Exercise B - Matching pairs
# -------------------------------
matches = {
    "Default sep in print()": "' '",
    "Default end in print()": "\\n",
    "Easiest way to print output": "Using fstring",
    "Return type of split()": "list",
    "print('{num:>5}')": "Right justify num in 5 columns",
    "print('{num:<5}')": "Left justify num in 5 columns"
}

print("\nMatching Pairs:")
for k, v in matches.items():
    print(f'{k:<30} --> {v}')
