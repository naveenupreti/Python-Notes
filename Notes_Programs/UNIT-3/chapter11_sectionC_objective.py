# ============================================================
# CHAPTER 11 – DICTIONARIES  (Let Us Python)
# SECTION C: Objective & Short-Answer Questions
# ============================================================

# (a) True / False explanations
"""
(a) Dictionary elements can be accessed using position index – False
(b) Dictionaries are immutable – False
(c) Insertion order is preserved – True (Python 3.7+)
(d) d[0] gives first key–value pair – False (no positional index)
(e) courses.clear() deletes all entries, not the object – True statement
(f) Nested dictionaries possible – True
(g) One key can map to multiple values – False (values may be lists)
"""

# (b) Output / prediction
"""
Q:  d = {'Milk':1,'Soap':2,'Towel':3,'Shampoo':4,'Milk':7}
    print(d[0], d[1], d[2])
A:  Error – keys are strings; 0/1/2 invalid.  Duplicate key 'Milk' = 7.
"""

# (c) Which statements are correct?
"""
i.  A dictionary always has unique keys – ✅ Correct
ii. Each key may have multiple values – ❌
iii.If same key reassigned, latest value prevails – ✅
"""

# (d) Creating empty structures
empty_list, empty_tuple, empty_set, empty_dict = [], (), set(), {}
print("Empty structures created:", empty_list, empty_tuple, empty_set, empty_dict)

# (e) One-element structures
one_list, one_tuple, one_set, one_dict = [10], (10,), {10}, {'a': 10}
print("One-element structures:", one_list, one_tuple, one_set, one_dict)

# (f) Access Mango and Winter from nested dict
d = {
    'd1': {'Fruitname': 'Mango', 'Season': 'Summer'},
    'd2': {'Fruitname': 'Orange', 'Season': 'Winter'}
}
print("Access Mango:", d['d1']['Fruitname'])
print("Access Winter:", d['d2']['Season'])

# (g) Property comparison table (see textbook)
"""
str  – Ordered, Immutable
list – Ordered, Mutable
tuple– Ordered, Immutable
set  – Unordered, Mutable, Unique
dict – Ordered (3.7+), Mutable, Key-Indexed
"""

# (h) Common usage of each datatype
"""
str  -> store text data
list -> sequence of items
tuple-> fixed record
set  -> unique collection
dict -> key–value mapping / lookup table
"""

print("\n--- End of Section C ---")
