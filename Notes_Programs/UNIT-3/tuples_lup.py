'''
Tuples 
--------------------------------
'''

# Standard library imports used in examples
import operator  # used later for sorting by a specific field in tuple records
from typing import Tuple, List  # only for readable type hints in comments (not required)

# ---------------------------------------------------------------------------
# Pretty separators (just using prints; no helper functions since user asked
# for a single-file, linear script without functions)
# ---------------------------------------------------------------------------

# Print a header for the demo run
print("\nDemo run: Chapter 9 - Tuples examples and exercises")  # top-level header
print("=" * 72)  # underline for visual separation

# ---------------------------------------------------------------------------
# Example 1: Tuple creation and types
# ---------------------------------------------------------------------------

print("\nDemo: tuple creation and types")  # section title
print("-" * 40)  # thin separator

empty_tuple = ()  # create an empty tuple using empty parentheses
print("empty_tuple:", empty_tuple)  # show the empty tuple value

print("type(empty_tuple):", type(empty_tuple))  # show that the type is tuple

one_item = ("Sanjay",)  # single-element tuple requires a trailing comma
print("one_item:", one_item)  # prints the one-item tuple

print("type(one_item):", type(one_item))  # confirm single-item tuple is tuple

without_parens = "Sanjay", 123, True  # tuple packing without parentheses
print("without_parens:", without_parens)  # packed tuple printed

print("type(without_parens):", type(without_parens))  # type is tuple

int_tuple = (1, 2, 3, 4)  # homogeneous tuple of integers
print("int_tuple:", int_tuple)  # print integer tuple

repeated = (1,) * 5  # replicate a single-element tuple five times
print("repeated:", repeated)  # prints (1, 1, 1, 1, 1)

concat = (1, 2) + (3, 4)  # concatenate two tuples to create a new tuple
print("concat:", concat)  # prints (1, 2, 3, 4)

# ---------------------------------------------------------------------------
# Example 2: Indexing and slicing
# ---------------------------------------------------------------------------

print("\nDemo: indexing & slicing")  # section title
print("-" * 40)  # separator

tpl = ("Handle", "Exceptions", "Like", "a", "boss")  # example tuple
print("tpl:", tpl)  # show the full tuple

print("tpl[0]:", tpl[0])  # first element (index 0)
print("tpl[2]:", tpl[2])  # third element (index 2)

print("tpl[-1]:", tpl[-1])  # negative index -1 -> last element

print("tpl[1:4]:", tpl[1:4])  # slice from index 1 up to (not including) 4

print("tpl[:3]:", tpl[:3])  # slice with omitted start -> from beginning to index 3
print("tpl[2:]:", tpl[2:])  # slice from index 2 to the end

# ---------------------------------------------------------------------------
# Example 3: Iteration and enumerate
# ---------------------------------------------------------------------------

print("\nDemo: iteration & enumerate")  # section title
print("-" * 40)  # separator

fruits = ("apple", "banana", "cherry", "date")  # tuple with 4 items

i = 0  # initialize loop counter for while loop
while i < len(fruits):  # loop until index equals tuple length
    print(f"while loop index {i} ->", fruits[i])  # print element at index i
    i += 1  # increment index

for fruit in fruits:  # for-loop: iterate directly over tuple elements
    print("for loop element ->", fruit)  # print current element

for i in range(len(fruits)):
    print(f"Index {i} -> {fruits[i]}") # print element at index i
    
for index, element in enumerate(fruits):  # enumerate yields (index, element)
    print(f"enumerate: index {index} ->", element)  # show both index and value
    
'''
range(start, stop, step)
start → starting value
stop → stopping value (not included)
step → increment (can be negative for reverse)

len(fruits) - 1 = 4-1=3
So, range(3, -1, -1) is interpreted as
start = 3 → begin at index 3 ("mango")
stop = -1 → stop before -1, i.e., the loop will end when it reaches index 0
step = -1 → move backwards (decrease by 1 each time)
'''
#printing tuple in reverse
for i in range(len(fruits) - 1, -1, -1):
    print(f"Index {i} -> {fruits[i]}")

# ---------------------------------------------------------------------------
# Example 4: Mutability, immutability and tuples containing mutable objects
# ---------------------------------------------------------------------------

print("\nDemo: immutability & mutable elements inside a tuple")  # title
print("-" * 40)  # separator

