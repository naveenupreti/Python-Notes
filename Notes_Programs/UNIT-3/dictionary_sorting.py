'''
itemgetter() is a function from Python’s built-in operator module.
It is used to fetch a specific item (or items) from an object — like a
tuple, list, or dictionary entry — by its index or key.
'''
# Python program to sort a dictionary
from operator import itemgetter

# Original dictionary
my_dict = {'banana': 3, 'apple': 5, 'cherry': 1, 'mango': 2}

print("Original Dictionary:")
print(my_dict)

# ---- Sort by KEYS ----
# Ascending order
sorted_by_keys_asc = dict(sorted(my_dict.items(), key=itemgetter(0)))
print("\nSorted by keys (ascending):")
print(sorted_by_keys_asc)

# Descending order
sorted_by_keys_desc = dict(sorted(my_dict.items(), key=itemgetter(0), reverse=True))
print("\nSorted by keys (descending):")
print(sorted_by_keys_desc)

# ---- Sort by VALUES ----
# Ascending order
sorted_by_values_asc = dict(sorted(my_dict.items(), key=itemgetter(1)))
print("\nSorted by values (ascending):")
print(sorted_by_values_asc)

# Descending order
sorted_by_values_desc = dict(sorted(my_dict.items(), key=itemgetter(1), reverse=True))
print("\nSorted by values (descending):")
print(sorted_by_values_desc)
