import pickle   # Used for binary serialization (Python → bytes → file)

# ------------------------------------------------------------
# Creating variables of ALL major Python built-in data types
# ------------------------------------------------------------

data = {
    "integer": 42,                  
    "float": 3.1415,                
    "boolean": True,                
    "string": "Hello Python",

    # Bytes (immutable) and bytearray (mutable)
    "bytes_data": b"ABC",                    # Raw bytes
    "byte_array": bytearray([10, 20, 30]),   # Mutable byte sequence

    # Sequences
    "list": [1, 2, 3],
    "tuple": (4, 5, 6),
    "range_obj": range(5),                   # 0–4

    # Set (mutable) and frozenset (immutable)
    "set_data": {7, 8, 9},
    "frozenset_data": frozenset({10, 11, 12}),

    # Mapping
    "dictionary": {"name": "Naveen", "age": 25},

    # Special data types
    "none_value": None,
    "complex_num": 2 + 3j,                   # Complex number
}

# ------------------------------------------------------------
# SERIALIZATION — Write all data types to a binary file
# ------------------------------------------------------------
with open("all_types.pkl", "wb") as f:
    pickle.dump(data, f)
    # pickle.dump() converts Python objects → binary bytes → writes to file

# ------------------------------------------------------------
# DESERIALIZATION — Read the data back exactly as original
# ------------------------------------------------------------
with open("all_types.pkl", "rb") as f:
    restored = pickle.load(f)
    # pickle.load() converts bytes → original Python objects

# ------------------------------------------------------------
# PRINTING RESTORED DATA WITH ITS DATA TYPE
# ------------------------------------------------------------
print("\nRestored data and their types:\n")

for key, value in restored.items():
    # {key:15} → left-aligned, 15-character width (clean table output)
    # {value!r} → prints raw Python representation (repr)
    # x = "Hello\nWorld"
    # print(f"{x}")      # Uses str() output: Hello and World are in 2 different lines
    # print(f"{x!r}")    # Uses repr() output: 'Hello\nWorld'
    #type(value) → gives the full type object (e.g., <class 'int'>)
    #type(value).__name__ → extracts only the type's name (e.g., "int")
    print(f"{key:15} → {value!r}   (type: {type(value).__name__})")