msg = ("Fall", "In", "Line")  # tuple of strings (immutable elements)
print("original msg:", msg)  # show original tuple

try:
    msg[0] = "FALL"  # attempt to assign to tuple element (should raise TypeError)
except TypeError as exc:  # catch the immutability error to explain behavior
    print("Attempting msg[0] = 'FALL' raised:", type(exc).__name__, "-", exc)

s = ([1, 2, 3, 4], [4, 5], "Ocelot")  # tuple containing lists (mutable) and a string
print("before modifying inner list s:", s)  # show tuple before mutation of inner list

s[0][1] = 99  # change second element of the first inner list (lists are mutable)
print("after modifying s[0][1] =", s[0][1], "- s becomes:", s)  # change visible in tuple

p = s[0]  # assign reference to the inner list to variable p
p[0] = 500  # mutate the list through the variable reference
print("after p[0] = 500 -> s:", s)  # mutation is reflected inside tuple

# ---------------------------------------------------------------------------
# Example 5: Common tuple operations & builtins
# ---------------------------------------------------------------------------

print("\nDemo: basic ops & built-in functions")  # title
print("-" * 40)  # separator

t = (10, 20, 30, 20, 40)  # numeric tuple (contains a repeated 20)

print("len(t):", len(t))  # length of the tuple (number of elements)
print("min(t):", min(t))  # smallest numeric element in t
print("max(t):", max(t))  # largest numeric element in t
print("sum(t):", sum(t))  # sum of all numeric elements in t

print("any(t):", any(t))  # True if any element is truthy (non-zero here)
print("all(t):", all(t))  # True if all elements are truthy (non-zero here)

print("sorted(t):", sorted(t))  # returns a new list containing sorted elements

print("list(reversed(t)):", list(reversed(t)))  # reversed returns an iterator -> convert to list

# Demonstrate tuple methods count() and index() with safe handling
print("\nDemo: tuple methods (count & index)")  # mini-title
print("-" * 24)  # small separator

tpl = (1, 2, 3, 2, 2, 5)  # tuple that contains multiple occurrences of 2
print("tpl:", tpl)  # show the tuple

print("tpl.count(2):", tpl.count(2))  # count occurrences of value 2
print("tpl.index(3):", tpl.index(3))  # index() returns first matching index for 3

try:
    print("tpl.index(99):", tpl.index(99))  # attempt to find index of missing value 99
except ValueError as exc:  # index raises ValueError when element not found
    print("tpl.index(99) raised:", type(exc).__name__, "-", exc)  # show the exception

# ---------------------------------------------------------------------------
# Example 6: Tuple of tuples, nested indexing and unpacking (including star unpack)
# ---------------------------------------------------------------------------

print("\nDemo: tuple-of-tuples, nested indexing and unpacking")  # title
print("-" * 40)  # separator

a = (1, 2, 3)  # simple tuple
b = (4, 5, 6)  # another tuple
c = (a, b)  # tuple containing tuples
print("c:", c)  # show nested tuple structure

print("c[0][0]:", c[0][0])  # index into first inner tuple then its first element
print("c[1][2]:", c[1][2])  # index into second inner tuple then its third element

records = (  # tuple containing record-tuples (name, age, salary)
    ("Priyanka", 24, 25000),
    ("Shailesh", 25, 30000),
    ("Subhash", 23, 22000),
)
print("records[0]:", records[0])  # show first record tuple

for name, age, salary in records:  # unpack each record tuple into variables
    print("record:", name, age, salary)  # display unpacked fields

x = (1, 2, 3, 4)  # example tuple to demonstrate star-unpacking
y = (10, 20, *x, 30)  # star-unpack x inside a new tuple y
print("y after star-unpacking x:", y)  # show resulting tuple

# ---------------------------------------------------------------------------
# Example 7: Sorting a list/tuple of tuples with operator.itemgetter()
# ---------------------------------------------------------------------------

print("\nDemo: sort list-of-tuples using operator.itemgetter")  # title
print("-" * 40)  # separator

lst = [("Shailesh", 25, 30000), ("Priyanka", 24, 25000)]  # list of tuples (records)
tpl_of_tuples = (("Shailesh", 25, 30000), ("Priyanka", 24, 25000))  # tuple-of-tuples

