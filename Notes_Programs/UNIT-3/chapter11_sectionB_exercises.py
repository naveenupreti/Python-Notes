# ============================================================
# CHAPTER 11 – DICTIONARIES  (Let Us Python)
# SECTION B: Exercises & Programming Problems
# ============================================================

import operator

# ------------------------------------------------------------
# Problem 11.1
# Create a dictionary called students containing names and ages.
# Copy it into stud. Empty the students dictionary so stud keeps data.
# ------------------------------------------------------------
students = {'Anil': 23, 'Sanjay': 28, 'Ajay': 25}
stud = students
students = {}
print("Problem 11.1 Solution ->", stud)

# ------------------------------------------------------------
# Problem 11.2
# Create a list of cricketers. Use this list to create a dictionary in which
# list values become keys and all values = 50.
# ------------------------------------------------------------
lst = ['Sunil', 'Sachin', 'Rahul', 'Kapil', 'Sunil', 'Rahul']
d = dict.fromkeys(lst, 50)
print("\nProblem 11.2 Solution ->", d)

# ------------------------------------------------------------
# Problem 11.3
# Write a program to sort a dictionary by key/value ascending/descending.
# ------------------------------------------------------------
d = {'Oil': 230, 'Clip': 150, 'Stud': 175, 'Nut': 35}
print("\nProblem 11.3: Sorted by key/value")
print("Asc key:", sorted(d.items()))
print("Desc key:", sorted(d.items(), reverse=True))
print("Asc value:", sorted(d.items(), key=operator.itemgetter(1)))
print("Desc value:", sorted(d.items(), key=operator.itemgetter(1), reverse=True))

# ------------------------------------------------------------
# Problem 11.4
# Create three dictionaries and concatenate them into a fourth one.
# ------------------------------------------------------------
d1 = {'Mango': 30, 'Guava': 20}
d2 = {'Apple': 70, 'Pineapple': 50}
d3 = {'Kiwi': 90, 'Banana': 35}
d4 = {}
for d in (d1, d2, d3):
    d4.update(d)
print("\nProblem 11.4 ->", d4)
d5 = {**d1, **d2, **d3}
print("Merged using unpacking:", d5)
d6 = list({*d1, *d2, *d3})
print("List of keys only:", d6)

# ------------------------------------------------------------
# Problem 11.5
# Check whether a dictionary is empty or not.
# ------------------------------------------------------------
d1 = {'Anil': 45, 'Amol': 32}
if bool(d1):
    print("\nProblem 11.5 -> Dictionary is not empty")
d2 = {}
if not bool(d2):
    print("Dictionary is empty")

# ------------------------------------------------------------
# Problem 11.6
# Merge two dictionaries boys & girls into a third one.
# ------------------------------------------------------------
boys = {'Nilesh': 41, 'Soumitra': 42, 'Nadeem': 47}
girls = {'Rasika': 38, 'Rajashree': 43, 'Rasika': 45}
combined1 = {**boys, **girls}
combined2 = {**girls, **boys}
print("\nProblem 11.6 ->", combined1, combined2)

# ------------------------------------------------------------
# Problem 11.7
# For given dictionary of employees, print max and min salary.
# ------------------------------------------------------------
d = {
    'anuj': {'salary': 10000, 'age': 20, 'height': 6},
    'aditya': {'salary': 6000, 'age': 26, 'height': 5.6},
    'rahul': {'salary': 7000, 'age': 26, 'height': 5.9}
}
salaries = [v['salary'] for v in d.values()]
print("\nProblem 11.7 -> Max salary:", max(salaries), "Min salary:", min(salaries))

# ------------------------------------------------------------
# Problem 11.8
# Suppose a dictionary contains roll numbers & names.
# Receive roll number, display congrats message using name.
# ------------------------------------------------------------
students = {554: 'Ajay', 350: 'Ramesh', 395: 'Rakesh'}
# For demo, simulate two lookups:
for rollno in [350, 450]:
    name = students.get(rollno, 'Student')
    print(f"Problem 11.8 -> Congratulations {name}!")

# ------------------------------------------------------------
# Additional Exercises from Section B (a – i)
# ------------------------------------------------------------

# (a) Character frequency & histogram
def char_frequency_histogram(s):
    """Reads string and prints histogram of character frequencies."""
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    for k, v in freq.items():
        print(f"{k}: {'*' * v}")

# (b) Students total & average marks
def total_average_marks(data):
    """Replace subject marks with total & average, print topper."""
    result = {}
    for name, marks in data.items():
        total = sum(marks)
        avg = total / len(marks)
        result[name] = {'Total': total, 'Average': avg}
    topper = max(result.items(), key=lambda x: x[1]['Total'])[0]
    print("Topper:", topper)
    return result

# (c) Portfolio operations
def portfolio_operations():
    """Perform additions, updates, sorting, deletion in portfolio dict."""
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
    """Compute total bill from two dictionaries of price & quantity."""
    return sum(prices[i] * qty.get(i, 0) for i in prices)

# (f) User login check
def login_check(users, uname, passwd):
    """Check username & password in dictionary."""
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
    print("Marks of Amol in English:", marks['Amol']['Eng'])
    marks['Raka']['Maths'] = 77
    sorted_dict = dict(sorted(marks.items()))
    print("Sorted by name:", sorted_dict)

# (h) Network interfaces dictionary
def network_info():
    net = {
        'eth0': {'IP': '1.1.1.1', 'status': 'up'},
        'eth1': {'IP': '2.2.2.2', 'status': 'up'},
        'wlan0': {'IP': '3.3.3.3', 'status': 'down'},
        'wlan1': {'IP': '4.4.4.4', 'status': 'up'}
    }
    given = 'eth0'
    print(f"Status of {given}:", net[given]['status'])
    ups = [(i, v['IP']) for i, v in net.items() if v['status'] == 'up']
    print("Interfaces UP:", ups)
    print("Total interfaces:", len(net))
    net['usb0'] = {'IP': '5.5.5.5', 'status': 'up'}
    net['usb1'] = {'IP': '6.6.6.6', 'status': 'down'}
    print("Updated interfaces:", net)

# (i) Reverse printing & deletion
def reverse_delete(d):
    """Print from last to first while deleting each item."""
    for k, v in reversed(list(d.items())):
        print(k, v)
        d.pop(k)
    print("After deletion:", d)

print("\n--- End of Section B ---")
