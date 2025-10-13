# ============================================================
#  CHAPTER 11 – DICTIONARIES   (Let Us Python)
# ============================================================
# Covers all examples, problems (11.1–11.8), Section B and Section C
# ============================================================

import operator

# ------------------------------------------------------------
# 1. BASIC CONCEPTS
# ------------------------------------------------------------

print("\n# --- Basic Dictionary Concepts ---")

# Empty and filled dictionaries
d1 = {}
d2 = {'A101': 'Amol', 'A102': 'Anil', 'B103': 'Ravi'}
print("Dictionary d2:", d2)

# Duplicate keys: last assignment wins
d3 = {10: 'A', 20: 'B', 10: 'Z'}
print("Duplicate keys example:", d3)

# Accessing elements
d = {'A101': 'Dinesh', 'A102': 'Shrikant', 'B103': 'Sudhir'}
print("Access using key:", d['A102'])

# Looping in dictionaries
courses = {'DAA': 'CS', 'AOA': 'ME', 'SVY': 'CE'}
print("\nIterating over key–value pairs:")
for k, v in courses.items():
    print(k, v)

# Enumerate with index
print("Enumerating dictionary items:")
for i, (k, v) in enumerate(courses.items()):
    print(i, k, v)

# Basic operations
courses = {
    'CS101': 'CPP', 'CS102': 'DS', 'CS201': 'OOP',
    'CS226': 'DAA', 'CS601': 'Crypt', 'CS442': 'Web'
}
courses['CS444'] = 'Web Services'
courses['CS201'] = 'OOP using Java'
del courses['CS102']
print("Modified dictionary:", courses)

# Built-in functions
d = {'CS101': 'CPP', 'CS102': 'DS', 'CS201': 'OOP'}
print("\nBuilt-in functions:")
print("len:", len(d))
print("max key:", max(d))
print("min key:", min(d))
print("sorted:", sorted(d))

# Reverse iteration
for k, v in reversed(list(d.items())):
    print("Reversed:", k, v)

# Methods
c = {'CS101': 'CPP', 'CS102': 'DS', 'CS201': 'OOP'}
d2 = {'ME126': 'HPE', 'ME102': 'TOM'}
print(c.get('CS102', 'Absent'))
print(c.get('EE102', 'Absent'))
c.update(d2)
print("After update:", c)
print("popitem():", c.popitem())
print("pop('CS102'):", c.pop('CS102', 'Not found'))
c.clear()
print("After clear:", c)

# Varieties
print("\nDictionary varieties:")
d = {(1, 5): 'ME126', (3, 2): 'ME102'}
print(d)
contacts = {
    'Anil': {'DOB': '17/11/98', 'Favorite': 'Igloo'},
    'Amol': {'DOB': '14/10/99', 'Favorite': 'Tundra'},
}
print(contacts)
animals = {'Tiger': 141, 'Lion': 152}
birds = {'Eagle': 38, 'Crow': 3}
combined = {**animals, **birds}
print("Merged:", combined)

lst = [12, 13, 14, 15, 16]
d = dict.fromkeys(lst, 25)
print("fromkeys:", d)

# ============================================================
#  PROBLEMS 11.1 – 11.8
# ============================================================

print("\n# --- Chapter Problems ---")

# Problem 11.1
students = {'Anil': 23, 'Sanjay': 28, 'Ajay': 25}
stud = students
students = {}
print("Problem 11.1:", stud)

# Problem 11.2
lst = ['Sunil', 'Sachin', 'Rahul', 'Kapil', 'Sunil', 'Rahul']
d = dict.fromkeys(lst, 50)
print("\nProblem 11.2 ->", d)

# Problem 11.3
d = {'Oil': 230, 'Clip': 150, 'Stud': 175, 'Nut': 35}
print("\nProblem 11.3 -> Sorting by key/value")
print("Asc by key:", sorted(d.items()))
print("Desc by key:", sorted(d.items(), reverse=True))
print("Asc by value:", sorted(d.items(), key=operator.itemgetter(1)))
print("Desc by value:", sorted(d.items(), key=operator.itemgetter(1), reverse=True))

# Problem 11.4
d1 = {'Mango': 30, 'Guava': 20}
d2 = {'Apple': 70, 'Pineapple': 50}
d3 = {'Kiwi': 90, 'Banana': 35}
d4 = {}
for d in (d1, d2, d3):
    d4.update(d)
print("\nProblem 11.4 ->", d4)
d5 = {**d1, **d2, **d3}
print(d5)
d6 = list({*d1, *d2, *d3})
print("Keys list:", d6)

# Problem 11.5
print("\nProblem 11.5 -> Empty or not")
d1 = {'Anil': 45}
print("Non-empty:", bool(d1))
d2 = {}
print("Empty:", not bool(d2))

# Problem 11.6
print("\nProblem 11.6 -> Merge two dictionaries")
boys = {'Nilesh': 41, 'Soumitra': 42, 'Nadeem': 47}
girls = {'Rasika': 38, 'Rajashree': 43, 'Rasika': 45}
print({**boys, **girls})
print({**girls, **boys})

