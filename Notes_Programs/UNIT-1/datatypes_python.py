"""
Program: Display details about all major Python built-in data types.
This file includes:
    ✔ Inline comments explaining each part of code
    ✔ Use of dictionary to store data types with default values
    ✔ Function to compute min/max values where applicable
    ✔ Printing details such as ID, size, class, min/max value
    ✔ Sample output included at the bottom
"""

# ---------------------------------------------------------
# IMPORT STATEMENTS
# ---------------------------------------------------------
import sys     # sys module used for system-level information (float limits, size of objects, etc.)

# ---------------------------------------------------------
# DICTIONARY OF PYTHON DATA TYPES WITH DEFAULT VALUES
# Each key is a type name, and each value is its default value.
# ---------------------------------------------------------
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

# ---------------------------------------------------------
# FUNCTION: Return min/max value for selected data types
# ---------------------------------------------------------
def get_min_max(value):
    """
    Returns (min, max) values for numeric types.
    For others, returns '-' as not applicable.
    """
    if isinstance(value, int):
        # Python integers are unbounded
        return "Unlimited", "Unlimited"

    elif isinstance(value, float):
        # sys.float_info gives machine-level float limits
        return sys.float_info.min, sys.float_info.max

    elif isinstance(value, complex):
        # Complex numbers have no min/max; only real/imag float limits
        return f"Real Min: {sys.float_info.min}", f"Real Max: {sys.float_info.max}"

    elif isinstance(value, bool):
        return 0, 1

    # For non-numeric types
    return "-", "-"

# ---------------------------------------------------------
# PRINT DETAILS FOR EACH DATA TYPE
# ---------------------------------------------------------
for dtype, value in data_types.items():
    min_val, max_val = get_min_max(value)

    print(f"Data Type      : {dtype}")
    print(f"Default Value  : {value}")
    print(f"ID             : {id(value)}")            # Memory ID of object
    print(f"Class          : {type(value)}")         # Shows class/type of value
    print(f"Size (bytes)   : {sys.getsizeof(value)}") # Memory size of object
    print(f"Min Value      : {min_val}")
    print(f"Max Value      : {max_val}")
    print("-" * 50)  # Divider line


# ---------------------------------------------------------
# SAMPLE OUTPUT (Not executed — for reference only)
# ---------------------------------------------------------
"""
=================== SAMPLE OUTPUT ===================

Data Type      : int
Default Value  : 0
ID             : 140723477466864
Class          : <class 'int'>
Size (bytes)   : 24
Min Value      : Unlimited
Max Value      : Unlimited
--------------------------------------------------
Data Type      : float
Default Value  : 0.0
ID             : 140723477469648
Class          : <class 'float'>
Size (bytes)   : 24
Min Value      : 2.2250738585072014e-308
Max Value      : 1.7976931348623157e+308
--------------------------------------------------
Data Type      : complex
Default Value  : 0j
ID             : 140723477474832
Class          : <class 'complex'>
Size (bytes)   : 32
Min Value      : Real Min: 2.2250738585072014e-308
Max Value      : Real Max: 1.7976931348623157e+308
--------------------------------------------------
Data Type      : bool
Default Value  : False
ID             : 9480544
Class          : <class 'bool'>
Size (bytes)   : 28
Min Value      : 0
Max Value      : 1
--------------------------------------------------
... (similar output for all remaining data types)

=====================================================
"""
