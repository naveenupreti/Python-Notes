1️sort() vs sorted()

| Feature           | `sort()`                      | `sorted()`                                                  |
| ----------------- | ----------------------------- | ----------------------------------------------------------- |
| **Type**          | Method of a list              | Built-in function                                           |
| **Original list** | Changes the list **in-place** | Returns a **new sorted list**, original list stays the same |
| **Return value**  | `None`                        | New list                                                    |
| **Works on**      | Only lists                    | Any iterable (list, tuple, string, etc.)                    |

Example with sort() (in-place):

numbers = [4, 1, 7, 3]
numbers.sort()        # Sorts the list itself
print(numbers)        # Output: [1, 3, 4, 7]


Example with sorted() (returns new list):

numbers = [4, 1, 7, 3]
new_numbers = sorted(numbers)   # Returns a new sorted list
print(new_numbers)              # [1, 3, 4, 7]
print(numbers)                  # Original list unchanged: [4, 1, 7, 3]



2️reverse() vs reversed()
| Feature           | `reverse()`                    | `reversed()`                                                            |
| ----------------- | ------------------------------ | ----------------------------------------------------------------------- |
| **Type**          | Method of a list               | Built-in function                                                       |
| **Original list** | Reverses the list **in-place** | Returns an **iterator** that goes through the elements in reverse order |
| **Return value**  | `None`                         | Iterator (can convert to list using `list()`)                           |
| **Works on**      | Only lists                     | Any iterable                                                            |


Example with reverse() (in-place):

numbers = [1, 2, 3, 4]
numbers.reverse()     # Reverse the list itself
print(numbers)        # Output: [4, 3, 2, 1]


Example with reversed() (returns iterator):

numbers = [1, 2, 3, 4]
rev_numbers = reversed(numbers)   # Returns an iterator
print(list(rev_numbers))          # Convert to list: [4, 3, 2, 1]
print(numbers)                    # Original list unchanged: [1, 2, 3, 4]

'''
Quick summary:

sort() → sorts in-place, only lists.

sorted() → returns a new sorted list, works on any iterable.

reverse() → reverses in-place, only lists.

reversed() → returns an iterator in reverse order, works on any iterable.
'''