# Problem 11.7
print("\nProblem 11.7 -> Max/Min salary")
d = {
    'anuj': {'salary': 10000, 'age': 20},
    'aditya': {'salary': 6000, 'age': 26},
    'rahul': {'salary': 7000, 'age': 26}
}
sal = [v['salary'] for v in d.values()]
print("Max:", max(sal), "Min:", min(sal))

# Problem 11.8
print("\nProblem 11.8 -> Congratulate student")
students = {554: 'Ajay', 350: 'Ramesh', 395: 'Rakesh'}
# Uncomment next lines to test interactively
# rollno = int(input("Enter roll number: "))
# name = students.get(rollno, 'Student')
# print(f"Congratulations {name}!")

# ============================================================
#  SECTION B – APPLICATION PROGRAMS
# ============================================================

print("\n# --- Section B Programs ---")

# (a) Character frequency & histogram
def char_frequency_histogram(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    for k, v in freq.items():
        print(f"{k}: {'*' * v}")

# Example:
# char_frequency_histogram("banana")

# (b) Students total & average marks
def total_average_marks(data):
    total_avg = {}
    for name, marks in data.items():
        total = sum(marks)
        avg = total / len(marks)
        total_avg[name] = {'Total': total, 'Average': avg}
    topper = max(total_avg.items(), key=lambda x: x[1]['Total'])[0]
    print("Topper:", topper)
    return total_avg

# (c) Portfolio manipulation
def portfolio_operations():
    portfolio = {
        'accounts': ['SBI', 'IOB'],
        'shares': ['HDFC', 'ICICI', 'TM', 'TCS'],
        'ornaments': ['10 gm gold', '1 kg silver']
    }
    portfolio['MF'] = ['Reliance', 'ABSL']
    portfolio['accounts'] = ['Axis', 'BOB']
    portfolio['shares'].sort()
    del portfolio['ornaments']
    print("Updated portfolio:", portfolio)

# (d) Grocery billing
def grocery_bill(prices, qty):
    total = 0
    for item in prices:
        total += prices[item] * qty.get(item, 0)
    return total

# (f) User login check
def login_check(users, uname, passwd):
    if users.get(uname) == passwd:
        print("Login successful!")
    else:
        print("Invalid username or password.")

# (g) Marks nested dictionary operations
def marks_operations():
    marks = {
        'Subu': {'Maths': 88, 'Eng': 60, 'SSt': 95},
        'Amol': {'Maths': 78, 'Eng': 68, 'SSt': 89},
        'Raka': {'Maths': 56, 'Eng': 66, 'SSt': 77}
    }
    print("Amol English marks:", marks['Amol']['Eng'])
    marks['Raka']['Maths'] = 77
    sorted_marks = dict(sorted(marks.items()))
    print("Sorted by name:", sorted_marks)

# (h) Network interface dictionary
def network_info():
    net = {
        'eth0': {'IP': '1.1.1.1', 'status': 'up'},
        'eth1': {'IP': '2.2.2.2', 'status': 'up'},
        'wlan0': {'IP': '3.3.3.3', 'status': 'down'},
        'wlan1': {'IP': '4.4.4.4', 'status': 'up'}
    }
    up_interfaces = [i for i, v in net.items() if v['status'] == 'up']
    print("Total interfaces:", len(net))
    print("Up interfaces:", up_interfaces)
    net['usb0'] = {'IP': '5.5.5.5', 'status': 'up'}
    net['usb1'] = {'IP': '6.6.6.6', 'status': 'down'}
    return net

# (i) Reverse printing and deletion
def reverse_delete(d):
    for k, v in reversed(list(d.items())):
        print(k, v)
        d.pop(k)
    print("Final dictionary:", d)

# ============================================================
#  SECTION C – OBJECTIVE / SHORT ANSWERS
# ============================================================

print("\n# --- Section C Objective Answers ---")

# (a) Output prediction
d = {'Milk': 1, 'Soap': 2, 'Towel': 3, 'Shampoo': 4, 'Milk': 7}
print("Q(a) -> Access by numeric index not allowed. KeyError expected.")

# (b) Correct statements
print("Q(b) -> i and iii are correct.")

# (c) Empty structures
empty_list, empty_tuple, empty_set, empty_dict = [], (), set(), {}
print("Empty structures created.")

# (d) One-element structures
one_list, one_tuple, one_set, one_dict = [10], (10,), {10}, {'a': 10}
print("One-element structures created.")

# (e) Access Mango & Winter
d = {
    'd1': {'Fruitname': 'Mango', 'Season': 'Summer'},
    'd2': {'Fruitname': 'Orange', 'Season': 'Winter'}
}
print("Mango:", d['d1']['Fruitname'], "| Winter:", d['d2']['Season'])

# (f) Property table explanation – shown via comments
"""
str : Ordered, Immutable
list: Ordered, Mutable
tuple: Ordered, Immutable
set : Unordered, Mutable (no duplicates)
dict: Ordered (3.7+), Mutable, Key-indexed
"""

# (g) Common usage
"""
str  -> Text data
list -> Ordered collection
tuple -> Fixed collection
set -> Unique items
dict -> Key–value mapping
"""

print("\n# --- END OF CHAPTER 11 ---")
