import sys

# Dictionary of Python data types with default values
data_types = {
    "int": 0,
    "float": 0.0,
    "complex": 0 + 0j,
    "bool": False,
    "str": "",
    "list": [],
    "tuple": (),
    "range": range(0),
    "set": set(),
    "frozenset": frozenset(),
    "dict": {},
    "bytes": b'',
    "bytearray": bytearray(),
    "memoryview": memoryview(b''),
    "NoneType": None,
}

# Function to get min/max if applicable
def get_min_max(value):
    if isinstance(value, int):
        return "Unlimited", "Unlimited"
    elif isinstance(value, float):
        return sys.float_info.min, sys.float_info.max
    elif isinstance(value, complex):
        return f"Real: {sys.float_info.min}", f"Real: {sys.float_info.max}"
    elif isinstance(value, bool):
        return 0, 1
    else:
        return "-", "-"

# Print details data type wise
for dtype, value in data_types.items():
    min_val, max_val = get_min_max(value)
    print(f"Data Type      : {dtype}")
    print(f"Default Value  : {value}")
    print(f"ID             : {id(value)}")
    print(f"Class          : {type(value)}")
    print(f"Size (bytes)   : {sys.getsizeof(value)}")
    print(f"Min Value      : {min_val}")
    print(f"Max Value      : {max_val}")
    print("-" * 50)
