# Tuple Unpacking Examples in Python

# 1. Basic unpacking
a, b, c = 1, 2, 3
print("Basic unpacking:")
print(f"a={a}, b={b}, c={c}")  # a=1, b=2, c=3
print("-"*40)

# 2. Swapping variables without a temp variable
x, y = 5, 10
x, y = y, x
print("Swapping variables:")
print(f"x={x}, y={y}")  # x=10, y=5
print("-"*40)

# 3. Returning multiple values from a function
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([4, 7, 1, 9])
print("Function returning multiple values:")
print(f"low={low}, high={high}")  # low=1, high=9
print("-"*40)

# 4. Iterating over list of tuples
points = [(1, 2), (3, 4), (5, 6)]
print("Iterating over list of tuples:")
for x, y in points:
    print(f"x={x}, y={y}")
# Output:
# x=1, y=2
# x=3, y=4
# x=5, y=6
print("-"*40)

# 5. Ignoring unneeded values
data = (10, 20, 30)
a, _, c = data
print("Ignoring unneeded values:")
print(f"a={a}, c={c}")  # a=10, c=30
print("-"*40)

# 6. Variable-length unpacking
numbers = [1, 2, 3, 4, 5]
a, *middle, z = numbers
print("Variable-length unpacking:")
print(f"a={a}")        # a=1
print(f"middle={middle}")  # middle=[2, 3, 4]
print(f"z={z}")        # z=5
print("-"*40)
