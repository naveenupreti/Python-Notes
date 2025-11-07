'''

| Operation / Feature |     **List**     |    **Tuple**    |         **Dictionary**         |
| ------------------- | :--------------: | :-------------: | :----------------------------: |
| Concatenation (+)   |      ✅ Works     |     ✅ Works     |         ❌ Not supported        |
| Merging             | ✅ Works (extend) | ✅ Works (via +) | ✅ Works via update / unpacking |
| Conversion          |      ✅ Works     |     ✅ Works     |             ✅ Works            |
| Aliasing            |      ✅ Works     |     ✅ Works     |             ✅ Works            |
| Cloning             |      ✅ Works     |     ✅ Works     |             ✅ Works            |
| Searching (`in`)    |      ✅ Works     |     ✅ Works     |        ✅ Works (on keys)       |
| Identity (`is`)     |      ✅ Works     |     ✅ Works     |             ✅ Works            |
| Comparison (<, >)   |      ✅ Works     |     ✅ Works     |         ❌ Not supported        |
| Emptiness (`not`)   |      ✅ Works     |     ✅ Works     |             ✅ Works            |
| Mutability          |     ✅ Mutable    |   ❌ Immutable   |            ✅ Mutable           |
| Change key in place |        N/A       |       N/A       |         ❌ Not possible         |

'''
# ============================================================
# Program: Dictionary Operations Demonstration
# Purpose: To show which list/tuple operations work on dictionaries
# ============================================================

# --- Part 1: Dictionary Keys Cannot Be Changed In Place ---
print("=== DICTIONARY KEYS CANNOT BE CHANGED IN PLACE ===")

# Create a dictionary
person = {"name": "Naveen", "age": 50}
print("Original dictionary:", person)    # {'name': 'Naveen', 'age': 50}

# Trying to modify a key directly (Not allowed)
print("\nTrying to change key 'name' to 'fullname' directly...")
try:
    list(person.keys())[0] = "fullname"  # ❌ Invalid operation
except TypeError as e:
    print("Output:", e)                  # Output: 'dict_keys' object does not support item assignment

# Correct way: remove old key and add a new one
print("\n✅ Correct Way (using pop and new key):")
person["fullname"] = person.pop("name")
print("Modified dictionary:", person)     # {'age': 50, 'fullname': 'Naveen'}

# --- Separator ---
print("\n" + "="*80)
print("Now testing various LIST/TUPLE operations on DICTIONARIES")
print("="*80)

# Create two sample dictionaries
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}

# --- 1️⃣ Concatenation ---
print("\n1️⃣ Concatenation (+ operator)")
print("# Trying to use '+' like with lists or tuples")
try:
    result = d1 + d2
except TypeError as e:
    print("Output:", e)  # unsupported operand type(s) for +: 'dict' and 'dict'
print("❌ Concatenation doesn't work on dictionaries")

# --- 2️⃣ Merging ---
print("\n2️⃣ Merging")
print("# '+' fails but we can merge dictionaries using update() or ** unpacking")
try:
    merged = d1 + d2
except TypeError as e:
    print("Output:", e)
print("✅ Merging using {**d1, **d2} works:", {**d1, **d2})  # {'a':1,'b':2,'c':3,'d':4}

# --- 3️⃣ Conversion ---
print("\n3️⃣ Conversion Works")
print("# We can convert dictionary views into lists or tuples")
print("list(d1.keys())  ->", list(d1.keys()))      # ['a', 'b']
print("list(d1.values()) ->", list(d1.values()))   # [1, 2]
print("list(d1.items())  ->", list(d1.items()))    # [('a', 1), ('b', 2)]
print("✅ Conversion to list/tuple works correctly")

# --- 4️⃣ Aliasing ---
print("\n4️⃣ Aliasing (Two names for same object)")
print("# Assigning alias = d1 creates a new name for same dictionary")
alias = d1
alias["x"] = 99
print("alias:", alias)   # {'a': 1, 'b': 2, 'x': 99}
print("d1:", d1)         # {'a': 1, 'b': 2, 'x': 99}
print("✅ Aliasing works — both refer to same memory location")

# --- 5️⃣ Cloning ---
print("\n5️⃣ Cloning (Independent copy)")
print("# copy() creates a new independent dictionary")
clone = d1.copy()
clone["y"] = 100
print("clone:", clone)   # {'a':1, 'b':2, 'x':99, 'y':100}
print("d1:", d1)         # {'a':1, 'b':2, 'x':99}
print("✅ Cloning works — clone is a separate object")

# --- 6️⃣ Searching ---
print("\n6️⃣ Searching Keys")
print("# The 'in' operator checks whether a key exists in dictionary")
print("'a' in d1 ->", 'a' in d1)     # True
print("'z' in d1 ->", 'z' in d1)     # False
print("✅ Searching by key works fine")

# --- 7️⃣ Identity ---
print("\n7️⃣ Identity")
print("# 'is' checks if two variables refer to the same object")
print("d1 is alias ->", d1 is alias)  # True
print("d1 is clone ->", d1 is clone)  # False
print("✅ Identity check works using 'is' operator")

# --- 8️⃣ Comparison ---
print("\n8️⃣ Comparison")
print("# Equality (==) works but <, > do not work for dictionaries")
d3 = {"a": 1, "b": 2, "x": 99}
print("d1 == d3 ->", d1 == d3)       # True
try:
    print("d1 < d2 ->", d1 < d2)
except TypeError as e:
    print("Output:", e)               # '<' not supported between instances of 'dict' and 'dict'
print("✅ Only equality/inequality works; <, > don't work")

# --- 9️⃣ Emptiness ---
print("\n9️⃣ Emptiness")
print("# Empty dictionary evaluates to False; non-empty to True")
empty_dict = {}
print("not empty_dict ->", not empty_dict)  # True
print("not d1 ->", not d1)                  # False
print("✅ Emptiness check works using 'not dict'")

# --- Final Summary ---
print("\n" + "="*80)
print("🎯 SUMMARY OF OPERATIONS ON DICTIONARIES")
print("- Keys change in place: ❌")
print("- Concatenation (+): ❌")
print("- Merging (update or **): ✅")
print("- Conversion (to list/tuple): ✅")
print("- Aliasing: ✅")
print("- Cloning: ✅")
print("- Searching (in): ✅")
print("- Identity (is): ✅")
print("- Comparison (<,>): ❌")
print("- Emptiness (not): ✅")
print("="*80)

