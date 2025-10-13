# ============================================================
# CHAPTER 11 – DICTIONARIES  (Let Us Python)
# SECTION A: Concepts, Examples & Demonstrations
# ============================================================

# ------------------------------------------------------------
# What are Dictionaries?
# ------------------------------------------------------------
# Dictionary = collection of key–value pairs, enclosed in { }.
# Also called associative arrays or maps.

d1 = {}  # empty dictionary
d2 = {'A101': 'Amol', 'A102': 'Anil', 'B103': 'Ravi'}
print("Dictionary d2:", d2)

# Keys must be unique; values may repeat.
d = {10: 'A', 20: 'A', 30: 'Z'}
print("Different keys, same values:", d)

# If same key repeats, last value overrides previous one.
d = {10: 'A', 20: 'B', 10: 'Z'}
print("Duplicate key -> latest stored:", d)

# ------------------------------------------------------------
# Accessing Dictionary Elements
# ------------------------------------------------------------
d = {'A101': 'Dinesh', 'A102': 'Shrikant', 'B103': 'Sudhir'}
print("\nEntire dictionary:", d)
print("Access element with key 'A102':", d['A102'])
# Note: Dictionaries are key-indexed, not position-indexed.

# ------------------------------------------------------------
# Looping in Dictionaries
# ------------------------------------------------------------
courses = {'DAA': 'CS', 'AOA': 'ME', 'SVY': 'CE'}
print("\nIterate over key-value pairs:")
for k, v in courses.items():
    print(k, v)

print("Iterate over keys:")
for k in courses:
    print(k)

print("Iterate over values:")
for v in courses.values():
    print(v)

print("Enumerate items with index:")
for i, (k, v) in enumerate(courses.items()):
    print(i, k, v)

# ------------------------------------------------------------
# Basic Dictionary Operations
# ------------------------------------------------------------
courses = {
    'CS101': 'CPP', 'CS102': 'DS', 'CS201': 'OOP',
    'CS226': 'DAA', 'CS601': 'Crypt', 'CS442': 'Web'
}
print("\nOriginal courses:", courses)

courses['CS444'] = 'Web Services'         # add
courses['CS201'] = 'OOP using Java'       # modify
del courses['CS102']                      # delete a key–value pair
print("After modifications:", courses)

# ------------------------------------------------------------
# Using Built-in Functions
# ------------------------------------------------------------
d = {'CS101': 'CPP', 'CS102': 'DS', 'CS201': 'OOP'}
print("\nBuilt-in functions:")
print("len(d)  ->", len(d))
print("max(d)  ->", max(d))
print("min(d)  ->", min(d))
print("sorted(d) ->", sorted(d))

num_keys = {1: 'A', 2: 'B', 3: 'C'}
print("sum(num_keys) ->", sum(num_keys))
print("any(num_keys) ->", any(num_keys))
print("all(num_keys) ->", all(num_keys))

print("Reverse iteration:")
for k, v in reversed(list(d.items())):
    print(k, v)

# ------------------------------------------------------------
# Dictionary Methods
# ------------------------------------------------------------
c = {'CS101': 'CPP', 'CS102': 'DS', 'CS201': 'OOP'}
d2 = {'ME126': 'HPE', 'ME102': 'TOM', 'ME234': 'AEM'}

print("\nDictionary methods demonstration:")
print("c.get('CS102') ->", c.get('CS102', 'Absent'))
print("c.get('EE102') ->", c.get('EE102', 'Absent'))

c.update(d2)
print("After update:", c)
print("popitem() ->", c.popitem())
print("pop('CS102') ->", c.pop('CS102', 'Not found'))
c.clear()
print("After clear():", c)

# ------------------------------------------------------------
# Dictionary Varieties
# ------------------------------------------------------------
print("\nDictionary Varieties:")
# Keys can be numbers, strings, or tuples (tuples must be immutable).
d = {(1, 5): 'ME126', (3, 2): 'ME102'}
print(d)

# Nested dictionaries
contacts = {
    'Anil': {'DOB': '17/11/98', 'Favorite': 'Igloo'},
    'Amol': {'DOB': '14/10/99', 'Favorite': 'Tundra'},
    'Ravi': {'DOB': '19/11/97', 'Favorite': 'Arctic'}
}
print(contacts)

# Merging via unpacking
animals = {'Tiger': 141, 'Lion': 152}
birds = {'Eagle': 38, 'Crow': 3, 'Parrot': 2}
combined = {**animals, **birds}
print("Combined:", combined)

# fromkeys example
lst = [12, 13, 14, 15, 16]
d = dict.fromkeys(lst, 25)
print("fromkeys ->", d)

print("\n--- End of Section A ---")