print("sorted(lst):", sorted(lst))  # default sort sorts by first element (name)
print("sorted(tpl_of_tuples):", sorted(tpl_of_tuples))  # same, but returns a list

# sort by salary (3rd field -> index 2) using operator.itemgetter
print(
    "sorted(lst, key=operator.itemgetter(2)):",
    sorted(lst, key=operator.itemgetter(2)),
)  # sorts by salary ascending

print(
    "sorted(tpl_of_tuples, key=operator.itemgetter(2)):",
    sorted(tpl_of_tuples, key=operator.itemgetter(2)),
)  # same for tuple-of-tuples (converted to list internally)

# ---------------------------------------------------------------------------
# Problem 8-1: divmod with tuple
# ---------------------------------------------------------------------------

print("\nProblem 8-1: divmod with tuple")  # problem header
print("-" * 40)  # separator

t = (10, 3)  # tuple containing (dividend, divisor)
print("t:", t)  # show tuple

result = divmod(*t)  # unpack tuple into two args for divmod()
print("divmod(*t):", result)  # prints (quotient, remainder)

# ---------------------------------------------------------------------------
# Problem 8-2: packing & unpacking examples
# ---------------------------------------------------------------------------

print("\nProblem 8-2: packing & unpacking examples")  # problem header
print("-" * 40)  # separator

tpl = tuple(i * 10 for i in range(1, 11))  # pack first 10 multiples of 10 into a tuple
print("tpl:", tpl)  # print the packed tuple

# full unpack into ten variables (explicit)
a, b, c, d, e, f, g, h, i, j = tpl  # unpack each element into separate variables
print("a..j unpacked values:", a, b, c, d, e, f, g, h, i, j)  # show unpacked values

# star-unpacking with discard variable `_`
x, *_, y = tpl  # first -> x, last -> y, middle elements captured in `_` list
print("x, y and discarded middle _ ->", x, y, _)  # show first, last and `_` contents

i_first, *_middle, j_last = tpl  # another unpack: first, middle list, last
print("i_first, j_last, middle-list _ ->", i_first, j_last, _middle)  # show values

# ---------------------------------------------------------------------------
# Problem 8-3: count boys (tuple entries) and girls (strings)
# ---------------------------------------------------------------------------

print("\nProblem 8-3: count boys (tuple entries) and girls (strings)")  # header
print("-" * 40)  # separator

lst = ["Shubha", "Nisha", "Sudha", ("Suresh",), ("Rajesh",), "Radha"]  # mixed list
boys = 0  # initialize boy counter
girls = 0  # initialize girl counter

for ele in lst:  # iterate through elements of the list
    if isinstance(ele, tuple):  # per problem, tuple entries denote boys
        boys += 1  # increment boys count
    else:
        girls += 1  # otherwise increment girls count

print("Boys:", boys, "Girls:", girls)  # display final counts

# ---------------------------------------------------------------------------
# Problem 8-4: gather names from list of tuples
# ---------------------------------------------------------------------------

print("\nProblem 8-4: gather names from list of tuples")  # header
print("-" * 40)  # separator

lst_records = [(101, "Shubha", 21), (102, "Nisha", 22), (103, "Sudha", 20)]  # sample records
nlst = []  # create an empty list to collect names

for ele in lst_records:  # iterate each tuple record
    nlst.append(ele[1])  # ele[1] is the name field; append it to nlst

print("names extracted:", nlst)  # print collected list of names

# ---------------------------------------------------------------------------
# Problem 8-5: operations on a character tuple "Flabbergasted"
# ---------------------------------------------------------------------------

print("\nProblem 8-5: operations on a character tuple")  # header
print("-" * 40)  # separator

tpl_chars = tuple("Flabbergasted")  # convert string into tuple of characters
print("original tpl:", tpl_chars)  # print tuple of characters

tpl_chars = tpl_chars + ("!",)  # add '!' by concatenation (tuples are immutable -> new tuple)
print("after adding '!':", tpl_chars)  # show new tuple with '!'

s_joined = "".join(tpl_chars)  # join characters back into a single string
print("joined string:", s_joined)  # show joined string

# find indices of character 'b' within the tuple
b_indices = [idx for idx, ch in enumerate(tpl_chars) if ch == "b"]  # list comprehension for indices
print("indices of 'b':", b_indices)  # show indices of 'b'

