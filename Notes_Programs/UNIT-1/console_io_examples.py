# console_io_examples.py
# Demonstration of Console Input/Output in Python

# -------------------------------
# Console Input
# -------------------------------

# Basic input
name = input('Enter full name: ')
print(f'Full name entered: {name}')

# Splitting full name into first, middle, and last
fname, mname, sname = input('Enter full name (first middle last): ').split()
print(f'First Name: {fname}, Middle Name: {mname}, Surname: {sname}')

# Receiving multiple integer values
n1, n2, n3 = input('Enter three integers: ').split()
n1, n2, n3 = int(n1), int(n2), int(n3)
print(n1 + 10, n2 + 20, n3 + 30)

# Compact version using list comprehension
n1, n2, n3 = [int(n) for n in input('Enter three integers: ').split()]
print(n1 + 10, n2 + 20, n3 + 30)

# Arbitrary number of integers
numbers = [int(x) for x in input('Enter values separated by space: ').split()]
for n in numbers:
    print(n + 10)

# Receiving different types of values
data = input('Enter name, age, salary: ').split()
name = data[0]
age = int(data[1])
salary = float(data[2])
print(f'Name: {name}, Age: {age}, Salary: {salary}')

# -------------------------------
# Console Output
# -------------------------------
a, b, c = 10, 20, 30
x, y = 5, 15

# Basic print with sep and end
print(a, b, c, sep=',', end='!\n')  # prints ',' after each value, '!' at end
print(x, y, sep='...', end='#\n')   # prints '...' after each value, '#' at end

# -------------------------------
# Formatted Printing
# -------------------------------

# Using f-strings
r, l, b = 1.5678, 10.5, 12.66
print(f'radius = {r}')
print(f'length = {l} breadth = {b} radius = {r}')

name = 'Sushant Ajay Raje'
for n in name.split():
    print(f'{n:10}')  # print in 10 columns

# Using format() method
name, age, salary = 'Rakshita', 30, 53000.55
print('radius = {} length = {} breadth ={}'.format(r, l, b))
print('name = {} age = {} salary = {}'.format(name, age, salary))
print('radius = {2} length = {1} breadth ={0}'.format(r, l, b))
print('age={1} salary={2} name={0}'.format(name, age, salary))
print('name = {0:15} salary = {1:10}'.format(name, salary))
print('radius = {0:10.2f}'.format(r))

# -------------------------------
# Problem 7.1
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
# Problem 7.2
# -------------------------------
start, end, step = input('Enter start, end, step values: ').split()
# Right aligned printing
for n in range(int(start), int(end), int(step)):
    print(f'{n:>5}{n**2:>7}{n**3:>8}')
print()
# Left aligned printing
for n in range(int(start), int(end), int(step)):
    print('{0:<5}{1:<7}{2:<8}'.format(n, n**2, n**3))

# -------------------------------
# Problem 7.3 - Contacts Table
# -------------------------------
contacts = {
    'Dilip': 9823077892,
    'Shekhar': 6784512345,
    'Vivek': 9823011245,
    'Riddhi': 9766556779
}
for name, cellno in contacts.items():
    print(f'{name:15} : {cellno:10d}')

# -------------------------------
# Problem 7.4 - Multiple fstrings
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
# Problem 7.5 - Square and Cube Roots
# -------------------------------
import math
width = 10
precision = 4
for n in range(1, 10):
    s = math.sqrt(n)
    c = math.pow(n, 1/3)
    print(f'{n:^5}{s:{width}.{precision}}{c:{width}.{precision}}')