# slice to extract the contiguous portion that contains the two 'b' characters
bb = tpl_chars[3:5]  # slice positions 3 and 4 -> ('b', 'b') in this example
print("extracted ('b','b') via slice:", bb)  # print sliced tuple

print("tpl.count('e'):", tpl_chars.count("e"))  # count occurrences of 'e' in the tuple

print("'r' in tpl ? ->", "r" in tpl_chars)  # membership test for 'r'

lst_from_tpl = list(tpl_chars)  # convert tuple to list for mutability
print("as list:", lst_from_tpl)  # print the list version

to_remove = {"b", "e", "r"}  # set of characters we want to remove
tpl_filtered = tuple(ch for ch in tpl_chars if ch not in to_remove)  # rebuild tuple excluding removals
print("after removing b, e, r:", tpl_filtered)  # show filtered tuple

# ---------------------------------------------------------------------------
# Exercises [A] & [B] — Answers and Explanations (end-of-chapter conceptual)
# ---------------------------------------------------------------------------

print("\nExercises [A] & [B] — Answers and Explanations")  # header
print("-" * 72)  # underline separator

# Exercise [A]: property applicability mapping (String, List, Tuple)
properties = [
    "Iterable",
    "Sliceable",
    "Indexable",
    "Immutable",
    "Sequence",
    "Can be empty",
    "Sorted collection (intrinsic)",
    "Ordered collection",
    "Unordered collection",
    "Elements can be accessed using their position in the collection",
]  # list of properties to evaluate

# mapping answers as tuples of booleans (string, list, tuple)
answers_A = {
    "Iterable": (True, True, True),  # all are iterable
    "Sliceable": (True, True, True),  # slicing supported by all
    "Indexable": (True, True, True),  # index access supported by all
    "Immutable": (True, False, True),  # strings & tuples immutable, lists mutable
    "Sequence": (True, True, True),  # all are sequence types
    "Can be empty": (True, True, True),  # '' , [] , () can be empty
    "Sorted collection (intrinsic)": (False, False, False),  # none are intrinsically sorted
    "Ordered collection": (True, True, True),  # insertion order is preserved
    "Unordered collection": (False, False, False),  # not applicable here
    "Elements can be accessed using their position in the collection": (True, True, True),
}  # dictionary containing boolean triples per property

print("Exercise [A]: Property applicability (String, List, Tuple):")  # explanatory line
for prop in properties:  # iterate property list in defined order
    val = answers_A[prop]  # get answer triple for the property
    print(f" - {prop:55} -> String: {val[0]}, List: {val[1]}, Tuple: {val[2]}")  # print mapping

# short justification for Exercise [A]
print(
    "\nJustification (brief): strings/lists/tuples are iterable, sliceable and "
    "indexable. Strings and tuples are immutable; lists are mutable. All are "
    "ordered sequences that can be empty. None are intrinsically 'sorted' by "
    "definition."
)  # printed justification text

# Exercise [B]: operation applicability for string, list, tuple
print("\nExercise [B]: Operation applicability (String, List, Tuple):")  # header

operations_answers = {
    "a = b + c (concatenation)": (True, True, True),  # concatenation returns a new object
    "a = b * n (repetition)": (True, True, True),  # repetition returns a new object
    "Appending a new element at the end": (False, True, False),  # list only
    "Deletion of an element at the ith position": (False, True, False),  # list only
    "Modification of last element": (False, True, False),  # list only (mutable)
    "In-place reversal (e.g. list.reverse())": (False, True, False),  # list only
}  # mapping of operations to applicability triples

for op, ans in operations_answers.items():  # iterate operations & answers
    print(f" - {op:55} -> String: {ans[0]}, List: {ans[1]}, Tuple: {ans[2]}")  # pretty-print mapping

# summary for Exercise [B]
print(
    "\nSummary: concatenation and repetition produce new objects and are "
    "supported by strings, lists and tuples. Mutating operations (append, "
    "delete, in-place modification, in-place reversal) are supported only "
    "by mutable sequence types such as lists."
)  # print final summary

# ---------------------------------------------------------------------------
# End of script
# ---------------------------------------------------------------------------

print("\nEnd of Chapter 9 Tuples demo script.")  # final footer
print("=" * 72)  # closing underline

